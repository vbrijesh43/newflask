import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("pending.xlsx")

# Remove empty rooms
df = df.dropna(subset=["ROOM NUMBER"])

# -------- Chart 1 : Top Pending Rooms --------
top_rooms = df.sort_values("TOTAL AMOUNT", ascending=False).head(10)

plt.figure()
plt.bar(top_rooms["ROOM NUMBER"].astype(str), top_rooms["TOTAL AMOUNT"])
plt.xlabel("Room Number")
plt.ylabel("Total Amount")
plt.title("Top 10 Rooms by Total Pending Amount")
plt.show()


# -------- Chart 2 : Monthly Collection Trend --------
month_columns = [col for col in df.columns if "collection" in col.lower()]
monthly_totals = df[month_columns].sum()

plt.figure()
plt.plot(monthly_totals.index, monthly_totals.values, marker='o')
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Collection Amount")
plt.title("Monthly Collection Trend")
plt.show()