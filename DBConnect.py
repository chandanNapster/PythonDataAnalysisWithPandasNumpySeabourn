import csv 
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from matplotlib import pyplot as plt 
# print("Hello World")
from warnings import filterwarnings

filterwarnings('ignore')

hackData = pd.read_csv("E:\PythonWorkbook\PythonDataAnalysisWithPandasNumpySeabourn\Data\Hack.csv")



pd.to_numeric(hackData["TotalScores"])
# print("HALLOOOOO")
# print(hackData.info())

# print(hackData.info())

hackGroupby = hackData.groupby("GroupID").agg({"TotalScores": np.mean, "GroupID": np.size})

# print(hackGroupby)

hackGroupby = hackGroupby.rename(columns={'GroupID': 'Number Group Members', 'TotalScores': 'Total (Out of 15)'})




sns.set(style="darkgrid", color_codes = True)
j = sns.jointplot(data = hackGroupby, x="Total (Out of 15)",y = "Number Group Members",kind='reg',color='g')
r,p = stats.pearsonr(hackGroupby['Total (Out of 15)'], hackGroupby['Number Group Members'])

print(r)
# sns.histplot(hackGroupby.TotalScores,kde=True) 
plt.show()

hackGroupby = hackGroupby.rename(columns={'Number Group Members': 'GroupNum', 'Total (Out of 15)': 'Total'})
 
print(hackGroupby.sort_values(by=['Total'], ascending=False))

# gf = df.groupby('GroupID')TotalScores
# gff = gf.first()
# print(gff.sort_values(by=['TotalScores']))
