import Auto_Correlation_Ten
from check_correlation import Check_Correlation
from Log_Return_Process import Log_Return_Process
import Multiple_Linear_Regression_Analysis
import Moving_Average_Related
import sys 
import messages

class Financial_Analysis():
    def __init__(self) -> None:
        self.process_argument()
        self.symbol_to_analize = "TSLA" #for testing purposes I put TSLA here.

    def process_argument(self):
        try: 
            self.run_mode = int(sys.argv[1])
        except: 
            print(messages.No_argument_message)
            sys.exit()


    def auto_correlation_analysis(self):
        LR = Auto_Correlation_Ten.LRshift_N(self.symbol_to_analize)
        result = LR.estimation_dataprocessing_tomorrow()
        print("tomorrow's predicted price value of {}".format(LR.name),result)
        LR.visual_future_prediction() #I think it is quite accurate but need to be tested?

    def correlation_analysis(self):
        """
        todo: it needs to be examined.
        """
        checker = Check_Correlation()
        #checker.check_pure_correlation()
        print("devider")
        #checker.normalized_correlation()
        checker.Correlation_with_formula()
        #going to test correlationcompare.
        checker.test_output_correlation_change_throughout_time()
    
    def log_return_analysis(self):
        """
        We should make it one report instead of showing a graph after graphs.
        """
        Log_process = Log_Return_Process()
        Log_process.examine_wholly(self.symbol_to_analize)
        #if invested ~ 
    
    def multiple_linear_regression_analysis(self):
        """
        This works quite well.
        """
        start_dates = ["1980-01-01","2001-01-01","2010-01-01"]
        #start_dates = ["2015-01-01","2018-01-01","2010-01-01"]
        #symbols = ["NVO","SO","PLUG"]
        symbols = ["NEE","AAPL","V"]
        #symbols = ["NEE"]
        LR = Multiple_Linear_Regression_Analysis.LRANALYSIS(start_dates, symbols)
        LR.main()
        #LR.fig.show()
    
    def moving_average_analysis(self):
        ma = Moving_Average_Related.MA()
        ma.main(self.symbol_to_analize)
    
    def main(self):
        if self.run_mode == 1:
            self.auto_correlation_analysis()
        elif self.run_mode == 2:
            self.correlation_analysis()
        elif self.run_mode == 3:
            self.log_return_analysis()
        elif self.run_mode == 4:
            self.multiple_linear_regression_analysis()
        elif self.run_mode == 5:
            self.moving_average_analysis()
        else:
            print(messages.No_argument_message)
            sys.exit()

if __name__ == "__main__":
    financial_analysis = Financial_Analysis()
    financial_analysis.main()

        

