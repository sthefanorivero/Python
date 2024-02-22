life_expectancy=float(input("Insert life expectancy: "))
income_index=float(input("Insert Gross National Income per capita: "))
education_index=float(input("Insert Education index: "))
idh=(life_expectancy*income_index*education_index)**(1/3)
print("IDH is: ",idh)
if idh >=0.8:
    print("IDH is high.")
elif idh>0.8 and idh >=0.5:
    print("IDH is medium.")
else:
    print("IDH is low.")