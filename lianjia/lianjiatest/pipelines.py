# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql


class QiushibaiketestPipeline(object):

    def process_item(self, item, spider):
        print(" ")
        print(" ")
        print("=======管道输出数据=======")
        print(item['hName'], end="\n")
        print(item['hPrice'], end="\n")
        print(item['hAdr'], end="\n")
        print(item['hMsg'], end="\n")

        print("========================")

        hMsgr = item['hMsg']
        hDirection =('')
        hDegree = ('')
        hFloor =('')
        hYear = ('')
        hSystem = ('')
        hRoom = ""
        if '|' in hMsgr:
            salary = hMsgr.split('|')
            hDirection = hMsgr.split('|')[2]
            hDegree = hMsgr.split('|')[3]
            hFloor =hMsgr.split('|')[4]
            hYear = hMsgr.split('|')[5]
            hSystem = hMsgr.split('|')[6]
        hMsgs = item['hMsg']
        hSquare = ""

        hMsgm = item['hMsg']
        hMsgm = ""
        if '厅 |' in hMsgr:
            hRoom = hMsgr.split('厅 |')[0] + '厅'
            hSquare = hMsgr.split('厅 |')[1]

        else:
            hRoom = ""
            pass
        if '米 |' in hMsgs:
            hSquares = hSquare.split('米 |')[0] + '米'
            hMsgm = hSquare.split('米 |')[1]
        else:
            hSquare = ""

        # 建立连接
        connection = pymysql.connect(host='localhost',
                                     user='root', password='1234',
                                     database='db_2020_jobinfo', port=3306,
                                     charset='utf8')
        # connection.autocommit(True)
        # 获得游标
        cursor = connection.cursor()
        # 执行sql语句
        result = cursor.execute("insert into home (hName, hPrice, hAdr,hMsg,hRoom,hSquare,hDirection,hDegree,hFloor,hYear,hSystem)" \
                                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                [item['hName'], item['hPrice'], item['hAdr'], item['hMsg'], hRoom, hSquares,hDirection,hDegree,hFloor,hYear,hSystem])
        # result = cursor.execute("insert into home(hName,hPrice,hAdr,hMsg)" \
        #                         "values(%s,%s,%s,%s)", [item['hName'], item['hPrice'], item['hAdr'], item['hMsg']])

        # 提交到数据库
        connection.commit()
        if result > 0:
            print("写入成功")
        pass

        # 关闭连接
        connection.close()

        return item
