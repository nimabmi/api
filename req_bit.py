# We are calling API request from coinbase
#ref is here https://docs.cdp.coinbase.com/sign-in-with-coinbase/docs/api-prices
#based on guide BTC-$ is based on below curl https://api.coinbase.com/v2/prices/BTC-USD/buy \
# you can run here in shell or cmd or Kinux terminal based on curl
# The output is based on JSON format so we neeed to call them in python ( parsing data)

import requests



response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/buy")
price = float(response.json()["data"]["amount"])

print("Bitcoin is %i in USD" %price)