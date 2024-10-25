import os
import threading
import tkinter as tk
from tkinter import scrolledtext
import json

import openai
from swarm import Swarm
from agents.triage_agent import triage_agent  # 请根据实际路径导入

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
        self.process_and_print_streaming_response(response)

    def process_and_print_streaming_response(self, response):
        content = ""
        last_sender = ""

        for chunk in response:
            if "sender" in chunk:
                last_sender = chunk["sender"]

            if "content" in chunk and chunk["content"] is not None:
                if not content and last_sender:
                    self.display_text(f"\n{last_sender}: ", 'blue', 'bold')
                    last_sender = ""  # 与库函数一致，重置 last_sender
                self.display_text(chunk["content"])
                content += chunk["content"]

            if "tool_calls" in chunk and chunk["tool_calls"] is not None:
                for tool_call in chunk["tool_calls"]:
                    f = tool_call["function"]
                    name = f["name"]
                    if not name:
                        continue
                    args = f.get("arguments", "{}")
                    arg_str = self.format_arguments(args)
                    # 在工具调用时使用 last_sender，但不重置
                    self.display_text(f"\n{last_sender}: ", 'blue', 'bold')
                    self.display_text(f"{name}({arg_str})", 'purple')

            if "delim" in chunk and chunk["delim"] == "end" and content:
                self.display_text("\n")
                content = ""
                last_sender = ""  # 在消息结束时重置 last_sender

            if "response" in chunk:
                # 更新代理和消息列表
                self.agent = chunk["response"].agent
                self.messages.extend(chunk["response"].messages)
                return

    def format_arguments(self, args):
        try:
            arg_json = json.dumps(json.loads(args))
            arg_str = arg_json.replace(":", "=")
            if arg_str.startswith("{") and arg_str.endswith("}"):
                arg_str = arg_str[1:-1]  # 去除首尾的花括号
        except json.JSONDecodeError:
            arg_str = args  # 解析失败，直接使用原始字符串
        return arg_str

    def display_text(self, text, *tags):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, text, tags)
        self.text_area.configure(state='disabled')
        self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalApp(root)
    root.mainloop()
