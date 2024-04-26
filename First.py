import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Read data from data base 
df=pd.read_csv(r"C:\Users\Shubm\OneDrive\Desktop\ByteUprise_DS_01\Customer.csv")

#plot a bar graph 
sns.barplot(data=df,x='Delivery',y='Speed_Delivery')
plt.title("Rating of Delivery VS Rating of Accuracy of Delivery")
plt.show()

#plot a histogram 
plt.hist(df['Food'], bins=10, edgecolor='black')
plt.xlabel('Food')
plt.ylabel('Stars')
plt.title('Food Quality Distribution Histogram')
plt.show()

# Plotting a pie chart
gender_counts = df['Food'].value_counts()
plt.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Food Quality Composition Pie Chart')
plt.show()

