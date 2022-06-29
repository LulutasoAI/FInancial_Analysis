from configparser import ConfigParser
import test_util
from test_util import check_result
class config_test():
    def __init__(self) -> None:
        self.config = ConfigParser()
        self.config.read("../config.ini")
        

    def test_config_read(self)->bool:
        try:
            symbol = self.config["moving_Average_Analysis"]["symbol_to_analyse"]
            print(symbol)
            return True
        except Exception as e:
            print(e)
            return False
        
    def main(self):
        result = []
        result.append(self.test_config_read())
        
        return check_result(result)