import os
import openai
import json
import time
import streamlit as st
from swarm import Swarm
from agents.triage_agent import triage_agent  # 使用 triage_agent 作为初始代理

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 创建 Swarm 客户端
client = Swarm()

# 初始化 Streamlit 的 session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # 用于存储所有对话历史
if "agent" not in st.session_state:
    st.session_state.agent = triage_agent  # 初始代理设为 triage_agent

# 应用标题
st.title("智能成本计算器 - 多轮交互模式")

# 用户输入
user_input = st.text_area("请输入您的请求：例如宽: 6800, 高: 2700, 类型: 布帘, 厂家: mingyuan, 面料型号: 186A素色布")

if st.button("提交"):
    if user_input.strip() != "":
        # 将用户输入添加到消息列表中
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 占位符用于逐步更新 AI 的响应
        response_placeholder = st.empty()

        # 调用代理获取响应（支持流式输出）
        stream = client.run(
            agent=st.session_state.agent,
            messages=st.session_state.messages,
            stream=True,  # 启用流式生成
        )

        # 逐步处理流式输出
        aggregated_response_content = ""
        for chunk in stream:
            # 每个 chunk 是流的一部分
            if "content" in chunk:
                aggregated_response_content += chunk["content"]
                response_placeholder.write(f"**AI 回复：**\n{aggregated_response_content}")

            # 如果流的部分有结束信号（比如 delim 的 "end"）
            if "delim" in chunk and chunk["delim"] == "end":
                break

        # 最终将整个响应对象更新到对话历史中
        final_response = chunk.get("response")
        if final_response:
            st.session_state.messages.extend(final_response.messages)
            st.session_state.agent = final_response.agent  # 更新代理状态

# 显示对话历史
st.write("### 对话历史")
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**用户：** {message['content']}")
    elif message["role"] == "assistant":
        st.write(f"**AI：** {message['content']}")
