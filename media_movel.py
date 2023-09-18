import yfinance as yf
import ta
import pandas as pd
import plotly.graph_objects as go
ativo = '^BVSP'
dados = yf.download(ativo, start='2022-01-01', end='2023-08-01')
dados
