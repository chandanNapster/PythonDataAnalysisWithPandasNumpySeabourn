# UNDERSTANDING THE FUNDAMENTALS FOR PANDAS
import pandas as pd
import lxml

# 2-D PANDAS DATA FRAME

# bank_client_df = pd.DataFrame({'Bank Client ID':[111,222,333,444],
#                                 'Bank Client Name':['Ron', 'Steve', 'Tom', 'Harry'],
#                                 'Net Worth [$]':[350000, 290000, 10000, 3000],
#                                 'Years with bank': [3,4,9,5]})

# print(bank_client_df)
# print(type(bank_client_df))
# print(bank_client_df.head(2))  
# print(bank_client_df.tail(2))      
# print(bank_client_df.describe())                        

# ANALYZING STOCK DATA SYMBOL A
# E:\PythonWorkbook\PythonDataAnalysisWithPandasNumpySeabourn\Data\archive\stocks\AAPL.csv

# apple_stocks = pd.read_csv("E:\PythonWorkbook\PythonDataAnalysisWithPandasNumpySeabourn\Data\AAPL.csv")

# print(apple_stocks)

# portfolio_df = pd.DataFrame({'Stock ticker symbol':['AAPL','AMZN','AABA'],
#                                 'Price per share [$]':[3500, 200, 4000],
#                                 'Number of Stocks':[3,4,9]})

# portfolio_df['Total'] = portfolio_df['Price per share [$]'] * portfolio_df['Number of Stocks']


# print(portfolio_df)
# print(sum(portfolio_df['Total']))

# READ HTML AND CSV FILES
# SOME SORT OF WEB SCRIPPING
# LIVING IN CANADA

# have to install lxml
# pip install lxml 
# url =  'https://www.livingin-canada.com/house-prices-canada.html' 
# url_2 = 'https://www.ssa.gov/oact/progdata/nra.html'
# house_price_df = pd.read_html(url_2)

# print(house_price_df)

# TASK NUMBER 8
# FILTER ON A SPECIFIC ROW

bank_client_df = pd.DataFrame({'Bank Client ID':[111,222,333,444],
                                'Bank Client Name':['Ron', 'Steve', 'Tom', 'Harry'],
                                'Net Worth [$]':[350000, 290000, 10000, 3000],
                                'Years with bank': [3,4,9,5]})


bank_client_df['Total'] = bank_client_df['Net Worth [$]'] *  bank_client_df['Years with bank']

print(bank_client_df)
filter = bank_client_df['Years with bank'] >= 4
df_loyal_cust = bank_client_df[filter]
print(df_loyal_cust)                                

del bank_client_df['Total']

print(bank_client_df)

# SELECT high networth indiduals with 5000+ minimum net worth
# What is the combined networth of these individuals

filter = bank_client_df['Net Worth [$]'] > 5000
bank_client_df = bank_client_df[filter]

print("HIGH NET WORTH")
print(bank_client_df)

print(sum(bank_client_df['Net Worth [$]']))