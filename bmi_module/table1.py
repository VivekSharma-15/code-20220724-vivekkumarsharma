import pandas as pd

#Creating a data table using pandas
data = {'BMI Category': ['Underweight', 'Normal weight', 'Overweight', 'Moderately obese', 'Severely obese', 'Very severely obese'],
        'BMI Range (kg/m2)': ['18.4 and below', '18.5 - 24.9', '25 - 29.9', '30 - 34.9', '35 - 39.9', '40 and above'],
        'Health risk': ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']
         }

df = pd.DataFrame(data)