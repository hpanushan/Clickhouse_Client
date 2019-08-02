from ClickhouseClient import *


def main():
    obj = ClickhouseClient("10.0.0.30")
    #obj.createDatabase("twitter")
    #obj.createDatabase("facebook")
    print(obj.showDatabases())
    
if __name__ == '__main__':
    main()
    