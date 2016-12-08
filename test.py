from cv import Cv

trainingData = []
cv = Cv()

for filename in trainingData:
	cv.highlightContours(filename)
