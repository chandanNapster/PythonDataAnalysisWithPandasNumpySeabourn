# UNDERSTANDING THE FUNDAMENTALS FOR PANDAS
from ctypes import Union
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


# bank_client_df['Total'] = bank_client_df['Net Worth [$]'] *  bank_client_df['Years with bank']

# print(bank_client_df)
# filter = bank_client_df['Years with bank'] >= 4
# df_loyal_cust = bank_client_df[filter]
# print(df_loyal_cust)                                

# del bank_client_df['Total']

# print(bank_client_df)

# SELECT high networth indiduals with 5000+ minimum net worth
# What is the combined networth of these individuals

# filter = bank_client_df['Net Worth [$]'] > 5000
# bank_client_df = bank_client_df[filter]

# print("HIGH NET WORTH")
# print(bank_client_df)

# print(sum(bank_client_df['Net Worth [$]']))

# def increase_val(price):
#     bank_client_df['Net Worth [$]'] = bank_client_df['Net Worth [$]'] * 1.2
#     return bank_client_df

# print(increase_val(400))    


# print(bank_client_df)

# def networth_update(balance):
#     return balance * 1.2

# bank_client_df['Net Worth [$]'] = bank_client_df['Net Worth [$]'].apply(networth_update)



# print(bank_client_df)
# DEFINE A FUNCTION that triples the stock price and adds 200
# Apply the function 
# Calculate the updated total networth of all clients combined
# def tripleNet(balance):
#     return balance * 3 + 200

# bank_client_df['Net Worth [$]'] = bank_client_df['Net Worth [$]'].apply(tripleNet)    

# print(bank_client_df)

# print(sum(bank_client_df['Net Worth [$]']))


print(bank_client_df)

# SORT A DATA FRAME

print(bank_client_df.sort_values(by= 'Years with bank'))

# sorted_bank_client_df = bank_client_df.sort_values(by= 'Years with bank')
print(bank_client_df.sort_values(by= 'Years with bank', inplace=True))

print(bank_client_df)

# CONCATENATION AND MERGING WITH PANDAS
df1 = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                    'B':['B0', 'B1', 'B2', 'B3'],
                    'C':['C0','C1','C2','C3'],
                    'D':['D1','D2','D3','D4']}, index = [0,1,2,3])

print(df1)


df2 = pd.DataFrame({'A':['A4', 'A5', 'A6', 'A7'],
                    'B':['B4', 'B5', 'B6', 'B7'],
                    'C':['C4','C5','C6','C7'],
                    'D':['D4','D5','D6','D7']}, index = [4,5,6,7])


print(pd.concat([df1, df2]))