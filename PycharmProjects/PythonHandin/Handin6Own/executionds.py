import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv('executionds.csv', quotechar='"', skipinitialspace=True, delimiter=',',
                           encoding='latin1').fillna(0)

#1

data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].map(lambda x: x.year)
executions_by_year = data.groupby(['Year'])['Name'].count()
ax = executions_by_year.plot.bar(figsize=(8,6), title="Total number of executions in the US since 1976")
label = plt.ylabel("Total amount of executions since 1976")
plt.savefig('Q1.png')
plt.show()
print("Peak execution number in 1999: %d" % executions_by_year.ix[1999])


#2


executions_by_race = data.groupby(['Race'], as_index=False)['Name'].count()
executions_by_race.rename(columns={'Name':'Total Executed'}, inplace=True)
ax = executions_by_race.plot.bar(x='Race', y='Total Executed', title='Number of Executions Since 1976 by race')
label = plt.ylabel("Total number of Executions Since 1976")
plt.savefig('Q2.png')
plt.show()


#3


executions_by_state = data.groupby(['State'])['Name'].count()
ax = executions_by_state.plot.bar(x='State', figsize=(8,6), title="Total number of Executions Since 1976")
txt = plt.ylabel("Total number of Executions Since 1976")
plt.savefig('Q3.png')
plt.show()

