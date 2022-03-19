from pandas_datareader import data
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt 
from datetime import date
import scipy.stats as scs
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from pandas_datareader import data
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from datetime import date
from pandas_datareader import data
from decimal import Decimal
from utils import stock_id_to_prices
class Log_Return_Process():
    def __init__(self):
        self.start_date = "1980-01-01"
        pass 
    
    def stock_id_to_prices(self,stock_id,start_date):
        today = date.today()
        end_date = "{}".format(today)
        df = data.DataReader(stock_id, "yahoo", start_date, end_date)
        df = df[[ "Open", "High", "Low", "Close", "Volume"]]
        prices = df["Close"]
        return prices
    
    def prices_to_log_return(self,prices):
        return np.log(prices/prices.shift(1))
    
    def prices_to_return(self,prices):
        return (prices/prices.shift(1))
    
    def get_log_return_from_stock_id(self,stock_id):
        prices = stock_id_to_prices(stock_id,self.start_date)
        log_return = self.prices_to_log_return(prices)
        return log_return
    
    def returns_raw_graph(self,log_returns):
        plt.plot(log_returns)
        plt.show()
        
    def qqplot(self,log_returns):
        sm.qqplot(log_returns.dropna(), line = "s")
        plt.show()
        
    def information_checker(self,log_returns,data_name=""):
        result_information = {}
        mean = log_returns.mean()
        std = log_returns.std()
        max_return = log_returns.max()
        worst_return = log_returns.min()
        sum_of_return = np.sum(log_returns)
        print("Data name = {}\nsum : {}\nmean : {} \nstd : {}\nmax_return : {}%\nworst_return : {}%".format(data_name,sum_of_return,mean, std, round(max_return*100,1), round(worst_return*100,1)))
        worst_index = np.argmin(log_returns)
        best_index = np.argmax(log_returns)
        plt.title("Worst200days around the worst day. Data name = {}".format(data_name))
        plt.plot(log_returns[max(worst_index-100,0):min(worst_index+100,len(log_returns))])
        plt.show()
        plt.title("best200days around the best day. Data name = {}".format(data_name))
        plt.plot(log_returns[max(best_index-100,0):min(best_index+100,len(log_returns))])
        plt.show()
        result_information["mean"] = mean
        result_information["std"] = std
        result_information["max_return"] = max_return
        result_information["worst_return"] = worst_return
        result_information["sum_of_return"] = sum_of_return
        return result_information
    
    def seasonal_information(self,log_return):
        seasonal_performances = []
        length = len(log_return)
        print
        start_point = 0
        first_point = length//3
        middle_point = first_point*2
        
        print("aa",length, first_point,middle_point)
        end_point = length
        first_part = log_return[start_point:first_point]
        middle_part = log_return[first_point:middle_point]
        last_part = log_return[middle_point:end_point]
        
        first_info_set = self.information_checker(first_part,"First_part")
        second_info_set = self.information_checker(middle_part,"Middle_part")
        last_info_set = self.information_checker(last_part,"Last_part")
        seasonal_performances.append(first_info_set["mean"])
        seasonal_performances.append(second_info_set["mean"])
        seasonal_performances.append(last_info_set["mean"])
        plt.plot(seasonal_performances)
        plt.show()
        
    def examine_wholly(self,symbol):
        prices = self.stock_id_to_prices(symbol,self.start_date)
        self.converter(prices)
        log_returns = self.prices_to_log_return(prices)
        self.returns_raw_graph(log_returns)
        self.converter(log_returns)
        self.information_checker(log_returns,"whole data")

        self.seasonal_information(log_returns)
    
    def replace_nan(self,prices):
        result = []
        for i, price in enumerate(prices):
            if np.isnan(price):
                try:
                    result.append(prices[i+1])
                except:
                    result.append(prices[i-1])
            else:
                result.append(price)
        return np.array(result)

    def converter(self,prices):
        plt.figure(clear=True)
        date = prices.index
        X = date
        y = prices
        #X = X.rename_axis("Date")
        y = y.rename_axis("Price")
        X = X.values.astype("datetime64[D]").astype(int) # a aproblem here
        X = pd.Series(X)
        type(y)
        type(X)
        X = X.values.reshape(-1,1)
        y = y.values.reshape(-1,1)
        lm = linear_model.LinearRegression()
        y = self.replace_nan(y)
        model = lm.fit(X,y)
        predictions = lm.predict(X)
        #print(predictions)
        linear_regressor = LinearRegression()
        linear_regressor.fit(X, y)
        Y_pred = linear_regressor.predict(X)
        """"plt.plot(X, Y_pred, y, color="red", )
        plt.show()"""
        plt.title(str(Decimal(float(Y_pred[-1]-Y_pred[0]))))
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.plot(date,y)
        plt.plot(X, Y_pred, color="red")
        plt.show()
        plt.figure(clear=True)
    
    def if_invested_10000_yen(self,stock_id):
        log_return = self.get_log_return_from_stock_id(stock_id)
        original_money = 10000.0
        returns = []
        for i,log_rtn in enumerate(log_return):
            if i == 0:
                pass 
            else:
                original_money *= (1+log_rtn)
                returns.append(original_money)
        print(original_money)
        plt.plot(log_return.index[1:],returns)
        plt.show()
        

if __name__ == "__main__":
    Log_process = Log_Return_Process()
    Log_process.examine_wholly("^N225")