from ClickhouseClient import *


def main():
    obj = ClickhouseClient("10.0.0.30")
    
    print(obj.showTables("facebook"))

    
if __name__ == '__main__':
    main()
    