import json

def process_and_print_streaming_response(response, display_text):
    content = ""
    last_sender = ""

    for chunk in response:
        if "sender" in chunk:
            last_sender = chunk["sender"]

        if "content" in chunk and chunk["content"] is not None:
            if not content and last_sender:
                display_text(f"\n{last_sender}: ", 'blue', 'bold')
                last_sender = ""  # 与库函数一致，重置 last_sender
            display_text(chunk["content"])
            content += chunk["content"]

        if "tool_calls" in chunk and chunk["tool_calls"] is not None:
            for tool_call in chunk["tool_calls"]:
                f = tool_call["function"]
                name = f["name"]
                if not name:
                    continue
                args = f.get("arguments", "{}")
                arg_str = format_arguments(args)
                # 在工具调用时使用 last_sender，但不重置
                display_text(f"\n{last_sender}: ", 'blue', 'bold')
                display_text(f"{name}({arg_str})", 'purple')

        if "delim" in chunk and chunk["delim"] == "end" and content:
            display_text("\n")
            content = ""
            last_sender = ""  # 在消息结束时重置 last_sender

        if "response" in chunk:
            return chunk["response"]

def format_arguments(args):
    try:
        arg_json = json.dumps(json.loads(args))
        arg_str = arg_json.replace(":", "=")
        if arg_str.startswith("{") and arg_str.endswith("}"):
            arg_str = arg_str[1:-1]  # 去除首尾的花括号
    except json.JSONDecodeError:
        arg_str = args  # 解析失败，直接使用原始字符串
    return arg_str
