import pandas as pd
data=pd.read_excel("Epidural.xlsx")
print(data)

#See column names
print(data.columns)

#Summary statistics
print(data[["edad"]].describe())

#Filter
epidural_si=data.loc[data["EPIDURAL"]==1]
print(epidural_si)

#Clasify by "edad"
data["edad_recodificada"] = pd.cut(data['edad'], bins=[-float('inf'), 24, 25, float('inf')],
labels=['por debajo', 'por igual', 'por encima'])
print(data)

#FREQ TABLE
frequency_table = data["edad_recodificada"].value_counts()
print(frequency_table)

#New variable: mean
mean = data[["TEMP1","TEMP2"]].mean(axis=1)
data["MEAN_TEMP"] = mean
print(data)

#Scatter plot 1
import matplotlib.pyplot as plt 
import numpy as np
x=data["edad"]
y=data["TEMP2"]
m,b=np.polyfit(x,y,1)
print(m)
print(b)

plt.scatter(x,y,color="b")
plt.plot(x,m*x+b,color="r",label="Linear regression")
plt.xlabel("Age (years)")
plt.ylabel("Temperature after childbirth (ºC)")
plt.title("Scatter plot Age - Temperature")
plt.legend()
plt.show()    #No correlation

#Scatter plot 2
x=data["DILATACI"]
y=data["TEMP2"]
m,b=np.polyfit(x,y,1)
plt.scatter(x,y,color="b")
plt.plot(x,m*x+b,color="r",label="Linear regression")
plt.xlabel("Dilatation (cm)")
plt.ylabel("Temperature after childbirth (ºC)")
plt.title("Scatter plot")
plt.legend()
plt.show() #Weak correlation

#Scatter plot 3
x=data["EXPULSIV"]
y=data["TEMP2"]
m,b=np.polyfit(x,y,1)
plt.scatter(x,y,color="b")
plt.plot(x,m*x+b,color="r",label="Linear regression")
plt.xlabel("Expulsiv")
plt.ylabel("Temperature after childbirth (ºC)")
plt.title("Scatter plot")
plt.legend()
plt.show() #Weak correlation

#Calculate the correlation coefficients between the variables. 
# The coefficient r of Pearson, which varies between -1 and 1. The greater its absolute value, the greater the intensity
#of the relationship.
variables=["TEMP2","edad","DILATACI","EXPULSIV"]
data2=data[variables]
corr_matrix=data2.corr()
print(corr_matrix)

#LINEAL MODEL: TEMP2 and DILATACI
x=data["DILATACI"]
y=data["TEMP2"]
corr_coef=np.corrcoef(x,y)[0][1] # r
beta1=corr_coef*(y.std()/x.std())   # m
beta0=y.mean()-beta1*x.mean()  #n
print("n= ",beta0," and m= ",beta1)

