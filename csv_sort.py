import pandas as pd
import ast

df = pd.read_csv("trees.csv")
soil_type = "Clay"
df = df[df["Soil_Type"] == soil_type].reset_index(drop=True)

columns = ["Ideal_Soil_pH","Ideal_Soil_Moisture_pct","Avg_Yearly_Temp_C","Avg_Yearly_Rainfall_mm","Altitude_m"]
environment = [5, 22, 18, 700, 600]

totals = [0] * len(df)

for i, col in enumerate(columns):
    for j, row in df.iterrows():
        # Parse string range like "[5,10]" into a list
        data = ast.literal_eval(row[col])
        lower, upper = float(data[0]), float(data[1])
        if "." in str(lower):
            lower *= 10
            upper *= 10
        elif lower > 100:
            lower /= 10
            upper /= 10

        # Compute difference from range
        if environment[i] < lower:
            dif = lower - environment[i]
        elif environment[i] > upper:
            dif = environment[i] - upper
        else:
            dif = 0

        totals[j] += dif

best_match = totals.index(min(totals))
print(df.loc[best_match]["Tree_Species"])
