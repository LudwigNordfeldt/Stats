import pandas as pd
data = pd.read_csv('diabetes_changed.csv')
print(data.drop_duplicates(subset = ['num_preg','glucose','blood_pressure','triceps','insulin','body_mass_index','diabetes_pedigree_function','age','diabetes','doctor']))
print(data.dropna(thresh=10))

Q1 = data['num_preg'].quantile(0.25)
Q3 = data['num_preg'].quantile(0.75)
IQR = Q3 - Q1
print('Num_preg outliers')
print ( data[((data['num_preg'] < (Q1 - 1.5 * IQR)) | (data['num_preg'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['glucose'].quantile(0.25)
Q3 = data['glucose'].quantile(0.75)
IQR = Q3 - Q1
print('glucose outliers')
print ( data[((data['glucose'] < (Q1 - 1.5 * IQR)) | (data['glucose'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['blood_pressure'].quantile(0.25)
Q3 = data['blood_pressure'].quantile(0.75)
IQR = Q3 - Q1
print('blood_pressure outliers')
print ( data[((data['blood_pressure'] < (Q1 - 1.5 * IQR)) | (data['blood_pressure'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['triceps'].quantile(0.25)
Q3 = data['triceps'].quantile(0.75)
IQR = Q3 - Q1
print('triceps outliers')
print ( data[((data['triceps'] < (Q1 - 1.5 * IQR)) | (data['triceps'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['insulin'].quantile(0.25)
Q3 = data['insulin'].quantile(0.75)
IQR = Q3 - Q1
print('insulin outliers')
print ( data[((data['insulin'] < (Q1 - 1.5 * IQR)) | (data['insulin'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['body_mass_index'].quantile(0.25)
Q3 = data['body_mass_index'].quantile(0.75)
IQR = Q3 - Q1
print('body_mass_index outliers')
print ( data[((data['body_mass_index'] < (Q1 - 1.5 * IQR)) | (data['body_mass_index'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['diabetes_pedigree_function'].quantile(0.25)
Q3 = data['diabetes_pedigree_function'].quantile(0.75)
IQR = Q3 - Q1
print('diabetes_pedigree_function')
print ( data[((data['diabetes_pedigree_function'] < (Q1 - 1.5 * IQR)) | (data['diabetes_pedigree_function'] > (Q3 + 1.5 * IQR)))] )

Q1 = data['age'].quantile(0.25)
Q3 = data['age'].quantile(0.75)
IQR = Q3 - Q1
print('age outliers')
print ( data[((data['age'] < (Q1 - 1.5 * IQR)) | (data['age'] > (Q3 + 1.5 * IQR)))] )




print(data)
