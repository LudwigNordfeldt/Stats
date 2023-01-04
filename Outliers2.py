import pandas as pd
data = pd.read_csv('diabetes_changed.csv')

M = data['num_preg'].mean()
s = data['num_preg'].std()

print('Num_preg outliers using mean and std deviation')
print( data[(data['num_preg'] > (M + 3*s)) | (data['num_preg'] < (M - 3*s))] )

M = data['glucose'].mean()
s = data['glucose'].std()

print('glucose outliers using mean and std deviation')
print( data[(data['glucose'] > (M + 3*s)) | (data['glucose'] < (M - 3*s))] )

M = data['blood_pressure'].mean()
s = data['blood_pressure'].std()

print('blood_pressure outliers using mean and std deviation')
print( data[(data['blood_pressure'] > (M + 3*s)) | (data['blood_pressure'] < (M - 3*s))] )

M = data['triceps'].mean()
s = data['triceps'].std()

print('triceps outliers using mean and std deviation')
print( data[(data['triceps'] > (M + 3*s)) | (data['triceps'] < (M - 3*s))] )

M = data['insulin'].mean()
s = data['insulin'].std()

print('insulin outliers using mean and std deviation')
print( data[(data['insulin'] > (M + 3*s)) | (data['insulin'] < (M - 3*s))] )

M = data['body_mass_index'].mean()
s = data['body_mass_index'].std()

print('body_mass_index outliers using mean and std deviation')
print( data[(data['body_mass_index'] > (M + 3*s)) | (data['body_mass_index'] < (M - 3*s))] )

M = data['diabetes_pedigree_function'].mean()
s = data['diabetes_pedigree_function'].std()

print('diabetes_pedigree_function outliers using mean and std deviation')
print( data[(data['diabetes_pedigree_function'] > (M + 3*s)) | (data['diabetes_pedigree_function'] < (M - 3*s))] )

M = data['age'].mean()
s = data['age'].std()

print('age outliers using mean and std deviation')
print( data[(data['age'] > (M + 3*s)) | (data['age'] < (M - 3*s))] )
