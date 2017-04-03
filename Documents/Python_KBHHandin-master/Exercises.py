import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
from operator import itemgetter
from collections import defaultdict
df = pd.read_csv('befkbh.csv',quotechar='"',skipinitialspace=True, delimiter=',', encoding='latin1').fillna(0)
data = df.as_matrix()
#Q1
m18 = collections.defaultdict(list)
f18 = collections.defaultdict(list)
m50 = collections.defaultdict(list)
f50 = collections.defaultdict(list)

for row in data:
	key = row[0]
	if key == "" or key == 0: continue
	#Male 18-30
	if row[4] == 1:
		if row[2] >= 18 and row[2] <= 30:
			val = 0 if(row[5]) ==""  else float(row[5])
			m18.setdefault(key,[]).append(val)
	#Male 50+
		if row[2] >= 50:
			val = 0 if(row[5]) ==""  else float(row[5])
			m50.setdefault(key,[]).append(val)
	#Female 18-30
	if row[4] == 2:
		if row[2] >= 18 and row[2] <= 30:
			val = 0 if(row[5]) ==""  else float(row[5])
			f18.setdefault(key,[]).append(val)
	#Female 50+
		if row[2] >= 50:
			val = 0 if(row[5]) ==""  else float(row[5])
			f50.setdefault(key,[]).append(val)	

m18_2 = {}
for k, v in m18.items(): m18_2[k] = sum(v)
f18_2 = {}
for k, v in f18.items(): f18_2[k] = sum(v)
m50_2 = {}
for k, v in m50.items(): m50_2[k] = sum(v)
f50_2 = {}
for k, v in f50.items(): f50_2[k] = sum(v)

# Ploting
fig, ax1 = plt.subplots()
ax1.plot(*zip(*sorted(m18_2.items())), label='Male 18-30')
ax1.plot(*zip(*sorted(f18_2.items())), label='Female 18-30')
ax1.plot(*zip(*sorted(m50_2.items())), label='Male 50+')
ax1.plot(*zip(*sorted(f50_2.items())), label='Female 50+')
ax1.legend(loc='upper center', shadow=True)
plt.savefig('Question1.png', bbox_inches='tight')
# plt.show()

#Q2

Q2_m18_1 = collections.defaultdict(list)
Q2_f18_1 = collections.defaultdict(list)
for row in data:
	key = row[0]
	if key == "" or key == 0: continue
	#Male 18-30 Singles in different BYDEL
	if row[4] == 1 and row[2] >= 18 and row[2] <= 30 and row[3] != 'G' and row[3] != 'P':
		if row[1] == 1 or row[1] == 2 or row[1] == 3:
			val = 0 if(row[5]) ==""  else float(row[5])
			Q2_m18_1.setdefault(key,[]).append(val)
	#Female 18-30 singles in different BYDEL
	if row[4] == 2 and row[2] >= 18 and row[2] <= 30 and row[3] != 'G' and row[3] != 'P':
		if row[1] == 1 or row[1] == 2 or row[1] == 3:
			val = 0 if(row[5]) ==""  else float(row[5])
			Q2_f18_1.setdefault(key,[]).append(val)

			
Q2_m18_12 = {}
for k, v in Q2_m18_1.items(): Q2_m18_12[k] = sum(v)
Q2_f18_12 = {}
for k, v in Q2_f18_1.items(): Q2_f18_12[k] = sum(v)
#Plotting
fig, ax2 = plt.subplots()
y_pos = np.arange(len(Q2_m18_12))
ax2.bar(y_pos, Q2_m18_12.values(), color = '#8080ff', label='Male 18-30')
ax2.bar(y_pos, Q2_f18_12.values(), color = 'r', bottom = Q2_m18_12.values(), label='Female 18-30')
ax2.legend(loc='upper center', shadow=True)
for a,b,c in zip(y_pos, Q2_m18_12.values(), Q2_f18_12.values()):
	plt.text(a-0.25, 10000, str("%.0f" % (b / ((b+c) / 100))) + '%', rotation=90, color = 'black')
	plt.text(a-0.25, 40000, str("%.0f" % (c / ((b+c) / 100))) + '%', rotation=90)
