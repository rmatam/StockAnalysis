from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import SGD
import numpy
import pandas as pd

def train(data):

    # fix random seed for reproducibility
    seed = 7
    numpy.random.seed(seed)

    # split into input (X) and output (Y) variables
    X = data
    Y = pd.DataFrame() # empty data frame

    # calculate the value(s) to train on
    exec(open("Options/truthValues.py").read())

    # create model and set learning parameters
    exec(open("Options/model.py").read())
