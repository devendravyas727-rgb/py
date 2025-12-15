import yfinance as yf
import pandas as pd
import numpy as np

ticker = "^NSEBANK"
data = yf.download (ticker, start ="2007-09-17", end="2025-09-17")

data["daily_return"] = data["Close"].pct_change()
data["state"] = np.where(data["daily_return"] >= 0, "up", "down")

up_counts = len(data[data["state"] == "up"])
down_counts = len(data[data["state"] == "down"])
up_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1) == "up") ]) / up_counts
down_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1) =="down") ]) / up_counts
up_to_down = len(data[(data["state"] == "down") & (data["state"].shift(-1) == "up") ]) / down_counts
down_to_down = len(data[(data["state"] == "down") & (data["state"].shift(-1) == "down") ]) / down_counts
transition_matrix = pd.DataFrame({    
    "up": [up_to_up, up_to_down],
    "down": [down_to_up,down_to_down]
}, index=["up","down"])

print(transition_matrix)
