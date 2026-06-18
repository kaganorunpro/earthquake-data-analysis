import pandas as pd
import matplotlib.pyplot as plt

# Sample earthquake dataset
data = {
    "city": ["Hatay", "Kahramanmaras", "Gaziantep", "Adiyaman", "Malatya"],
    "magnitude": [7.8, 7.5, 6.4, 6.3, 5.9],
    "depth_km": [17.9, 10.0, 12.0, 9.5, 14.2]
}

df = pd.DataFrame(data)

print("Earthquake Data")
print(df)

print("\nAverage Magnitude:")
print(df["magnitude"].mean())

plt.bar(df["city"], df["magnitude"])
plt.title("Earthquake Magnitudes by City")
plt.xlabel("City")
plt.ylabel("Magnitude")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
