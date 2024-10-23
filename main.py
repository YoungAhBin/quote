# main.py

import os
import openai

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

from swarm.repl import run_demo_loop
from agents.triage_agent import triage_agent  # 确保正确导入

run_demo_loop(
    starting_agent=triage_agent,
    context_variables=None,
    stream=True,
    debug=False
)
