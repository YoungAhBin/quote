# 创建布料代理
fabric_agent = Agent(
    name="布料代理",
    instructions="您负责根据用户提供的尺寸、类型和厂家，计算布料成本。",
    functions=[calculate_fabric_cost],
)
