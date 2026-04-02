import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv('data/cleaned_data.csv')

# Plot 1: Experiment Score vs Student ID
plt.figure()
plt.plot(df['student_id'].tolist(), df['experiment_score'].tolist())
plt.xlabel('Student ID')
plt.ylabel('Experiment Score')
plt.title('Experiment Score vs Student ID')
plt.savefig('results/score_plot.png')

# Plot 2: Temperature vs Humidity
plt.figure()
plt.scatter(df['temperature'].tolist(), df['humidity'].tolist())
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.title('Temperature vs Humidity')
plt.savefig('results/temp_humidity_plot.png')

print("Plots saved in results/")

