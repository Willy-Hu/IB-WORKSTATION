from ib_insync import *

import pandas as pd

def open_trade_info(trade_object):
	  return {
        'orderId': trade_object.order.orderId,
        'action': trade_object.order.action,
        'totalQuantity': trade_object.order.totalQuantity,
        'orderType': trade_object.order.orderType,
        'lmtPrice': trade_object.order.lmtPrice,
        'secType': trade_object.contract.secType,
        'symbol': trade_object.contract.symbol
    }

# start the thread
util.startLoop()

ib = IB()

result = ib.connect('127.0.0.1', 7497, clientId=123)

print(result)

# get account information

# 1. get account summary

account_summary = ib.accountSummary(account='DU228379')

# transfer the data to DataFrame (need install pandas)

account_summary_df = pd.DataFrame(account_summary).set_index('tag')

#get cash
cash = account_summary_df.loc['AvailableFunds']
print(cash)

print("==get Securities Gross Position Value==")
# get Securities Gross Position Value
sgpv =  account_summary_df.loc['GrossPositionValue']

print(sgpv)


print("==get  Net Liquidation Value==")
#get Net Liquidation Value
nlv =  account_summary_df.loc['NetLiquidation']
print(nlv)



print("\n\n==buy stock==")
# buy stock
# 1. create contract

contract = Contract(
      secType='STK', # stock
      symbol='TSLA', # stock name
      exchange='SMART', # TWS smart route
      currency='USD' # USD
	)
# 2. create order

order = Order(
      action='BUY',      # BUY or SELL
      totalQuantity=20,  
      orderType='MKT',   # this field can be Market(MKT) or Limit(LMT
	)

# send the order request to server(TWS)
result_order = ib.placeOrder(contract, order)
print(result_order)


# list the unfinished order
open_trades = ib.openTrades()

open_trades_df=pd.DataFrame(list(map(lambda x : open_trade_info(x), open_trades)))
print(open_trades_df)
































