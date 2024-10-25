import json
from swarm import Swarm

def process_and_print_streaming_response(response, display_text):
    content = ""
    last_sender = ""

    for chunk in response:
        if "sender" in chunk:
            last_sender = chunk["sender"]

        if "content" in chunk and chunk["content"] is not None:
            if not content and last_sender:
                display_text(f"\n{last_sender}: ", 'blue', 'bold')
                last_sender = ""
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
                display_text(f"\n{last_sender}: ", 'blue', 'bold')
                display_text(f"{name}({arg_str})", 'purple')

        if "delim" in chunk and chunk["delim"] == "end" and content:
            display_text("\n")
            content = ""
            last_sender = ""

        if "response" in chunk:
            return chunk["response"]

def format_arguments(args):
    try:
        arg_json = json.dumps(json.loads(args))
        arg_str = arg_json.replace(":", "=")
        if arg_str.startswith("{") and arg_str.endswith("}"):
            arg_str = arg_str[1:-1]
    except json.JSONDecodeError:
        arg_str = args
    return arg_str

def run_agent(client, agent, messages, display_text, context_variables=None, stream=True, debug=False):
    # 显示启动信息
    display_text("Starting Swarm CLI 🐝\n", 'bold')

    # 运行代理，获取响应
    response = client.run(
        agent=agent,
        messages=messages,
        context_variables=context_variables or {},
        stream=stream,
        debug=debug
    )

    # 处理流式响应
    process_and_print_streaming_response(response, display_text)

    return response
