import pandas as pd
data = pd.read_csv('Workbook1.csv')
"""
print(data)
#print(data.columns.values)
#print(data['ID'])
#print(data['PHYSICS'])
#print(data.info())
#print(data[['ID','Physics','Maths']])
print(data['ID'].tolist())

#Question:
for i in data['Maths']:
    if i>=50:
        print(i)
   
#other method
print(data[data["Maths"]>50])

#
print(data.dropna())
print(data.fillna("CS"))

#
data["Total"]=data["Physics"]+data["Chemistry"]+data["Maths"]
print(data)
print(data[data["Total"]>150])

data["Chemistry_Result"] = data["Chemistry"].apply(lambda x:"pass" if x>35 else "fail")

data["Physics_Result"] = data["Physics"].apply(lambda x:"good" if x>75  else "third class")
print(data)

print(data.drop(["ID"],axis=1))

data.to_csv("mydata.csv")
 """
