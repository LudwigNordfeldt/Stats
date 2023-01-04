import pandas as pd
data = pd.read_excel('filter3.xlsx', 'filter1')
data['subsidy'] = ( (data['Debts'] == 'no') & (data['AverageIncome'] < 4500) ) * 0.1 * data['Rent']

print(data)
print()

print (data.loc [ data['subsidy'] > 0 ] )
print()
print (data.loc [ (data['AverageIncome'] < 4500) & (data['Debts'] == 'yes') ] )
print()
print (data.loc [ data['Rent'] > 2000 ] )
print()
print (data.loc [ (data['AverageIncome'] > 3000) & (data['AverageIncome'] < 5000 ) ] )
print()
print (data.loc [ (data['subsidy'] > 0) & (data['Rent'] > 1500) ] )
print()
print (data.loc [ ((data['subsidy'] > 0) & (data['Rent'] > 1800)) | ( (data['AverageIncome'] < 5000) & (data['Debts'] == 'yes') ) ] )
print()
print (data.loc [ ((data['AverageIncome'] > 3000) & (data['AverageIncome'] < 5000) & (data['Rent'] > 1800)) | ( (data['Rent'] <= 1600) & (data['Debts'] == 'yes') ) ] )
