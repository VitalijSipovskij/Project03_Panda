# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address.
url1 = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user"

# Step 3. Assign it to a variable called users and use the 'user_id' as index
users = pd.read_csv(url1, delimiter='|').set_index('user_id')
# users.reset_index(inplace=True)  # reset index, it will make user_id as column

# Step 4. See the first 25 entries
print(f"------------Step 4. See the first 25 entries")
print(users.head(25))

# Step 5. See the last 10 entries
print(f"------------Step 5. See the last 10 entries")
print(users.tail(10))

# Step 6. What is the number of observations in the dataset?
print(f"------------Step 6. What is the number of observations in the dataset?")
num_observations = users.shape[0]
print("Number of observations in the dataset:", num_observations)

# Step 7. What is the number of columns in the dataset?
print(f"------------Step 7. What is the number of columns in the dataset?")
num_columns = users.shape[1]
print("Number of columns in the dataset:", num_columns)

# Step 8. Print the name of all the columns.
print(f"------------Step 8. Print the name of all the columns.")
print("Names of all columns:")
print(users.columns)

# Step 9. How is the dataset indexed?
print(f"------------Step 9. How is the dataset indexed?")
print("Index of the dataset:")
print(users.index)

# Step 10. What is the data type of each column?
print(f"------------Step 10. What is the data type of each column?")
print("Data type of each column:")
print(users.dtypes)

# Step 11. Print only the occupation column
print(f"------------Step 11. Print only the occupation column")
print("Occupation column:")
print(users.occupation)

# Step 12. How many different occupations there are in this dataset?
print(f"------------Step 12. How many different occupations there are in this dataset?")
num_occupations = users['occupation'].nunique()  # executed in 0.002 s in colab, faster than len(users['occupation'].value_counts()) executed in 0.335 s in colab
print("Number of different occupations:", num_occupations)

# Step 13. What is the most frequent occupation in this dataset?
print(f"------------Step 13. What is the most frequent occupation in this dataset?")
most_frequent_occupation = users['occupation'].value_counts().idxmax()  # executed in 0.002 in colab, faster most_frequent_occupation = users['occupation'].mode()[0] executed in 0.434 s in colab
print("Most frequent occupation:", most_frequent_occupation)

# Step 14. Summarize the dataframe
print(f"------------Step 14. Summarize the dataframe")
print(users.describe())

# Step 15. Summarize all the columns
print(f"------------Step 15. Summarize all the columns")
print(users.describe(include='all'))

# Step 16. Summarize only the occupation column
print(f"------------Step 16. Summarize only the occupation column")
occupation_summary = users['occupation'].value_counts()
print(occupation_summary)

# Step 17. What is the mean age of users?
print(f"------------Step 17. What is the mean age of users?")
mean_age = users['age'].mean()
print("Mean age of users:", mean_age)

# Step 18. What is the age with the least occurrence?
print(f"------------Step 18. What is the age with the least occurrence?")
age_least_occurrence = users['age'].value_counts().idxmin()
print("Age with least occurrence:", age_least_occurrence)
