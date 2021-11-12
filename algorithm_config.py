
strategy_map = {
    'BFRM': 1,
    'MRFM': 2,
    'GOFRM': 3
}

config = {
    'strategy': 2,
    'is_big_cycle_filter': False
    # 理论上不跳过奇数大环（False），2和3的效率会高一点。但是现在是2比1少了一倍，3比1多了50%？
    # 如果是True的话，2比1略高，3比1高10%
    # 感觉2（MRFM）实现可能还是有点点问题
}


def set_config(key, value):
    config[key] = value
