import pandas as pd
births = pd.read_csv(r"C:\Users\pc\Desktop\DS projects\birth rate analysis\births.csv") 
print(births.head()) 
births['day'].fillna(0, inplace=True) 
births['day'] = births['day'].astype(int)
births['decade'] = 10 * (births['year'] // 10)
birth=births.pivot_table('births', index='decade', columns='gender', aggfunc='sum')
print(birth)
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set()  
birth.plot() 
plt.ylabel("Total births per year") 
plt.show()
#cleaning data to further do more analysis 
import numpy as np
quartiles = np.percentile(births['births'], [25, 50, 75])
print(quartiles)
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])
births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')
births['day'] = births['day'].astype(int)
births.index = pd.to_datetime(10000 * births.year +
                              100 * births.month +
                              births.day, format='%Y%m%d')

births['dayofweek'] = births.index.dayofweek
births.pivot_table('births', index='dayofweek',
                    columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day')
plt.show()
births_month = births.pivot_table('births', [births.index.month, births.index.day])
print(births_month.head())
births_month.index = pd.to_datetime([
    f'2012-{month:02d}-{day:02d}'  # format month/day with leading zeros
    for (month, day) in births_month.index
])
print(births_month.head())
fig, ax = plt.subplots(figsize=(12, 4))
births_month.plot(ax=ax)
plt.show()
