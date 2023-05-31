# Importing all the libraries:

import yfinance as yf 
import streamlit as st 
import pandas as pd

# Here we write the header : 1 hashtage in the header means H1. adding more hashtags will make the font smaller.
# To bold a word - ***word*** 
# refer to the markdown cheatsheet.
st.write("""
# Simple Stock price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'APPL'

# Get data on the ticker:
tickerData = yf.Ticker(tickerSymbol)

# Getting the historical prices for this ticker:
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# The contents of the data frame comprise of - Open,high,low,close,volume,dividends,stock,splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)




# to run the application we write in terminal - streamlit run finance.py



