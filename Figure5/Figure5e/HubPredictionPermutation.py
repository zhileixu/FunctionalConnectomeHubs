import pandas
from sklearn import svm
from sklearn.model_selection import cross_val_predict

Hub = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure5\Figure5e\Data\Hub764.csv", header=None)

clf = svm.SVC()
for RandSeed in range(0, 999):
    AHBA = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure5\Figure5e\Data\AHBA764x150-%04d.csv"%(RandSeed), header=None)
    
    Prediction = cross_val_predict(clf, AHBA, Hub.values.ravel(), cv=382)
    Prediction = pandas.DataFrame(Prediction)
    Prediction.to_csv(r"\FunctionalConnectomeHubs\Figure5\Figure5e\CV764x150-%04d.csv"%(RandSeed), header=None, index=None)