# # get difference between tomorrow's open and tonight's close (absolute and percentage)
# # these will be the truth values to train on - hard coded, unfortunately
# Y["overnight_d"] = X["open"]-X["open_1_d"]-X["close"]
# Y["overnight_r"] = Y["overnight_d"]/X["close"]

# # just try to guess whether the overnight behavior will be positive or negative
# Y["overnight_d"] = [0 if value<=0 else 1 for value in Y["overnight_d"]]
# Y["overnight_r"] = [0 if value<=0 else 1 for value in Y["overnight_r"]]

# Y["close_1_r"] = [1 if value<=0 else 0 for value in X["close_1_r"]]

twoWeekHighs = []
for i in range(2,15): # any high within the next two weeks (not counting today, because RobinHood doesn't allow day trading)
    if i == 2:
        twoWeekHighs = X["high"].shift(-i)
    else:
        twoWeekHighs = pd.concat([twoWeekHighs, X["high"].shift(-i)], axis=1)
twoWeekHighs = twoWeekHighs.dropna().max(axis=1)
Y["d_TwoWeekHigh_Open_r"] = (twoWeekHighs - X["open"]) / X["open"]
Y["d_TwoWeekHigh_Open_r"] = [0 if value<=0 else 1 for value in Y["d_TwoWeekHigh_Open_r"]]

# remove truth parameters from training data
X = X.drop("open_1_d", 1) # 1 means it's a column
X = X.drop("open_1_r", 1)
X = X.drop("close_1_d", 1)
X = X.drop("close_1_r", 1)
