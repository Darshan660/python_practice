import pandas as pd
data = pd.read_csv("students.csv")
data.fillna(0,inplace=True)
data["Percentage"] = (data["act_composite"]+data["act_math"]+data["act_english"]+data["act_reading"]+data["sat_combined"]+data["sat_math"]+data["sat_verbal"]+data["sat_reading"])/240*100
print(data)
data.to_csv("final_student.csv")
