import pandas
from sklearn import svm
from sklearn.model_selection import cross_val_predict

Hub = pandas.read_csv(r"\FunctionalConnectomeHubs\FigureS8\FigureS8A\Data\Hub764.csv", header=None)

clf = svm.SVC()

for RandSeed in range(1, 1001):
    AHBA = pandas.read_csv(r"\FunctionalConnectomeHubs\FigureS8\FigureS8A\Data\AHBA764x150-%04d-Surrogate.csv"%(RandSeed), header=None)
    
    Prediction = cross_val_predict(clf, AHBA, Hub.values.ravel(), cv=382, n_jobs=8)
    Prediction = pandas.DataFrame(Prediction)
    Prediction.to_csv(r"\FunctionalConnectomeHubs\FigureS8\FigureS8A\CV382Fold\CV764x150-%04d.csv"%(RandSeed), header=None, index=None)
