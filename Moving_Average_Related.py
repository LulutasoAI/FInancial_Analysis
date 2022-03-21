import pandas as pd
import numpy as np
import pandas_datareader as dt
import datetime
from matplotlib import pyplot as plt
from Baseutils import Baseutils
class MA(Baseutils):
    def __init__(self):
        #for MA
        super().__init__()
        self.periods = [13,89,144]

    def MA(self, data, period):
        """This creates the MA data based on the set period like 14 100 144 200 and so on"""
        ma = []
        for i, dat in enumerate(data):
            if i > period:
                m = np.mean(data[i-period:i])
                ma.append(m)
            else:
                ma.append(0)
        #plt.plot(data)
        #plt.plot(ma)
        #plt.show()
        return ma

    def mashandler(self,mas, prices,rang):
        colors = ["green", "yellow", "red"]
        for i,a in enumerate(mas):
            plt.plot(a[-rang:],color = colors[i])
        plt.plot(prices[-rang:],color = "black")
        plt.title("green = MA20, yellow = 144, red = 200")
        plt.show()

    def df2price(self,data):
        return data["Close"]

    def main(self, stkname):
        """
        It's Up to date use this.
        """
        data = self.stksearch(stkname, self.start, self.end)
        prices = self.df2price(data)
        mas = []
        colors = ["green", "yellow", "red"]
        for i, period in enumerate(self.periods):
            ma = self.MA(prices, period)
            mas.append(ma)
            plt.plot(data.index,ma,color = colors[i])
        plt.plot(data.index,prices,color = "black")
        plt.title("green = {}, yellow = {}, red = {}".format(self.periods[0],self.periods[1],self.periods[2]))
        plt.show()
        plt.close()
        #self.mashandler(mas,prices,20)
        prediction : int = self.Prediction_from_mas(mas)
        if prediction ==1:
            print("up")
        elif prediction == 0:
            print("neutral")
        else:
            print("down")
        return mas
    
    def Prediction_from_mas(self,mas : list) ->  int:
        p = 0
        for i in range(len(self.periods)):
            #print(mas[a], "this is _ {}".format(a))
            if mas[i][-1] - mas[i][-199] >= 0:
                if i == 0:
                    print("{} is positive".format(self.periods[i]))
                elif i == 1:
                    print("{} is positive".format(self.periods[i]))
                elif i == 2:
                    print("{} is positive".format(self.periods[i]))
                p += 1
        if p >= 3:#The higher p is, the more MAs were upwards
            return 1
        elif p == 2:
            return 0
        else:
            return -1

        
    def MAprediction(self, data):
        prices = data[-400:]
        mas = []
        colors = ["green", "yellow", "red"]
        for i, period in enumerate(self.periods):
            ma = self.MA(prices, period)
            mas.append(ma)
        #self.mashandler(mas,prices,199)
        p = 0
        for a in range(0,3):
            #print(mas[a], "this is _ {}".format(a))
            if mas[a][-1] - mas[a][-199] >= 0:
                if a == 0:
                    print("{} is positive".format(self.periods[0]))
                elif a == 1:
                    print("{} is positive".format(self.periods[1]))
                elif a == 2:
                    print("{} is positive".format(self.periods[2]))
                p += 1
        if p == 3:#The higher p is, the more MAs were upwards
            return 1
        elif p == 2:
            return 0
        else:
            return -1

if __name__ == "__main__":
    ma = MA()
    ma.main("^N225")