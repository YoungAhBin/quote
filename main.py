import streamlit as st
from swarm import Swarm
from agents.fabric_agent import fabric_agent

client = Swarm()

st.title("布料成本计算器")

user_input = st.text_area("请输入您的请求：", "")

if st.button("提交"):
    response = client.run(
        agent=fabric_agent,
        messages=[{"role": "user", "content": user_input}],
    )
    ai_reply = response.messages[-1]["content"]
    st.write("**AI 回复：**")
    st.write(ai_reply)
