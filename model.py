import pandas
import pyttsx3

# Read the dataset
ds = pandas.read_csv('SalaryData.csv')
pyttsx3.speak("The dataset I have used")
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
pyttsx3.speak("Your Machine Learning model is deployed sir")
print("Machine Learning model created")

