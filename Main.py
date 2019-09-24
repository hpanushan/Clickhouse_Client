from ClickhouseClient import *


def main():
    obj = ClickhouseClient("10.0.0.30")
    print(obj.selectData('facebook','F_102699651071355_105714230769897_20190810_20190931'))
    
    
if __name__ == '__main__':
    main()
    