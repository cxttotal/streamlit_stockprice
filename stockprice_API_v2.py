import streamlit as st
import tushare as ts

ts.set_token(st.secrets["auth_token"])
pro = ts.pro_api()

tickerSymbol = '000002.SZ'
tickerDf = pro.daily(ts_code=tickerSymbol, start_date='20180701', end_date='20180718')
tickerDf = tickerDf.sort_values(by='trade_date', ascending=True)

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of 000002.SZ!

""")

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.vol)