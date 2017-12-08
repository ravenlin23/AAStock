# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
import mysql.connector


"""
class AastockpPipeline(object):



    def __init__(self):
        self.filename = open("AAStock.json", "wb")

    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False) + ",\n"
        self.filename.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.filename.close()
"""


class AastockpPipeline(object):
	def __init__(self):
		pass

	def process_item(self, item, spider):
		cnx = mysql.connector.connect(user='root', password='root',
                              host='10.231.30.152',
                              database='scrapy')

		cursor = cnx.cursor()
		pTime = '\'' + item['pTime'] +'\''
		title_org = '\'' + item['title_org'] +'\''
		title_stock = '\'' + item['title_stock'] +'\''
		title_price = '\'' + item['title_price'] +'\''
		title_rating = '\'' + item['title_rating'] +'\''
		title = '\'' + item['title'] +'\''
		content = '\'' + item['content'] +'\''


		add_data = ("INSERT INTO scrapy.aastock ""(pTime, ORG, Stock, Price, Rating, Title, Content) ""VALUES (%s, %s, %s, %s, %s, %s, %s)") % (pTime, title_org, title_stock, title_price, title_rating, title, content)



		cursor.execute(add_data)
		cnx.commit()
		cursor.close()
		cnx.close()





class Aastockp_clean(object):
	def __init__(self):
		pass

	def process_item(self, item, spider):
		pDate = '2017-12-07'
		print('AAAAAAAAAAAAAAAAAA'+str(item['pTime'][0:10]))
		print('AAAAAAAAAAAAAAAAAA'+pDate)
		if str(item['pTime'][0:10]) == pDate:
			return item
			print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
		else:
			raise DropItem
			
