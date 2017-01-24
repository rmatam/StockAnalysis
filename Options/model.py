# set up the model
model = Sequential()
model.add(Dense(12, input_dim=len(X.keys()), init='uniform', activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(Y.keys()), init='uniform', activation='sigmoid'))

# set learning parameters and compile the model
sgd = SGD(lr=0.05, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['accuracy'])

# fit the model
model.fit(X.as_matrix(), Y.as_matrix(), validation_split=0.33, nb_epoch=5000, batch_size=10) # 33% of the events will be used for testing
