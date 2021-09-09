import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df_Fallzahlen = pd.read_csv('Fallzahlen_BS.csv', sep=';')
print(df_Fallzahlen)
print(df_Fallzahlen.columns)
print(df_Fallzahlen['Datum'])

dates = df_Fallzahlen['Datum']
x = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]
print(x)


days = mdates.drange(min(x), max(x) + dt.timedelta(days=1), dt.timedelta(days=1))


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=40))
plt.bar(x, df_Fallzahlen['Differenz Fälle mit Wohnsitz BS'])
plt.gcf().autofmt_xdate()

#plt.show()
plt.close()

#Compare with estimates
df_Fallzahlen_reduced = df_Fallzahlen[['Differenz Fälle mit Wohnsitz BS', 'Datum']]
df_estimates = pd.read_csv('verdoppelung.csv')

df_combined = df_estimates.merge(df_Fallzahlen_reduced, how='left', on='Datum')

print(df_combined)
print(df_combined.columns)

dates = df_combined['Datum']
x = [dt.datetime.strptime(d, '%Y-%m-%d') for d in dates]
print(x)


days = mdates.drange(min(x), max(x) + dt.timedelta(days=1), dt.timedelta(days=1))


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=40))
plt.bar(x, df_combined['Differenz Fälle mit Wohnsitz BS'])
plt.gcf().autofmt_xdate()

plt.bar(x, df_combined['Mittlere growth rate'] * 100, color='r')

plt.show()
