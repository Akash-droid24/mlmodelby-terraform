import pandas


# Read the dataset
ds = pandas.read_csv('SalaryData.csv')

print("Here's the dataset I used\n",ds)
print("\n")
x = ds['YearsExperience']
y = ds['Salary']
x = x.values
x = x.reshape(30,1)

print("                THE MODEL IS BEING TRAINED          ")
from sklearn.linear_model import LinearRegression
mind = LinearRegression()

# Training the model
mind.fit( x , y)
print("******MODEL TRAINED SUCCESSFULLY")
print("\n")
value_to_predict = eval(input("Enter the value to predict: "))

print(mind.predict( [[value_to_predict]] ))
print("\n")

print("Machine Learning model created")

