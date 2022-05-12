import pandas as pd
import numpy as np
import matplotlib as plt
import requests


apiKey = "8cdcf870de9c79ffcb439e879b28a062f770eb58"



headers = {'Content-Type': 'application/json'}


vector = ["AAPL","TSLA","AXP","SHOP"]

requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=8cdcf870de9c79ffcb439e879b28a062f770eb58", headers=headers)

print(requestResponse.json())

out1 = requestResponse.json()


outDf = pd.DataFrame(out1)

outDf['date']

outDf.describe()


np.