ax2.set_xticks(y_pos)
ax2.set_xticklabels(Q2_m18_12.keys(), rotation=90)
ax2.set_title('How many single males and females of age 18 to 30?')
plt.savefig('Question2.png', bbox_inches='tight')


#Q3
print("Question 3-----------------------")
df3 = df.groupby(["AAR", "BYDEL"], as_index=False)["PERSONER"].sum()
print(df3[df3.AAR == 1992].nlargest(3, "PERSONER"))
print(df3[df3.AAR == 2000].nlargest(3, "PERSONER"))
print(df3[df3.AAR == 2015].nlargest(3, "PERSONER"))

#Q4
print("Question 4-----------------------")
#BYDEL 1,2,3 for year 2000
df4 = df.groupby(["AAR", "BYDEL", "CIVST"], as_index=False)["PERSONER"].sum()
df4 = df4[(df4.BYDEL < 4)& (df4.AAR == 2000)] 
#Deleting columns. Pass the axis=1 option for it to work on columns and not rows. 
df4 = df4.drop(['BYDEL','AAR'], axis=1)
df4 = df4.groupby('CIVST').sum()
#Removing the 3 minor values that contains around 1k value total (less than 1%)
df4 = df4.nlargest(4, 'PERSONER')
print('Year 2000')
print(df4)

#BYDEL 1,2,3 for year 2015
df5 = df.groupby(["AAR", "BYDEL", "CIVST"], as_index=False)["PERSONER"].sum()
df5 = df5[(df5.BYDEL < 4) & (df5.AAR == 2015)]
#Deleting columns. Pass the axis=1 option for it to work on columns and not rows. 
df5 = df5.drop(['BYDEL','AAR'], axis=1)
df5 = df5.groupby('CIVST').sum()
#Removing the 3 minor values that contains around 1k value total (less than 1%)
df5 = df5.nlargest(4, 'PERSONER')
print('Year 2015')

print(df5)

#Make auto % and values
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct
explode = (0,0,0,0.1)
my_labels = ['Unmarried','Maried','Divorced','Widdow']
# Pieplot 2000 
df4.plot(kind='pie', y='PERSONER', autopct=make_autopct(df4.PERSONER), startangle=45, shadow=False, labels=my_labels, legend = True, fontsize=14, title='2000', figsize=(8,8),explode = explode)
plt.savefig('Question4_1.png', bbox_inches='tight')
# Pieplot 2015

df5.plot(kind='pie', y='PERSONER', autopct=make_autopct(df5.PERSONER), startangle=45, shadow=False, labels=my_labels , legend = True, fontsize=14, title='2015', figsize=(8,8),explode = explode)
plt.savefig('Question4_2.png', bbox_inches='tight')


#Q5
#mit forsøg
def plot_5(age_distK, age_distV):
	plt.bar(age_distK, age_distV, width=0.5, linewidth=0, align='center')
	plt.ticklabel_format(useOffset=False)
	plt.axis([0, max(age_distK) + 10, 0, 2600])
	title = 'Distribution of {} peoples age in CPH municipality'.format(sum(age_distV))
	plt.title(title, fontsize=12)
	plt.xlabel("Ages", fontsize=10)
	plt.ylabel("Amount of people", fontsize=10)
	plt.tick_params(axis='both', which='major', labelsize=15)
	plt.savefig('LUDERTEST.png', bbox_inches='tight')
	plt.show()

def ex5(df):
	age_distribution = defaultdict(lambda: 0)

	for row in df.itertuples():
		if row[2]:
			age_distribution[row[3]] += 1

	plot_5(list(age_distribution.keys()), list(age_distribution.values()))



print("Question 5-----------------------")
df6 = df.groupby(["AAR", "ALDER", "CIVST"], as_index=False)["PERSONER"].sum()

# E=Widdow, F=Divorced, G=Maried, U=Unmarried








