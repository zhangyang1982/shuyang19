
import sys
from pymysql import *
import time,datetime

def readtxttomysql():
    # 1.从zhang.txt文本文件中批量读取数据并插入到数据库中
    file = open("D:\cqssc.txt", encoding='UTF-8')
    alldata = []
    for line in file.readlines():  # 读取历史开奖数据
        datassc = []
        curLine = line.strip().split("\n\t")
        string = str(curLine)
        string1 = string[2:13]  # 提取开奖期号
        string2 = string[13:23]  # 提取号码
        string2 = string2.replace(' ', '')  # 去除空格
        datassc.append(string1)
        datassc.append(string2)
        alldata.append(datassc)

    conn = connect(host='106.55.162.249', port=3306, user='root', password='SHuyang970819!$', database='music_db',
                   charset='utf8')
    cur = conn.cursor()
    for data in alldata:
        rq = str(data[0])
        hm = str(data[1])
        sql = """insert into cqssc (kjrq,kjhm) values (%s,%s) """  # 不要在格式化输入符s前面加双引号，否则插入到数据库中的字符也有引号
        cur.execute(sql, (rq, hm))
    conn.commit()
    cur.close()
    conn.close()
    print("Read Cqdata of TXT format To MySql")




if __name__ == '__main__':
    readtxttomysql()

