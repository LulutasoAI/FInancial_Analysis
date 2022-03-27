from tracemalloc import start
from Correlation_Analysis import Correlation_Analysis
import utils
from Log_Return_Process import Log_Return_Process
import pandas as pd
import numpy as np
from pandas_datareader import data
from matplotlib import pyplot as plt
from datetime import date
"""
This one I think is quite high level class. 
"""
class Check_Correlation():
    def __init__(self,start_date= "1980-01-01"):
        #self.symbol1 = str(input("input symbol1\n"))
        #self.symbol2 = str(input("input symbol2\n"))
        self.symbol1 = "^GSPC"
        self.symbol2 = "^N225"
        self.start_date = start_date
        self.Log_Process = Log_Return_Process()
        self.Correlation_analysis = Correlation_Analysis()

    def stock_id_to_prices_in_range(self, symbol:str,start_date:str,end_date:str) -> pd.Series:
        
        df = data.DataReader(symbol, "yahoo", start_date, end_date)
        df = df[[ "Open", "High", "Low", "Close", "Volume"]]
        prices = df["Close"]
        return prices 

    def fetch_prices_in_range(self, symbol1:str, symbol2:str, start:str, end : str)-> tuple:
        prices_a = self.stock_id_to_prices_in_range(symbol1, start, end)
        prices_b = self.stock_id_to_prices_in_range(symbol2, start, end)
        return prices_a,prices_b

    def fetch_prices(self,symbol1 : str, symbol2 : str) -> tuple:
        prices_a = utils.stock_id_to_prices(symbol1,self.start_date)
        prices_b = utils.stock_id_to_prices(symbol2, self.start_date)
        return prices_a,prices_b
    
    def test_output_correlation_change_throughout_time(self):
        today = date.today()
        end_date = "{}".format(today)
        symbol1 = "^GSPC"
        symbol2 = "^N225"
        start_end1 = ["1980-01-01", "2008-01-01"]
        start_end2 = ["2008-01-01",end_date]
        self.output_correlation_change_throughout_time(symbol1,symbol2, start_end1,start_end2)
        

    def output_correlation_change_throughout_time(self, symbol1 :str, symbol2:str, start_end1:list, start_end2 : list):
        """
        start_endn might be like ["1994-01-01", "2008-01-01"]
        """
        result : list(float) = [] #[correlation, correlation2]
        series1_first, series2_first = self.fetch_prices_in_range(symbol1, symbol2, start_end1[0],start_end1[1])
        series1_last, series2_last = self.fetch_prices_in_range(symbol1, symbol2, start_end2[0],start_end2[1])
        correlation_first = self.Correlation_analysis.main(series1_first,series2_first) #explicitly name the variable so that it is more readable.
        correlation_last = self.Correlation_analysis.main(series1_last,series2_last)
        result = [correlation_first,correlation_last]
        print(result,"correlation between the range of {} and {}".format(start_end1,start_end2))
        plt.plot(np.array(result))
        plt.show()

    def check_pure_correlation(self):
        #usually not usable because gold and stocks both go up thanks to continuous inflation.
        """
        I thought it was not usable but it turned out this function is fine.
        Thanks to the monetary crazy easing The market is distorted.
        """
        series1,series2 = self.fetch_prices(self.symbol1,self.symbol2)
        self.Correlation_analysis.main(series1,series2)

    def convert_value_into_logged_one(self,series : pd.Series) -> pd.Series:
        """
        It safely converts pd.Series.values into logged values. 
        """
        result = pd.Series(dtype='float64')
        index = series.index[1:]
        new_values = self.Log_Process.prices_to_log_return(series)[1:]
        for i in range(len(new_values)):
            result[index[i]] = new_values[i]
        return result 


    def normalized_correlation(self) -> None:
        """
        I thought correlation check was wack because they are not normalized.
        Attempted to normalize the procedure by making them logged.
        It turned out that it might be totally meaningless.
        """
        series1,series2 = self.fetch_prices(self.symbol1,self.symbol2)
        series1 = self.convert_value_into_logged_one(series1)
        series2 = self.convert_value_into_logged_one(series2)
        self.Correlation_analysis.main(series1,series2)
        
        #series1 = self.Log_Process.
    
    def Correlation_with_formula(self) -> float:
        """
        Correlation check with proper formula.
        but it turned out to be the same result
        as self.check_pure_correlation.
        """
        series1,series2 = self.fetch_prices(self.symbol1,self.symbol2)
        series1, series2 = self.Correlation_analysis.arrange_serieses(series1,series2)
        covariance = np.cov(series1,series2)[0][1]
        #print(np.cov(series1,series2)[0][1])
        denominator = np.std(series1) * np.std(series2)
        result = covariance/denominator
        print(result,"the correlation between {} and {} since {}".format(self.symbol1, self.symbol2,self.start_date ))
        return result




if __name__ == "__main__":
    checker = Check_Correlation()
    #checker.check_pure_correlation()
    print("devider")
    #checker.normalized_correlation()
    checker.Correlation_with_formula()
    #going to test correlationcompare.
    checker.test_output_correlation_change_throughout_time()