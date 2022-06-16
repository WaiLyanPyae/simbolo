import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import date

st.title('Crypto Price Watch By Wai Lyan Pyae <<Simbolo Batch-5>>')

tikcerSymbol = st.selectbox(
    'Please Select Your Crypto From Dropdown',
    ('EGLD-USD','BTC-USD','ETH-USD','ADA-USD','SOL-USD')
)
tickerData = yf.Ticker(tikcerSymbol)
tickerDf = tickerData.history(period='1d', start='2012-5-31', end=date.today())

st.subheader(f'Opening Price For {tikcerSymbol}')
st.line_chart(tickerDf.Open)

st.subheader(f'Closing Price For {tikcerSymbol}')
st.line_chart(tickerDf.Close)

st.subheader(f'Highest Price For {tikcerSymbol}')
st.bar_chart(tickerDf.High)

st.subheader(f'Lowest Price For {tikcerSymbol}')
st.area_chart(tickerDf.Low)

st.subheader(f'Volume For {tikcerSymbol}')
st.line_chart(tickerDf.Volume)
st.balloons()