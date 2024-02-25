# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address.
url2 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"

# Step 3. Assign it to a variable called euro12.
print(f"------------Step 3. Assign it to a variable called euro12.")
euro12 = pd.read_csv(url2)
print(euro12)

# Step 4. Select only the Goal column.
print(f"------------Step 4. Select only the Goal column.")
goal_column = euro12[['Goals']]
print(goal_column)

# Step 5. How many team participated in the Euro2012?
print(f"------------Step 5. How many team participated in the Euro2012?")
num_teams = euro12.shape[0]
print("Number of teams participated in the Euro2012:", num_teams)

# Step 6. What is the number of columns in the dataset?
print(f"------------Step 6. What is the number of columns in the dataset?")
num_columns = euro12.shape[1]
print("Number of columns in the dataset:", num_columns)

# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a variable called discipline.
print(f"------------Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a variable called discipline.")
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# Step 8. Sort the teams by Red Cards, then to Yellow Cards
print(f"------------Step 8. Sort the teams by Red Cards, then to Yellow Cards")
sorted_teams = euro12.sort_values(by=['Red Cards', 'Yellow Cards'])
print(sorted_teams)

# Step 9. Calculate the mean Yellow Cards given per Team
print(f"------------Step 9. Calculate the mean Yellow Cards given per Team")
mean_yellow_cards_per_team = euro12['Yellow Cards'].mean()
print("Mean Yellow Cards given per Team:", mean_yellow_cards_per_team)

# Step 10. Filter teams that scored more than 6 goals
print(f"------------Step 10. Filter teams that scored more than 6 goals")
teams_more_than_6_goals = euro12[euro12['Goals'] > 6]
print(teams_more_than_6_goals)

# Step 11. Select the teams that start with G
print(f"------------Step 11. Select the teams that start with G")
teams_starting_with_g = euro12[euro12['Team'].str.startswith('G')]
print(teams_starting_with_g)

# Step 12. Select the first 7 columns
print(f"------------Step 12. Select the first 7 columns")
first_7_columns = euro12.iloc[:, :7]
print(first_7_columns)

# Step 13. Select all columns except the last 3
print(f"------------Step 13. Select all columns except the last 3")
all_columns_except_last_3 = euro12.iloc[:, :-3]
print(all_columns_except_last_3)

# Step 14. Present only the Shooting Accuracy from England, Italy and Russia
print(f"------------Step 14. Present only the Shooting Accuracy from England, Italy and Russia")
shooting_accuracy = euro12.loc[euro12['Team'].isin(['England', 'Italy', 'Russia']), ['Team', 'Shooting Accuracy']]
print(shooting_accuracy)
