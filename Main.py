from ClickhouseClient import *


def main():
    obj = ClickhouseClient("10.0.0.30")
    print(obj.selectData('twitter','T201989'))
    
    
if __name__ == '__main__':
    main()
    