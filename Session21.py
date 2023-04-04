import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
"""
demo_list = [1,2,3,4]
demo_array = np.array(demo_list)
print("list in python :",demo_list,type(demo_list))
print("array in python :",demo_array,type(demo_array))

print(list(map(lambda x:x,demo_array)))

for i in demo_array:
    print(i)

a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
"""
df = pd.read_csv("nse.csv")
print(df)

df = df[['close ','OPEN ','HIGH ','LOW ']]
print(df)

forecast_col = 'close '
forecast_out = 3
df['label'] = df[forecast_col].shift(-forecast_out)
print(df)

x = np.array(df.drop(['close ','label'],1))
print(x)

x_lately = x[-forecast_out:]
print("X Lately:",x_lately)

x = x[:-forecast_out]
print("X ready:",x)

y = np.array(df['label'])
y = y[:-forecast_out]
print("Y ready:",y)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)
clf = LinearRegression()
clf.fit(x_train,y_train)

confidence = clf.score(x_test,y_test)
print('confidence:',confidence)
forecast_set = clf.predict(x_lately)
print(forecast_set)