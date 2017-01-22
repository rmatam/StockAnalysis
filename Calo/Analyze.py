from keras.callbacks import EarlyStopping
import LoadData

exec("Settings.py")
(Train_X, Train_Y, Train_YT), (Test_X, Test_Y, Test_YT) = LoadData(inputFile, testFraction)

# Normalize the Data... seems to be critical!
Norm=np.max(Train_X)
Train_X=Train_X/Norm
Test_X=Test_X/Norm

# Build/Load the Model
from DLTools.ModelWrapper import ModelWrapper
from CaloDNN.Classification import *

TXS= Train_X.shape

NInputs=TXS[1]*TXS[2]*TXS[3]

if LoadModel:
    print "Loading Model From:",LoadModel
    if LoadModel[-1]=="/":
        LoadModel=LoadModel[:-1]
    Name=os.path.basename(LoadModel)
    MyModel=ModelWrapper(Name)
    MyModel.InDir=os.path.dirname(LoadModel)
    MyModel.Load()
else:
    print "Building Model...",
    sys.stdout.flush()
    MyModel=Fully3DImageClassification(Name,TXS,Width,Depth,BatchSize,NClasses,WeightInitialization)

    # Build it
    MyModel.Build()
    print " Done."

# Print out the Model Summary
MyModel.Model.summary()

# Compile The Model
print "Compiling Model."
MyModel.Compile(Loss=loss,Optimizer=optimizer) 

# Train
if Train:
    print "Training."
    callbacks=[EarlyStopping(monitor='val_loss', patience=2, verbose=1, mode='min') ]
    callbacks=[]

    MyModel.Train(Train_X, Train_Y, Epochs, BatchSize, Callbacks=callbacks)
    score = MyModel.Model.evaluate(Test_X, Test_Y, batch_size=BatchSize)

    print "Final Score:", score

# Save Model
if Train:
    MyModel.Save()

# Analysis
if Analyze:
    # ROC curve... not useful here:
    #from CaloDNN.Analysis import MultiClassificationAnalysis
    #result=MultiClassificationAnalysis(MyModel,Test_X,Test_Y,BatchSize )

    from EventClassificationDNN.Analysis import MultiClassificationAnalysis
    result=MultiClassificationAnalysis(MyModel,Test_X,Test_Y,BatchSize )


