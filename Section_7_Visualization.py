# Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2. Import the dataset from this address
url7 = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv"

# Step 3. Assign it to a variable titanic
print(f"------------Step 3. Assign it to a variable titanic")
titanic = pd.read_csv(url7)
print(titanic)

# Step 4. Set PassengerId as the index
print(f"------------Step 4. Set PassengerId as the index")
titanic.set_index('PassengerId', inplace=True)
print(titanic)

# Step 5. Create a pie chart presenting the male/female proportion
print(f"------------Step 5. Create a pie chart presenting the male/female proportion")
# Calculate the count of males and females
gender_counts = titanic['Sex'].value_counts()
# Plotting the pie chart using pandas plotting functionality
explode = [0, 0.1]
gender_counts.plot(kind='pie', explode=explode, autopct='%1.1f%%', startangle=90, shadow=True, colors=['lightblue', 'lightpink'])
# Adding labels and title
plt.title('Male/Female Proportion on Titanic')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.ylabel('')  # Remove the y-label
plt.show()

# Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
print(f"------------Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender")
# Separate data by gender
male_passengers = titanic[titanic['Sex'] == 'male']
female_passengers = titanic[titanic['Sex'] == 'female']
# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(male_passengers['Age'], male_passengers['Fare'], color='blue', label='Male', alpha=0.7)
plt.scatter(female_passengers['Age'], female_passengers['Fare'], color='red', label='Female', alpha=0.7)
# Adding labels and title
plt.title('Fare Paid vs Age by Gender')
plt.xlabel('Age')
plt.ylabel('Fare Paid')
plt.legend()
plt.grid(True)
plt.show()

# Using Seaborn library
# Combine male and female passengers into one DataFrame
combined_passengers = pd.concat([male_passengers, female_passengers])
# Plotting with seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=combined_passengers, x='Age', y='Fare', hue='Sex', palette={'male': 'blue', 'female': 'red'})
plt.title('Fare Paid vs Age by Gender')
plt.xlabel('Age')
plt.ylabel('Fare Paid')
plt.legend(title='Gender')
plt.grid(True)
plt.show()

# Step 7. How many people survived?
print(f"------------Step 7. How many people survived?")
survived_count = titanic['Survived'].value_counts()[1]
print("Number of people who survived:", survived_count)

# Step 8. Create a histogram with the Fare payed
print(f"------------Step 8. Create a histogram with the Fare payed")
# Plotting
plt.figure(figsize=(10, 6))
plt.hist(titanic['Fare'], bins=60, color='red', edgecolor='black', linewidth=1.2)
# Adding labels and title
plt.title('Histogram of Fare Paid')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# BONUS: Create your own question and answer it.
# Calculate survival rate by passenger class in percentage
print(f"------------Calculate survival rate by passenger class in percentage")
survival_rate_by_class_percent = titanic.groupby('Pclass')['Survived'].mean() * 100
print("Survival Rate by Passenger Class:")
for pclass, survival_rate in survival_rate_by_class_percent.items():
    print(f"Pclass {pclass}: {survival_rate:.2f}%")
