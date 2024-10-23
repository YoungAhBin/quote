# main.py

import os
import openai

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

import streamlit as st
from repl import run_streamlit_conversation  # 导入 repl.py 中的函数
from agents.triage_agent import triage_agent  # 确保正确导入

# 主程序
st.title("智能成本计算器")

run_streamlit_conversation(
    starting_agent=triage_agent,
    context_variables=None,
    stream=True,
    debug=False
)
