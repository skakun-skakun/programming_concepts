import numpy as np
import requests
import pandas as pd

# import matplotlib.pyplot as plt
# from pprint import pprint

resp = requests.get('https://api.binance.com/api/v3/klines', params={'symbol': 'BNBUSDT', 'interval': '1w'})

df = pd.DataFrame([map(float, kline[:6]) for kline in resp.json()])
df.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
df['avg'] = (df.open + df.close) / 2
df['SMA'] = df.avg.rolling(window=9).mean()
df['MSMA'] = df.avg.rolling(window=29).mean()
df.SMA = df.SMA.shift(-4)
df.MSMA = df.MSMA.shift(-14)
df['ds'] = (df.SMA - df.MSMA)

hds = 1
open_trades = []
close_trades = []
for row in df.iterrows():
    # print(row[1].ds)

    if not pd.isna(row[1].ds):
        if hds / row[1].ds < 0:
            hds = row[1].ds
            open_trades.append(
                {'open_time': row[1].time, 'stoploss': (row[1].close * 1.1, row[1].close * 0.9)[int(hds > 0)],
                 'open': row[1].close})
        for trade in open_trades:
            if (trade['open'] > trade['stoploss'] and (
                    trade['stoploss'] > row[1].close or row[1].close/trade['open'] > 1.2)) \
                    or (trade['open'] < trade['stoploss'] and (
                    trade['stoploss'] < row[1].close or row[1].close/trade['open'] < 0.8)):
                close_trades.append(trade)
                close_trades[-1]['close_time'] = row[1].time
                close_trades[-1]['close'] = row[1].close
                open_trades.remove(trade)

returns = []

for trade in close_trades:
    print(f'Open: {trade["open"]}; Close: {trade["close"]}; Stop loss: {trade["stoploss"]}; Trade type: {("Short", "Long")[bool(trade["open"] > trade["stoploss"])]}')
    returns.append((trade['stoploss'] - trade['close']) / (trade['stoploss'] - trade['open']) - 1)

print()
print(f"Total returns: {sum(returns)}\nAverage returns: {np.mean(returns)}")

# print(df.head(20))

# plt.figure()


# up = df[df.close >= df.open]
# down = df[df.close < df.open]
# col1 = 'green'
# col2 = 'red'

# width = 1
# width2 = .2

# plt.bar(up.index, up.close-up.open, width, bottom=up.open, color=col1)
# plt.bar(up.index, up.high-up.close, width2, bottom=up.close, color=col1)
# plt.bar(up.index, up.low-up.open, width2, bottom=up.open, color=col1)

# plt.bar(down.index, down.close-down.open, width, bottom=down.open, color=col2)
# plt.bar(down.index, down.high-down.open, width2, bottom=down.open, color=col2)
# plt.bar(down.index, down.low-down.close, width2, bottom=down.close, color=col2)

# plt.xticks(rotation=30, ha='right')

# plt.plot(df.index, df.SMA, color='black')
# plt.plot(df.index, df.MSMA, color='blue')

# plt.show()
