import csv 
import pandas as pd
import numpy as np

# print("Hello World")

hackData = pd.read_csv("E:\PythonWorkbook\Data\Hack.csv")



pd.to_numeric(hackData["TotalScores"])
# print("HALLOOOOO")
print(hackData.info())

# print(hackData.info())

hackGroupby = hackData.groupby("GroupID").agg({ "GroupID": np.size, "TotalScores": np.mean})

print(hackGroupby.describe())

# gf = df.groupby('GroupID')TotalScores
# gff = gf.first()
# print(gff.sort_values(by=['TotalScores']))