from keras.models import Sequential
from keras.layers import Dense
import numpy
import pandas as pd

def train(data):

    # fix random seed for reproducibility
    seed = 7
    numpy.random.seed(seed)

    # split into input (X) and output (Y) variables
    X = data
    Y = pd.DataFrame() # empty data frame

    # get difference between tomorrow's open and tonight's close (absolute and percentage)
    # these will be the truth values to train on - hard coded, unfortunately
    Y["overnight_d"] = X["open"]-X["open_1_d"]-X["close"]
    Y["overnight_r"] = Y["overnight_d"]/X["close"]

    # remove truth parameters from training data
    X = X.drop("open_1_d", 1) # 1 means it's a column
    X = X.drop("open_1_r", 1)

    # just try to guess whether the overnight behavior will be positive or negative
    Y["overnight_d"] = [0 if value<=0 else 1 for value in Y["overnight_d"]]
    Y["overnight_r"] = [0 if value<=0 else 1 for value in Y["overnight_r"]]

    # create model
    model = Sequential()
    model.add(Dense(12, input_dim=len(X.keys()), init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='relu'))
    model.add(Dense(2, init='uniform', activation='sigmoid'))

    # compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    # fit the model
    model.fit(X.as_matrix(), Y.as_matrix(), validation_split=0.33, nb_epoch=150, batch_size=10) # 33% of the events will be used for testing
