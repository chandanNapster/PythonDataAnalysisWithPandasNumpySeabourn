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

hackGroupby = hackGroupby.rename(columns={'GroupID': 'Number of Group Members', 'TotalScores': 'Total Marks (Out of 15)'})




sns.set(style="darkgrid", color_codes = True)
j = sns.jointplot(data = hackGroupby, x="Total Marks (Out of 15)",y = "Number of Group Members",kind='reg', color='#4169e1')
r,p = stats.pearsonr(hackGroupby['Total Marks (Out of 15)'], hackGroupby['Number of Group Members'])

print(r)
# sns.histplot(hackGroupby.TotalScores,kde=True) 
plt.show()

hackGroupby = hackGroupby.rename(columns={'Total Marks (Out of 15)': 'Total'})
 
final_result = hackGroupby.sort_values(by=['Total'], ascending=False).reset_index()

print(final_result)

final_result.to_csv('final_result.csv', index=False)




# gf = df.groupby('GroupID')TotalScores
# gff = gf.first()
# print(gff.sort_values(by=['TotalScores']))


