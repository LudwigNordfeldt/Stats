import pandas as pd
data = pd.read_csv('diabetes_changed.csv')


Q1 = data['num_preg'].quantile(0.25)
Q3 = data['num_preg'].quantile(0.75)
IQR = Q3 - Q1
M = data['num_preg'].mean()
s = data['num_preg'].std()

print('Num_preg outliers')
print (data[((data['num_preg'] < (Q1 - 1.5 * IQR)) | (data['num_preg'] > (Q3 + 1.5 * IQR)))
        & (data['num_preg'] > (M + 3*s)) | (data['num_preg'] < (M - 3*s))
             ])


data[((data['num_preg'] < (Q1 - 1.5 * IQR)) | (data['num_preg'] > (Q3 + 1.5 * IQR)))
        & (data['num_preg'] > (M + 3*s)) | (data['num_preg'] < (M - 3*s))
             ] = M
print(data[85:90])

Q1 = data['glucose'].quantile(0.25)
Q3 = data['glucose'].quantile(0.75)
IQR = Q3 - Q1
M = data['glucose'].mean()
s = data['glucose'].std()

print('glucose outliers')
print (data[((data['glucose'] < (Q1 - 1.5 * IQR)) | (data['glucose'] > (Q3 + 1.5 * IQR)))
        & (data['glucose'] > (M + 3*s)) | (data['glucose'] < (M - 3*s))
             ])


data[((data['glucose'] < (Q1 - 1.5 * IQR)) | (data['glucose'] > (Q3 + 1.5 * IQR)))
        & (data['glucose'] > (M + 3*s)) | (data['glucose'] < (M - 3*s))
             ] = M

Q1 = data['blood_pressure'].quantile(0.25)
Q3 = data['blood_pressure'].quantile(0.75)
IQR = Q3 - Q1
M = data['blood_pressure'].mean()
s = data['blood_pressure'].std()

print('blood_pressure outliers')
print (data[((data['blood_pressure'] < (Q1 - 1.5 * IQR)) | (data['blood_pressure'] > (Q3 + 1.5 * IQR)))
        & (data['blood_pressure'] > (M + 3*s)) | (data['blood_pressure'] < (M - 3*s))
             ])


data[((data['blood_pressure'] < (Q1 - 1.5 * IQR)) | (data['blood_pressure'] > (Q3 + 1.5 * IQR)))
        & (data['blood_pressure'] > (M + 3*s)) | (data['blood_pressure'] < (M - 3*s))
             ] = M

Q1 = data['triceps'].quantile(0.25)
Q3 = data['triceps'].quantile(0.75)
IQR = Q3 - Q1
M = data['triceps'].mean()
s = data['triceps'].std()

print('triceps outliers')
print (data[((data['triceps'] < (Q1 - 1.5 * IQR)) | (data['triceps'] > (Q3 + 1.5 * IQR)))
        & (data['triceps'] > (M + 3*s)) | (data['triceps'] < (M - 3*s))
             ])


data[((data['triceps'] < (Q1 - 1.5 * IQR)) | (data['triceps'] > (Q3 + 1.5 * IQR)))
        & (data['triceps'] > (M + 3*s)) | (data['triceps'] < (M - 3*s))
             ] = M

Q1 = data['insulin'].quantile(0.25)
Q3 = data['insulin'].quantile(0.75)
IQR = Q3 - Q1
M = data['insulin'].mean()
s = data['insulin'].std()

print('insulin')
print (data[((data['insulin'] < (Q1 - 1.5 * IQR)) | (data['insulin'] > (Q3 + 1.5 * IQR)))
        & (data['insulin'] > (M + 3*s)) | (data['insulin'] < (M - 3*s))
             ])


data[((data['insulin'] < (Q1 - 1.5 * IQR)) | (data['insulin'] > (Q3 + 1.5 * IQR)))
        & (data['insulin'] > (M + 3*s)) | (data['insulin'] < (M - 3*s))
             ] = M

Q1 = data['body_mass_index'].quantile(0.25)
Q3 = data['body_mass_index'].quantile(0.75)
IQR = Q3 - Q1
M = data['body_mass_index'].mean()
s = data['body_mass_index'].std()

print('body_mass_index outliers')
print (data[((data['body_mass_index'] < (Q1 - 1.5 * IQR)) | (data['body_mass_index'] > (Q3 + 1.5 * IQR)))
        & (data['body_mass_index'] > (M + 3*s)) | (data['body_mass_index'] < (M - 3*s))
             ])


data[((data['body_mass_index'] < (Q1 - 1.5 * IQR)) | (data['body_mass_index'] > (Q3 + 1.5 * IQR)))
        & (data['body_mass_index'] > (M + 3*s)) | (data['body_mass_index'] < (M - 3*s))
             ] = M

Q1 = data['diabetes_pedigree_function'].quantile(0.25)
Q3 = data['diabetes_pedigree_function'].quantile(0.75)
IQR = Q3 - Q1
M = data['diabetes_pedigree_function'].mean()
s = data['diabetes_pedigree_function'].std()

print('diabetes_pedigree_function outliers')
print (data[((data['diabetes_pedigree_function'] < (Q1 - 1.5 * IQR)) | (data['diabetes_pedigree_function'] > (Q3 + 1.5 * IQR)))
        & (data['diabetes_pedigree_function'] > (M + 3*s)) | (data['diabetes_pedigree_function'] < (M - 3*s))
             ])


data[((data['diabetes_pedigree_function'] < (Q1 - 1.5 * IQR)) | (data['diabetes_pedigree_function'] > (Q3 + 1.5 * IQR)))
        & (data['diabetes_pedigree_function'] > (M + 3*s)) | (data['diabetes_pedigree_function'] < (M - 3*s))
             ] = M

Q1 = data['age'].quantile(0.25)
Q3 = data['age'].quantile(0.75)
IQR = Q3 - Q1
M = data['age'].mean()
s = data['age'].std()

print('age outliers')
print (data[((data['age'] < (Q1 - 1.5 * IQR)) | (data['age'] > (Q3 + 1.5 * IQR)))
        & (data['age'] > (M + 3*s)) | (data['age'] < (M - 3*s))
             ])


data[((data['age'] < (Q1 - 1.5 * IQR)) | (data['age'] > (Q3 + 1.5 * IQR)))
        & (data['age'] > (M + 3*s)) | (data['age'] < (M - 3*s))
             ] = M
