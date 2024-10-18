# mingyuan.py

def fixed_height_buy_width(width_m, height_m, curtain_type):
    # 原始计算逻辑
    pleat_base = (width_m * 2) / 0.25
    pleat_count = round(pleat_base)
    if pleat_count % 2 != 0:
        pleat_count += 1
    pleats = pleat_count - 2

    if curtain_type == '纱帘':
        main_fabric_quantity = pleats * 0.25 + 0.3
    else:
        main_fabric_quantity = pleats * 0.25 + 0.3 + 0.2

    return main_fabric_quantity

def fixed_width_buy_height(width_m, height_m, curtain_type):
    # 原始计算逻辑
    pleat_base = (width_m * 2) / 0.25
    pleat_count = round(pleat_base)
    if pleat_count % 2 != 0:
        pleat_count += 1
    pleats = pleat_count - 2
    width_count = round((pleats * 0.25 + 0.3) / 2.8)

    if curtain_type == '纱帘':
        main_fabric_quantity = width_count * (height_m + 0.2)
    else:
        main_fabric_quantity = width_count * (height_m + 0.2) + 0.2

    return main_fabric_quantity

def calculate_fabric_cost(width_m, height_m, curtain_type):
    """
    计算布料成本，根据高度选择相应的计算方法。
    """
    UNIT_PRICE = 50  # 假设单价为 50 元

    if height_m > 2.8:
        # 使用定宽买高
        main_fabric_quantity = fixed_width_buy_height(width_m, height_m, curtain_type)
    else:
        # 使用定高买宽
        main_fabric_quantity = fixed_height_buy_width(width_m, height_m, curtain_type)

    cost = main_fabric_quantity * UNIT_PRICE
    return cost
