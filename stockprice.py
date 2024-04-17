import streamlit as st
import tushare as ts

ts.set_token("2da7dafaf4c64cbc39970911a2ff4f2fb622d4b274c9d05bb8745949")
pro = ts.pro_api()

tickerSymbol = '000001.SZ'
tickerDf = pro.daily(ts_code=tickerSymbol, start_date='20180701', end_date='20180718')
tickerDf = tickerDf.sort_values(by='trade_date', ascending=True)

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of 000001.SZ!

""")

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.vol)