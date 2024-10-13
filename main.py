from mercado_bitcoin import DataAPI

tick = DataAPI()
tick.ticker("BTC")

print(type(tick))