from sklearn import svm
from sklearn.externals import joblib
import numpy as np

from cv import Cv

class Model:

    def getTrainData(self,filename):
        cv = Cv()
        feat = cv.getDigits(filename)
        features = []
        label = []
        for f in feat:
            features.append(f.copy())
            keyPressed = cv.getLabels(f)
            label.append(keyPressed)
        return features,label

    def convertIMToFeature(self,X):
        X = np.array(X,dtype=np.float64)
        X = [x.reshape(-1) for x in X]
        return X

    def trainModel(self):
        trainingData = ['/Users/Krishak/Desktop/t3.png',]
        X = []
        Y = []
        for file in trainingData:
            features,labels = self.getTrainData(file)
            for x in features: X.append(x)
            for y in labels: Y.append(y)

        X = self.convertIMToFeature(X)
        Y = np.array(Y,dtype=np.float64)


        clf = svm.SVC()
        clf.fit(X,Y)

        joblib.dump(clf, 'pickel/model.pkl')

    def loadModel(self):
        clf = joblib.load('pickel/model.pkl')
        return clf

    def testModel(self,features, labels):
        features = self.convertIMToFeature(features)
        clf = self.loadModel()
        prediciton = clf.predict(features)
        prediciton = [int(p) for p in prediciton]
        counter = 0
        for i in range(0, len(labels)):
            if int(labels[i]) == prediciton[i]: counter += 1
        accuracy = counter / len(labels)
        return accuracy