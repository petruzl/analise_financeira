import yfinance as yf
import ta
import pandas as pd
import plotly.graph_objects as go
ativo = '^BVSP'
dados = yf.download(ativo, start='2022-01-01', end='2023-08-01')
dados
periodo_sma = 20
dados['sma'] = ta.trend.sma_indicator(dados['Close'], window=periodo_sma)
dados
dados.head(30)
fig = go.Figure()
df_fig = dados
fig.add_trace(go.Candlestick(
    x=df_fig.index,
    open=df_fig['Open'],
    high=df_fig['High'],
    low=df_fig['Low'],
    close=df_fig['Close'],
    name='Grafico de Candlesticks com SMA'))
fig.add_trace(go.Scatter(name='sma',
                         x=df_fig.index,
                         y=dados['sma'],
                         marker_color='black'))
fig.update_layout(template='ggplot2', width=1400, height=700)
fig.show()