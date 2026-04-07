import pandas as pd

# Load dataset
df = pd.read_csv("Public transport Analysis.csv")

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Handle missing values
df['Ticket_Type'].fillna("Unknown", inplace=True)

# Create new columns
df['Revenue'] = df['Fare'] * df['Passengers']
df['Total_Cost'] = df['Cost_per_passenger'] * df['Passengers']
df['Profit'] = df['Revenue'] - df['Total_Cost']

print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df['Passengers'], bins=20)
plt.title("Passenger Distribution")
plt.show()

sns.scatterplot(x='Distance_km', y='Fare', data=df)
plt.title("Distance vs Fare")
plt.show()

sns.countplot(x='Ticket_Type', data=df)
plt.title("Ticket Type Usage")
plt.xticks(rotation=45)
plt.show()

sns.boxplot(x='Remarks', y='Profit', data=df)
plt.title("Profit by Trip Type")
plt.show()


#Save Cleaned Dataset

df.to_csv("Cleaned_Public_transport_Analysis_data.csv",index=False)
print("Cleaned dataset saved as Cleaned_Public_transport_Analysis_data.csv")