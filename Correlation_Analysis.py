import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt


class Correlation_Analysis():
    def __init__(self):
        pass 

    def disinfector(self, pandas_series):
        disinfected_series = pd.Series() 
        for i in range(len(pandas_series)):
            disinfected_series[pandas_series.index[i]] = pandas_series.values[i]
        return disinfected_series 
    
    def sort_order(self,series1,series2):
        if len(series1) >= len(series2):
            return series1,series2
        else:
            return series2, series1 
    
    def cut_abundancy(self, longer_series,shorter_series):
        result1 = pd.Series(dtype='float64')
        result2 = shorter_series
        for i in range(len(longer_series)):
            if longer_series.index[i] in shorter_series.index:
                result1[longer_series.index[i]] = longer_series.values[i]
        return result1, result2


    def arrange_serieses(self,series1, series2):
        #high level
        series1 = self.disinfector(series1)
        series2 = self.disinfector(series2)
        longer_series, shorter_series = self.sort_order(series1,series2)
        result1, result2 = self.cut_abundancy(longer_series,shorter_series)
        if len(result1) == len(result2):
            return result1, result2
        else:
            return self.cut_abundancy(result2,result1)
    
    def main(self,series1,series2):
        result1,result2 = self.arrange_serieses(series1,series2)
        print(len(result1),len(result2))
        plt.scatter(result1,result2)
        plt.show()
        print(result1,result2)
        print(np.corrcoef(result1,result2)[0][1])

    
