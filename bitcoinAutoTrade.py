import time
import pyupbit
import datetime
import requests
#upbit token key#
access = ''
secret = ""
#slack message token key
myToken = ""

# 5 day moving average line
def get_ma5(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['close'].rolling(5).mean().iloc[-1]
    return ma5
# 10 day moving average line 
def get_ma10(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10 = df['close'].rolling(10).mean().iloc[-1]
    return ma10    
def get_ma20(ticker):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=10)
    ma10 = df['close'].rolling(20).mean().iloc[-1]
    return ma10  
def golden_cross(ticker):
   if get_ma5(ticker)>get_ma20(ticker):
        print("Golden Cross")
        return True
    
#volatility strategy 
def get_target_price(ticker, k):
    
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price 
#Send message to slack 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
def get_start_time(ticker):
    
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# login
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
post_message(myToken,"#stock","Auto Trade has started")
# Auto Trader
while True:

    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            print("chekc")
            target_price = get_target_price("KRW-BTC", 0.5)
            current_price = get_current_price("KRW-BTC")
            print( current_price, target_price)
            if   current_price>target_price:
                krw = get_balance("KRW")
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    #post_message(myToken,"#stock","Sucessfully bought:" + "KRW-XRP" +"at" + current_price)
                    
                #if earning is greater than 5 percent sell.
                # if  current_price%bought_price >=1.05:
                #     btc = get_balance("XRP")
                #     if btc > 0.00008:
                #         upbit.sell_market_order("KRW-XRP", btc*0.9995)
                #         post_message(myToken,"#stock"," You earned 5 percent executing code ")

        else:
            btc = get_balance("BTC")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-BTC", btc*0.9995)
        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1) 

       