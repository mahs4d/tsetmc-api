def _load_raw_client_type_data(asset_id):
    client_types_raw = requests.get(f'http://www.tsetmc.com/tsev2/data/clienttype.aspx?i={asset_id}', timeout=5).text
    client_types_raw = client_types_raw.split(';')

    return client_types_raw


def _extract_client_type_history(raw_client_type_data):
    ret = []
    for client_type_day in raw_client_type_data:
        if client_type_day == '':
            continue

        tick_data = client_type_day.split(',')

        time = tick_data[0]
        individual_buy_count = tick_data[1]
        corporate_buy_count = tick_data[2]
        individual_sell_count = tick_data[3]
        corporate_sell_count = tick_data[4]
        individual_buy_vol = tick_data[5]
        corporate_buy_vol = tick_data[6]
        individual_sell_vol = tick_data[7]
        corporate_sell_vol = tick_data[8]
        individual_buy_value = tick_data[9]
        corporate_buy_value = tick_data[10]
        individual_sell_value = tick_data[11]
        corporate_sell_value = tick_data[12]

        ret.append({
            'time': time,  # todo: parse
            'individual_buy_count': int(individual_buy_count),
            'corporate_buy_count': int(corporate_buy_count),
            'individual_sell_count': int(individual_sell_count),
            'corporate_sell_count': int(corporate_sell_count),
            'individual_buy_volume': int(individual_buy_vol),
            'corporate_buy_volume': int(corporate_buy_vol),
            'individual_sell_volume': int(individual_sell_vol),
            'corporate_sell_volume': int(corporate_sell_vol),
            'individual_buy_value': int(individual_buy_value),
            'corporate_buy_value': int(corporate_buy_value),
            'individual_sell_value': int(individual_sell_value),
            'corporate_sell_value': int(corporate_sell_value),
        })

    return ret


def load_client_type_history_data(asset_id):
    """
    تاریخچه‌ی حقیقی حقوقی (نماد >‌ حقیقی حقوقی)
    """

    raw_client_type_data = _load_raw_client_type_data(asset_id)
    return _extract_client_type_history(raw_client_type_data)
