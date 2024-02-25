# Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

# Step 2. Import the dataset from this address.
url3 = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv"

# Step 3. Assign it to a variable called drinks
print(f"------------Step 3. Assign it to a variable called drinks")
drinks = pd.read_csv(url3)
print(drinks)

# Step 4. Which continent drinks more beer on average?
print(f"------------Step 4. Which continent drinks more beer on average?")
continent_beer_avg = drinks.groupby('continent')['beer_servings'].mean()
print(continent_beer_avg)

# Step 5. For each continent print the statistics for wine consumption.
print(f"------------Step 5. For each continent print the statistics for wine consumption.")
wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print(wine_stats)

# Step 6. Print the mean alcohol consumption per continent for every column -------------------------------------------
print(f"------------Step 6. Print the mean alcohol consumption per continent for every column")

# alcohol_mean = drinks.groupby('continent').mean()    # not working, gives tracebacks
# print(alcohol_mean)

numeric_columns = drinks.select_dtypes(include=[np.number])  # to solve problem above was chosen to use numpy
alcohol_mean_per_continent = numeric_columns.groupby(drinks['continent']).mean()
print(alcohol_mean_per_continent)

# Step 7. Print the median alcohol consumption per continent for every column
print(f"------------Step 7. Print the median alcohol consumption per continent for every column")
numeric_columns = drinks.select_dtypes(include=np.number)
alcohol_median_per_continent = numeric_columns.groupby(drinks['continent']).median()
print(alcohol_median_per_continent)

# Step 8. Print the mean, min and max values for spirit consumption.
print(f"------------Step 8. Print the mean, min and max values for spirit consumption.")
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
print(spirit_stats)
