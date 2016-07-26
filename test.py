from cv import Cv

trainingData = ['/Users/Krishak/Desktop/t3.png','/Users/Krishak/Desktop/t1.jpg','/Users/Krishak/Desktop/train1.jpg',]
cv = Cv()

for filename in trainingData:
	cv.highlightContours(filename)
