from model import Model
from calculator import Calculator
from cv import Cv

def getData(filename):
    cv = Cv()
    model = Model()
    digits = cv.getDigits(filename)
    digits = model.convertIMToFeature(digits)
    clf = model.loadModel()
    prediciton = clf.predict(digits)
    prediciton = [chr(int(p)) for p in prediciton]
    prediciton = ''.join(prediciton)
    return prediciton

# TODO Print answer onto image
def display(equation):
    calculator = Calculator()
    answer = calculator.evaluate(equation)
    print("Answer is "+str(answer))


def readFromVideo(self):
    pass

filename = "/Users/Krishak/Desktop/test1.png"
prediction = getData(filename)
display(prediction)