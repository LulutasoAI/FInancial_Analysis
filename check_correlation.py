from tracemalloc import start
from Correlation_Analysis import Correlation_Analysis
import utils
from Log_Return_Process import Log_Return_Process
import pandas as pd

class Check_Correlation():
    def __init__(self,start_date= "2015-01-01"):
        self.symbol1 = str(input("input symbol1\n"))
        self.symbol2 = str(input("input symbol2\n"))
        self.start_date = start_date
        self.Log_Process = Log_Return_Process()
        self.Correlation_analysis = Correlation_Analysis()

    def fetch_prices(self,symbol1, symbol2):
        prices_a = utils.stock_id_to_prices(symbol1,self.start_date)
        prices_b = utils.stock_id_to_prices(symbol2, self.start_date)
        return prices_a,prices_b
    
    def check_pure_correlation(self):
        #usually not usable because gold and stocks both go up thanks to continuous inflation.
        series1,series2 = self.fetch_prices(self.symbol1,self.symbol2)
        self.Correlation_analysis.main(series1,series2)

    def convert_value_into_logged_one(self,series : pd.Series) -> pd.Series:
        result = pd.Series(dtype='float64')
        index = series.index[1:]
        new_values = self.Log_Process.prices_to_log_return(series)[1:]
        for i in range(len(new_values)):
            result[index[i]] = new_values[i]
        return result 


    def normalized_correlation(self):
        
        series1,series2 = self.fetch_prices(self.symbol1,self.symbol2)
        series1 = self.convert_value_into_logged_one(series1)
        series2 = self.convert_value_into_logged_one(series2)
        self.Correlation_analysis.main(series1,series2)
        
        #series1 = self.Log_Process.
    
    def Correlation_with_formula(self):
        """
        2つの証券Ａ、Ｂの相関係数の式は
        （2つの証券の共分散）÷（証券Ａの標準偏差と証券Ｂの標準偏差との積）
        として定義される。
        """
        pass 




if __name__ == "__main__":
    checker = Check_Correlation()
    #checker.main()
    checker.normalized_correlation()