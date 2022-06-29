from read_config_test import config_test
from test_util import check_result
class test_main():
    def __init__(self) -> None:
        pass 

    def main(self):
        config_test().main()
    
if __name__ == "__main__":
    result = []
    result.append(test_main().main())
    
    if check_result(result):
        print("all tests passed")
    else:
        print("fail")
    
