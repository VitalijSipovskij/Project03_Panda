# Step 1. Import the necessary libraries
import pandas as pd

url6 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"

pd.set_option('display.max_columns', None)
# # Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.
print(f"------------Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.")
# Read the data
data = pd.read_csv(url6, sep=r'\s+')
# Combine 'Yr', 'Mo', and 'Dy' columns into a single datetime column named 'date'
data['date'] = pd.to_datetime(data[['Yr', 'Mo', 'Dy']].astype(str).agg('-'.join, axis=1), format='%y-%m-%d')
# Drop the original 'Yr', 'Mo', and 'Dy' columns
data.drop(columns=['Yr', 'Mo', 'Dy'], inplace=True)
print(data)
print(data.dtypes)

# Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.
print(f"------------Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.")


print("IGNORE THIS STEP")
# def fix_year_2061(df):
#     df['date'] = pd.to_datetime(df['date'])
#     mask = df['date'].dt.year == 2061
#     if mask.any():
#         df.loc[mask, 'date'] = pd.NaT
#     return df


# fixed_data = fix_year_2061(data)
# fixed_data = fixed_data[~pd.isna(fixed_data['date'])]
# print("Data without 2061 entries:\n", fixed_data)

# Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].
print(f"------------Step 5. Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns].")
data = data.copy()
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)
print(data)
print(data.dtypes)

# fixed_data = fixed_data.copy()
# fixed_data['date'] = pd.to_datetime(fixed_data['date'])
# fixed_data.set_index('date', inplace=True)
# print(fixed_data)
# print(fixed_data.dtypes)


# Step 6. Compute how many values are missing for each location over the entire record.
print(f"------------Step 6. Compute how many values are missing for each location over the entire record.")
print(data.isnull().sum())
# print(fixed_data.isnull().sum())

# Step 7. Compute how many non-missing values there are in total.
print(f"------------Step 7. Compute how many non-missing values there are in total.")
print(data.notnull().sum())
# print(fixed_data.notnull().sum())

# Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.
print(f"------------Step 8. Calculate the mean windspeeds of the windspeeds over all the locations and all the times.")
print(data.mean())
mean_windspeed = data.mean().mean()

# print(fixed_data.mean())
# mean_windspeed = fixed_data.mean().mean()
print("Mean windspeed over all locations and times:", mean_windspeed)

# Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
print(f"------------Step 9. Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days")
loc_stats = data.describe().loc[['min', 'max', 'mean', 'std']]
# loc_stats = fixed_data.describe().loc[['min', 'max', 'mean', 'std']]
print("Summary statistics for each location:")
print(loc_stats)

# Step 10. Create a DataFrame called day_stats and calculate the min, max, mean, and standard deviations of the windspeeds across all locations at each day.
print(f"------------Step 10. Create a DataFrame called day_stats and calculate the min, max, mean, and standard deviations of the windspeeds across all locations at each day.")
day_stats = data.T.describe().loc[['min', 'max', 'mean', 'std']].T
# day_stats = fixed_data.T.describe().loc[['min', 'max', 'mean', 'std']].T
print("Summary statistics for each day:")
print(day_stats)

# Step 11. Find the average windspeed in January for each location.
print(f"------------Step 11. Find the average windspeed in January for each location.")
january_data = data[data.index.month == 1]
# january_data = fixed_data[fixed_data.index.month == 1]
average_windspeed_january = january_data.mean()
print("Average windspeed in January for each location:")
print(average_windspeed_january)

# Step 12. Downsample the record to a yearly frequency for each location.
print(f"------------Step 12. Downsample the record to a yearly frequency for each location.")
yearly_data = data.resample('YE').mean()
# yearly_data = fixed_data.resample('YE').mean()
print(yearly_data)

# Step 13. Downsample the record to a monthly frequency for each location.
print(f"------------Step 13. Downsample the record to a monthly frequency for each location.")
monthly_data = data.resample('ME').mean()
# monthly_data = fixed_data.resample('ME').mean()
print(monthly_data)

# Step 14. Downsample the record to a weekly frequency for each location.
print(f"------------Step 14. Downsample the record to a weekly frequency for each location.")
weekly_data = data.resample('W').mean()
# weekly_data = fixed_data.resample('W').mean()
print(weekly_data)

# Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2, 1961) for the first 52 weeks.
print(f"------------Step 15. Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2, 1961) for the first 52 weeks.")
# Correcting the start date to the first available date in the index
start_date = data.index[0]
# start_date = fixed_data.index[0]

# Calculating the end date for the first 52 weeks
end_date = pd.to_datetime(start_date) + pd.DateOffset(weeks=52)
# Slicing the DataFrame and resampling to weekly frequency
weekly_data_first_52_weeks = data[start_date:end_date].resample('W').agg(['min', 'max', 'mean', 'std'])
# weekly_data_first_52_weeks = fixed_data[start_date:end_date].resample('W').agg(['min', 'max', 'mean', 'std'])

# Printing the summary statistics for the first 52 weeks
print("Summary statistics for the first 52 weeks:", weekly_data_first_52_weeks)
