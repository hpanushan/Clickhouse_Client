from ClickhouseClient import *

def main():
    obj = ClickhouseClient("10.0.0.22")

    obj.dropTable('tweets')
    print(obj.showTables())


if __name__ == '__main__':
    main()
    