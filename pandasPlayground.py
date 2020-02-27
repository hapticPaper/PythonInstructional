import pandas


files = [f"./datasets/stocks{s}.csv" for s in range(2014, 2017)]



stockDfs = []

for file in files:
    stockDfs.append(pandas.read_csv(file))

mins = []
for i, stockDf in enumerate(stockDfs):
    stockDfs[i] = stockDf.rename(columns = {'<ticker>':'ticker', '<date>':'dt', '<open>':'open', '<high>':'high', '<low>':'low', '<close>':'close', '<vol>':'volume'})
    stockDf.merge()