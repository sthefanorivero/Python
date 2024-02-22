#Suppose a college professor takes a sample of student grades from a class to analyze. Data is a python list.
dt = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63]
print("El conjunto de datos a analizar es el siguiente: \n",dt)

#Run the following cell to load the data into a NumPy array.
import numpy as np
grades = np.array(dt)
print(grades) #se ha convertido en un array de numpy
print(grades.shape) #(21,) significa un array de 1 dimensión y 21 elementos
#Get the first element:
print(grades[0])
#Calculate mean grade value
print(grades.mean())

# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5]
# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])
# display the array
print(student_data)
print(student_data.shape) #(2,21) 2 arrays de 21 elementos
# Show the first element of the first element
print(student_data[0][0])
# Get the mean value of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()
print(f'Average study hours: {avg_study}\nAverage grade: {avg_grade}')

#Llamamos a pandas y hacemos un triple array
import pandas as pd
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny','Jakeem','Helena','Ismat','Anila','Daniel','Sthefano'],'StudyHours':student_data[0],'Grade':student_data[1]})
print(df_students)

# Get the data for index value 5
print(df_students.loc[5])
# Get the rows with index values from 0 to 5
print(df_students.loc[0:5]) #devuelve 6 líneas, de la 0 a la 5
print(df_students.iloc[0:5]) #devuelve 5 líneas, de la 0 a la 4
print(df_students.iloc[0,[1,2]]) #fila 0, columnas 1 y 2

#loc utiliza número para las filas y nombres para las columnas
print(df_students.loc[0,'Grade']) #devuelve el valor 50.0

#Otras 3 opciones para loc:
print("Datos encontrados:\n",df_students[df_students['Name']=='Sthefano'])
print(df_students.query('Name=="Sthefano"'))
print(df_students[df_students.Name == 'Sthefano'])

#LOADING A DATAFRAME FROM FILE



