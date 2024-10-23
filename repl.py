# repl.py

import json
import streamlit as st
from swarm import Swarm

def process_and_print_streaming_response(response_stream, update_callback=None):
    content = ""
    last_sender = ""
    assistant_message = ""

    for chunk in response_stream:
        if "sender" in chunk:
            last_sender = chunk["sender"]

        if "content" in chunk and chunk["content"] is not None:
            if not content and last_sender:
                assistant_message += f"**{last_sender}:** "
            assistant_message += chunk["content"]
            content += chunk["content"]
            if update_callback:
                update_callback(assistant_message)

        if "delim" in chunk and chunk["delim"] == "end" and content:
            # 回复结束，重置内容
            content = ""
            assistant_message = ""

        if "response" in chunk:
            return chunk["response"]

def pretty_print_messages(messages) -> None:
    for message in messages:
        if message["role"] != "assistant":
            continue

        # 显示 agent 名称
        sender = message.get('sender', 'AI')
        st.markdown(f"**{sender}:** {message['content']}")

def run_streamlit_conversation(
    starting_agent, context_variables=None, stream=False, debug=False
):
    client = Swarm()
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []
    if 'agent' not in st.session_state:
        st.session_state['agent'] = starting_agent
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = ''

    # 定义提交按钮的回调函数
    def submit():
        user_input = st.session_state['user_input']
        if user_input.strip():
            # 将用户输入添加到对话历史
            st.session_state['messages'].append({"role": "user", "content": user_input})

            # 创建一个占位符用于流式输出
            ai_response_placeholder = st.empty()

            # 定义更新回调函数
            def update_ai_reply(content):
                ai_response_placeholder.markdown(content)

            # 运行客户端，启用流式输出
            response_stream = client.run(
                agent=st.session_state['agent'],
                messages=st.session_state['messages'],
                context_variables=context_variables or {},
                stream=stream,
                debug=debug,
            )

            # 处理并显示流式响应
            response = process_and_print_streaming_response(response_stream, update_ai_reply)

            # 更新对话历史和 Agent
            st.session_state['messages'].extend(response.messages)
            st.session_state['agent'] = response.agent

            # 清空输入框
            st.session_state['user_input'] = ''

    # 定义清除对话的回调函数
    def clear_conversation():
        st.session_state['messages'] = []
        st.session_state['agent'] = starting_agent
        st.session_state['user_input'] = ''
        st.experimental_rerun()

    # 输入框在顶部
    st.text_input("请输入您的请求：", key='user_input')

    # 创建按钮，并指定回调函数
    col1, col2 = st.columns([1, 1])
    with col1:
        st.button("提交", on_click=submit)
    with col2:
        st.button("清除对话", on_click=clear_conversation)

    # 显示新的对话（最新的 AI 回复）
    if st.session_state['messages']:
        last_message = st.session_state['messages'][-1]
        if last_message["role"] == "assistant":
            sender = last_message.get('sender', 'AI')
            st.markdown(f"**{sender}:** {last_message['content']}")

    # 显示历史对话
    if len(st.session_state['messages']) > 1:
        st.markdown("---")
        st.markdown("**历史对话**")
        for message in st.session_state['messages'][:-1]:
            role = "用户" if message['role'] == 'user' else message.get('sender', 'AI')
            st.markdown(f"**{role}：** {message['content']}")
