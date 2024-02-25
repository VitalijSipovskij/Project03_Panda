# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

# Step 2. Import the dataset from this address.
url10 = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"

# Step 3. Assign it to a variable called wine
print("------------Step 3. Assign it to a variable called wine")
wine = pd.read_csv(url10, header=None)
print(wine)

# Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
print("------------Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns")
wine.drop(wine.columns[[0, 3, 6, 8, 10, 12, 13]], axis=1, inplace=True)
print(wine)

# Step 5. Assign the columns as below:
# The attributes are (donated by Riccardo Leardi, riclea '@' anchem.unige.it):
# 1) alcohol
# 2) malic_acid
# 3) alcalinity_of_ash
# 4) magnesium
# 5) flavanoids
# 6) proanthocyanins
# 7) hue
print("------------Step 5. Assign the columns as below:")
wine.columns = ["alcohol", "malic_acid", "alcalinity_of_ash", "magnesium", "flavanoids", "proanthocyanins", "hue"]
print(wine)

# Step 6. Set the values of the first 3 rows from alcohol as NaN
print("------------Step 6. Set the values of the first 3 rows from alcohol as NaN")
wine.iloc[:3, 0] = None
print(wine)

# Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN
print("------------Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN")
wine.iloc[2:4, 3] = None
print(wine)

# Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
print("------------Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium")
wine.fillna({'alcohol': 10, 'magnesium': 100}, inplace=True)
print(wine)

# Step 9. Count the number of missing values
print("------------Step 9. Count the number of missing values")
missing_values_count = wine.isnull().sum()
print("Number of missing values:")
print(missing_values_count)
# or
missing_values_count1 = wine.isnull().sum().sum()
print("Number of missing values:", missing_values_count1)

# Step 10. Create an array of 10 random numbers up until 10
print("------------Step 10. Create an array of 10 random numbers up until 10")
random_array = np.random.randint(0, 10, size=10)
print("Array of 10 random numbers up until 10:", random_array)

# Step 11. Use random numbers you generated as an index and assign NaN value to each of cell.
print("------------Step 11. Use random numbers you generated as an index and assign NaN value to each of cell.")
wine.iloc[random_array] = None
print(wine)

# Step 12. How many missing values do we have?
print("------------Step 12. How many missing values do we have?")
missing_values = wine.isnull().sum().sum()
print("Total number of missing values:", missing_values)

# Step 13. Delete the rows that contain missing values
print("------------Step 13. Delete the rows that contain missing values")
wine.dropna(inplace=True)
print(wine)

# Step 14. Print only the non-null values in alcohol
print("------------Step 14. Print only the non-null values in alcohol")
# print(wine.alcohol.notnull())

# Step 14. Print only the non-null values in alcohol
non_null_alcohol_values = wine[wine['alcohol'].notnull()]['alcohol']
print("Non-null values in the 'alcohol' column:", non_null_alcohol_values)

# Step 15. Reset the index, so it starts with 0 again
print("------------Step 15. Reset the index, so it starts with 0 again")
wine.reset_index(drop=True, inplace=True)
print(wine)
