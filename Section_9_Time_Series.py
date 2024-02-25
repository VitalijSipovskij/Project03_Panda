# Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2. Import the dataset from this address
url9 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv"

# Step 3. Assign it to a variable called apple
print(f"------------Step 3. Assign it to a variable called apple")
apple = pd.read_csv(url9)
print(apple)

# Step 4. Check out the type of the columns
print(f"------------Step 4. Check out the type of the columns")
print(apple.dtypes)

# Step 5. Transform the Date column as a datetime type
print(f"------------Step 5. Transform the Date column as a datetime type")
apple['Date'] = pd.to_datetime(apple['Date'])
print(apple.dtypes)

# Step 6. Set the date as the index
print(f"------------Step 6. Set the date as the index")
apple = apple.set_index('Date')
print(apple)

# Step 7. Is there any duplicate dates?
print(f"------------Step 7. Is there any duplicate dates?")
print(apple.index.is_unique)

# Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
print(f"------------Step 8. Ops...it seems the index is from the most recent date. Make the first entry the oldest date.")
apple = apple.sort_index()
print(apple)

# Step 9. Get the last business day of each month
print(f"------------Step 9. Get the last business day of each month")
last_business_days = apple.resample('BME').last()  # there is problem with running
# same code on colab and pycharm. Problem is in apple.resample('BME') in "BME" it
# just needs to be changed to something else that this platform supports and it will work
print(last_business_days)

# Step 10. What is the difference in days between the first day and the oldest
print(f"------------Step 10. What is the difference in days between the first day and the oldest")
print(apple.index.max() - apple.index.min())
# or
# print((apple.index.max() - apple.index.min()).days)

# Step 11. How many months in the data we have?
print(f"------------Step 11. How many months in the data we have?")
months_in_data = apple.resample('ME').size() # same thing problem with running
# same code on colab and pycharm. changed to something else that this platform
# supports and it will work
print(len(months_in_data))

# Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
print(f"------------Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches")
plt.figure(figsize=(13.5, 9))
plt.plot(apple.index, apple['Adj Close'])
plt.title('Apple Stock Adj Close Value')
plt.xlabel('Date')
plt.ylabel('Adj Close')
plt.grid(True)
plt.show()
