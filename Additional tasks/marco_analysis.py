import pandas as pd
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=1)

df = pd.read_csv('macro.csv', index_col=0)

df.loc['GDP relative increase (annual %)'] = df.loc["GDP (constant 2015 US$)"].diff()/df.loc["GDP (constant 2015 US$)"].shift(1)*100

print(df)
df.loc[["GDP relative increase (annual %)", "Inflation, consumer prices (annual %)"]].transpose().plot(ax=axes[0])

df.loc[["Official exchange rate (LCU per US$, period average)","Unemployment, total (% of total labor force) (national estimate)"]].transpose().plot(ax=axes[1])
plt.legend(fontsize='small')
plt.show()


print(df.transpose()["GDP relative increase (annual %)"].idxmax())
print(df.transpose()["GDP relative increase (annual %)"].idxmin())
