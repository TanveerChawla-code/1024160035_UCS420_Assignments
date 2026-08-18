import pandas as pd
df = pd.read_csv("A3/Iris.csv")
df = df.drop(index = 4)
df= df.drop(df.columns[3],axis = 1)
print(df)

