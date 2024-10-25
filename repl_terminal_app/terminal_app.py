import threading
import tkinter as tk
from tkinter import scrolledtext

from swarm import Swarm
from agents.triage_agent import triage_agent  # 请根据实际路径导入

from repl_terminal_app.repl import process_and_print_streaming_response  # 导入库函数
# 如果 format_arguments 在 repl.py 中定义，也需要导入
from repl_terminal_app.repl import format_arguments

import os
import openai

# 设置 OpenAI API 密钥
openai.api_key = os.environ.get("OPENAI_API_KEY")

class TerminalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Quote Terminal")

        # 创建用于显示输出的滚动文本区域
        self.text_area = scrolledtext.ScrolledText(self.root, height=20, width=80)
        self.text_area.pack(pady=10)
        self.text_area.configure(state='disabled')

        # 定义文本标签，用于设置颜色和样式
        self.text_area.tag_configure('blue', foreground='blue')
        self.text_area.tag_configure('purple', foreground='purple')
        self.text_area.tag_configure('gray', foreground='gray')
        self.text_area.tag_configure('bold', font=('Helvetica', 10, 'bold'))

        # 创建用于输入命令的输入框
        self.entry = tk.Entry(self.root, width=80)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.run_command)  # 绑定回车键事件

        # 初始化消息列表和当前代理
        self.messages = []
        self.agent = triage_agent

        # 创建 Swarm 客户端实例
        self.client = Swarm()

        # 显示初始提示
        self.display_text("AI Terminal is ready. Enter your commands below:\n", 'bold')
        self.display_text("$ ", 'gray')

    def run_command(self, event):
        user_input = self.entry.get()
        self.entry.delete(0, tk.END)

        # 显示用户输入
        self.display_text(f"{user_input}\n", 'gray')

        # 添加用户输入到消息列表
        self.messages.append({"role": "user", "content": user_input})

        # 启动新线程运行代理
        threading.Thread(target=self.run_agent).start()

    def run_agent(self):
        # 显示启动信息
        self.display_text("Starting Swarm CLI 🐝\n", 'bold')

        # 运行代理，获取响应
        response = self.client.run(
            agent=self.agent,
            messages=self.messages,
            context_variables={},
            stream=True,
            debug=False
        )

        # 处理流式响应
        process_and_print_streaming_response(response, self.display_text)

    def display_text(self, text, *tags):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, text, tags)
        self.text_area.configure(state='disabled')
        self.text_area.see(tk.END)
