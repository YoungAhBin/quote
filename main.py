import os
import openai
import json

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

import streamlit as st
from swarm import Swarm
from agents.triage_agent import triage_agent

client = Swarm()

st.title("布料成本计算器")

user_input = st.text_area("请输入您的请求：宽: 6800, 高: 2700, 类型: 布帘, 厂家: mingyuan, 面料型号: 186A素色布 ")

if st.button("提交"):
    response = client.run(
        agent=fabric_agent,
        messages=[{"role": "user", "content": user_input}],
    )
    ai_reply = response.messages[-1]["content"]
    st.write("**AI 回复：**")
    st.write(ai_reply)
