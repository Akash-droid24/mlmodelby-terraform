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
print("\n")
print("\n")
from sklearn.linear_model import LinearRegression
mind = LinearRegression()

# Training the model
mind.fit( x , y)
print("\t\t\t\t\tMODEL TRAINED SUCCESSFULLY")
print("\n")
value_to_predict = eval(input("Enter the value to predict: "))
print("\n")
print("The predicted value of salary is ",mind.predict( [[value_to_predict]] ))
print("\n")

print("Machine Learning model created")
print("\n\n")

print("""
      You want to save the Machine learning model :
           Press Y for yes 
           Press N for no
      """)
print("\n")
print("ENTER YOUR CHOICE: \n")
choice = input()

if "Y" in choice:
  import joblib
  joblib.dump(mind, 'model1.pk1')
  print("Your model has been saved")
  
if "N" in choice:
      print("OK BYE")
  

