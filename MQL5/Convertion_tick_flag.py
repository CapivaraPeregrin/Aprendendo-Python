import MetaTrader5 as mt5
from datetime import datetime, timedelta
import pandas as pd
import random
import pytz

def tratamento_df(df):
    '''Estabeleçe a coluna "time" como index e cria a coluna de classificação flags'''
    df.set_index("time", inplace=True )
    df.index = pd.to_datetime(df.index, utc=True, unit = 's')
    df["flag_nome"] = df["flags"].apply(lambda x: nome_das_flag(x))
    return df
   
def nome_das_flag(flag):
    '''
    Função para ser aplicada via apply que classifica os trades conforme o bolleano do binario dos números de classificação estabelecidos pela corretora
    '''
    nome = ""
    
    try:
        flag = int(flag)
        if flag & mt5.TICK_FLAG_BID:
            nome += ", BID"
        if flag & mt5.TICK_FLAG_ASK:
            nome += ", ASK"
        if flag & mt5.TICK_FLAG_LAST:
            nome += ", LAST"
        if flag & mt5.TICK_FLAG_VOLUME:
            nome += ", VOLUME"
        if flag & mt5.TICK_FLAG_BUY:
            nome += ", BUY"
        if flag & mt5.TICK_FLAG_SELL:
            nome += ", SELL"
        nome = nome[2:]
        if ("BUY" in nome) & ("SELL" in nome): 
            nome = "DIRETO"
        return nome
    except ValueError:
        print("A variável flag não contém um número válido.")
        return "ERRO"


# Connect to MetaTrader 5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

# Definindo ticker e periodo
ticker = "BTCUSD"

# set time zone to UTC and create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
timezone = pytz.timezone("Etc/UTC")
time_0 = datetime(2023, 12, 10, 9, tzinfo=timezone)
time_1 = datetime(2023, 12, 12, 10, tzinfo=timezone)

# Request ticks data
ticks = mt5.copy_ticks_range(ticker, time_0, time_1, mt5.COPY_TICKS_ALL)
df = pd.DataFrame(ticks)
df = tratamento_df(df)
print(df.head(100))
