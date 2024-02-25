# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address.
url4 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"

# Step 3. Assign it to a variable called crime.
print(f"------------Step 3. Assign it to a variable called crime.")
crime = pd.read_csv(url4)
print(crime)

# Step 4. What is the type of the columns?
print(f"------------Step 4. What is the type of the columns?")
print(crime.dtypes)

# Step 5. Convert the type of the column Year to datetime64
print(f"------------Step 5. Convert the type of the column Year to datetime64")
# Convert the type of the column 'Year' to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
# Confirm the conversion
print("Type of the 'Year' column after conversion:", crime['Year'].dtype)
# Check the conversion
print(crime.dtypes)

# Step 6. Set the Year column as the index of the dataframe
print(f"------------Step 6. Set the Year column as the index of the dataframe")
crime.set_index('Year', inplace=True)
print(crime.head())

# Step 7. Delete the Total column
print(f"------------Step 7. Delete the Total column")
crime.drop('Total', axis=1, inplace=True)
print(crime.head())

# Step 8. Group the year by decades and sum the values
print(f"------------Step 8. Group the year by decades and sum the values")
# Resample the DataFrame to group years by decades and sum the values
crime_decades = crime.resample('10YS').sum()
# Drop the 'Population' column
crime_decades = crime_decades.drop(columns=['Population'])
print(crime_decades)

# Step 9. What is the most dangerous decade to live in the US?
print(f"------------Step 9. What is the most dangerous decade to live in the US?")
crime_decades['Total_Crime'] = crime_decades.sum(axis=1)
most_dangerous_decade = crime_decades['Total_Crime'].idxmax()
print("The most dangerous decade to live in the US was:", most_dangerous_decade)
