import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('vaccination_process_2021_regions.xlsx', 'daily_vaccination process quant')
odessa_months = []
t = data.loc[ data['Назва території'] == 'Одеська область' ]

odessa_months.append (sum(t.iloc[0:24, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[24:54, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[54:85, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[85:116, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[116:146, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[146:177, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[177:207, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[207:238, [1, 2]]['AstraZeneca, осіб']))
odessa_months.append (sum(t.iloc[238:243, [1, 2]]['AstraZeneca, осіб']))


odessa_months_f = reversed(odessa_months)
f = pd.DataFrame(odessa_months_f)
f.index = ['February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October']
print(f)
f.plot(kind = 'bar')
plt.show()
