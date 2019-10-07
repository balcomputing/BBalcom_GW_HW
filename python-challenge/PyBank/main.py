import pandas as pd
import csv
import os

budget = pd.read_csv(r'budget_data.csv')
budget.head()

months = budget["Date"].count()
net = budget["Profit/Losses"].sum()
av_chg = budget["Profit/Losses"].mean()
maxprofit = budget.loc[budget["Profit/Losses"].idxmax()]
maxlosses = budget.loc[budget["Profit/Losses"].idxmin()]

o = open("output.txt", "w")

print("Financial Analysis", file = o)
print("------------------", file = o)

print(months, file = o)
print(net, file = o)
print(av_chg, file = o)
print(maxprofit, file = o)
print(maxlosses, file = o)



