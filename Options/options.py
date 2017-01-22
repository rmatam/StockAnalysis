# stocks = [] # extract all stocks on NYSE
stocks = ["DDD", "MMM", "WBAI"] # extract all stocks on NYSE

# features = ['open', 'high', 'low', 'close', 'volume', 'adj close', 'rsi_14', 'rsi_6', 'macd', 'boll_ub', 'boll_lb', 'tr', 'dma', 'pdi', 'mdi', 'trix', 'vr', 'cr', 'kdjk']
features = ['open', 'close',
'open_-1_r', # percent change in open from last day
'open_-2_r', # percent change in open from two days ago
'open_-3_r',
'open_-4_r',
'open_-5_r',
'open_-6_r',
'open_-7_r',
'open_-8_r',
'open_-9_r',
'open_-10_r',
'open_-11_r',
'open_-12_r',
'open_-13_r',
'open_-14_r',
'open_-15_r',
'open_-16_r',
'open_-17_r',
'open_-18_r',
'open_-19_r',
'open_-20_r',
'open_-21_r',
'open_-22_r',
'open_-23_r',
'open_-24_r',
'open_-25_r',
'open_-26_r',
'open_-27_r',
'open_-28_r',
'open_-29_r',
'open_-30_r',
'close_-1_r',
'close_-2_r',
'close_-3_r',
'close_-4_r',
'close_-5_r',
'close_-6_r',
'close_-7_r',
'close_-8_r',
'close_-9_r',
'close_-10_r',
'close_-11_r',
'close_-12_r',
'close_-13_r',
'close_-14_r',
'close_-15_r',
'close_-16_r',
'close_-17_r',
'close_-18_r',
'close_-19_r',
'close_-20_r',
'close_-21_r',
'close_-22_r',
'close_-23_r',
'close_-24_r',
'close_-25_r',
'close_-26_r',
'close_-27_r',
'close_-28_r',
'close_-29_r',
'close_-30_r',
'open_30_sma', # 30 day simple moving average
'close_30_sma', # 30 day simple moving average
'open_1_r', 'open_1_d'] # percent and absolute change for tomorrow - the truth outcomes
