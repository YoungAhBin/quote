# mingyuan.py
from swarm.core import Result
import json

def fixed_height_buy_width(width_m, height_m, curtain_type):
    pleat_base = (width_m * 2) / 0.25
    pleat_count = round(pleat_base)
    if pleat_count % 2 != 0:
        pleat_count += 1
    pleats = pleat_count - 2

    if curtain_type == '纱帘':
        main_fabric_quantity = pleats * 0.25m + 0.3m
    else:
        main_fabric_quantity = pleats * 0.25m + 0.3m + 0.2m

    return main_fabric_quantity

def fixed_width_buy_height(width_m, height_m, curtain_type):
    pleat_base = (width_m * 2) / 0.25
    pleat_count = round(pleat_base)
    if pleat_count % 2 != 0:
        pleat_count += 1
    pleats = pleat_count - 2
    width_count = round((pleats * 0.25 + 0.3) / 2.8)

    if curtain_type == '纱帘':
        main_fabric_quantity = width_count * (height_m + 0.2m)
    else:
        main_fabric_quantity = width_count * (height_m + 0.2m) + 0.2m

    return main_fabric_quantity

def calculate_fabric_cost(width_m, height_m, curtain_type):
    """
    计算布料成本，根据高度选择相应的计算方法。

    Returns:
        Result: 包含成本和主布数量的 Result 对象。
    """
    UNIT_PRICE = 50  # 假设单价为 50 元

    if height_m > 2.8:
        main_fabric_quantity = fixed_width_buy_height(width_m, height_m, curtain_type)
    else:
        main_fabric_quantity = fixed_height_buy_width(width_m, height_m, curtain_type)

    cost = main_fabric_quantity * UNIT_PRICE

    # 返回成本和主布数量
    return Result(
        value=json.dumps({"cost": cost, "main_fabric_quantity": main_fabric_quantity}),
        agent=None,
        context_variables={}
    )
