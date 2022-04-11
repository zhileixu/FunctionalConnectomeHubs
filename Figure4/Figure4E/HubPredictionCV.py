import pandas
from sklearn import svm
from sklearn.model_selection import cross_val_predict

AHBA = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure4\Figure4E\Data\AHBA764x11027-ContributionOrder.csv", header=None)
Hub = pandas.read_csv(r"\FunctionalConnectomeHubs\Figure4\Figure4E\Data\Hub764.csv", header=None)

clf = svm.SVC()
for Genes in range(99, 299):
    Prediction = cross_val_predict(clf, AHBA.loc[:,0:Genes], Hub.values.ravel(), cv=382)
    Prediction = pandas.DataFrame(Prediction)
    Prediction.to_csv(r"\FunctionalConnectomeHubs\Figure4\Figure4E\Data\CV764x%03d.csv"%(Genes + 1), header=None, index=None)