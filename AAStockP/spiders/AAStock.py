# -*- coding: utf-8 -*-
import scrapy
from AAStockP.items import AastockpItem
import time
import re


class AastockSpider(scrapy.Spider):
    name = 'AAStock'
    allowed_domains = ['aastocks.com/tc/mobile/News.aspx']
    offset = 1
    basicURL1 = 'http://aastocks.com/tc/mobile/News.aspx?NewsCategory=AAFN&NewsType=102&page='
    basicURL2 = '#newsanchor'
    basicURL3 = 'http://aastocks.com/tc/mobile/'
    start_urls = [basicURL1 + str(offset) + basicURL2]
    #start_urls = ['http://aastocks.com/tc/mobile/News.aspx?NewsCategory=AAFN&NewsType=102&page=1#newsanchor']
    

    def parse(self, response):
        #//*[@id="ctl00_cphContent_pNewsList"]/table/tbody[1]/tr/td[position()!= 3]/a[not(@id="AAFN")] Python中應去掉tbody
        link_items = response.xpath('//*[@id="ctl00_cphContent_pNewsList"]/table/tr/td[position()!= 3]/a[not(@id="AAFN")]/@href')       
        for link_item in link_items:
            r_link = link_item.extract()
            r_url = 'http://aastocks.com/tc/mobile/' + str(r_link) 
            print (r_url)
            yield scrapy.Request(r_url, callback = self.parse_items,dont_filter = True) 

        if self.offset < 12:
            self.offset += 1
            time.sleep(1)
            yield scrapy.Request(self.basicURL1+str(self.offset)+self.basicURL2, callback = self.parse,dont_filter = True)
    

    def parse_items(self, response):
        url_items = response.xpath('//*[@id="ctl00_cphContent_pNewsContent"]/table/tr[2]/td')
        for url_item in url_items:
            title = url_item.xpath('./span[1]/text()').extract()[0]
            item = AastockpItem()
            
            if title.find("升") != -1:
                title = url_item.xpath('./span[1]/text()').extract()[0]
                title_org = title[0:title.find('升')].strip('《大行報告').strip('》').strip('*')
                title_stock = re.findall('\((.*?)\)', title)
                title_price = re.findall('\d{1,3}.\d{1,2}元|\d{1,3}元', title)
                title_rating = re.findall('\「(.*?)\」', title)
                pTime1 = url_item.xpath('./text()').extract()[2]
                #pTime = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", pTime1) #搜索日期字段
                pTime = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", pTime1) #搜索日期字段
                content = url_item.xpath('./span[2]/text()').extract()
#                print(pTime[0])
#                print(title_org)
#                print(title_stock[0])
#                print(title_price[0])
#                print(title_rating[0])
#                print(content[1])
                item['pTime'] = pTime[0]
                item['title_org'] = title_org #if title_price else ''
                item['title_stock'] = title_stock[0] #if title_price else ''
                item['title_price'] = title_price[0] #if title_price else ''
                item['title_rating'] = title_rating[0] #if title_price else '' 
                item['title'] = title
                item['content'] = content[0]



            elif title.find("上調") != -1:
                title = url_item.xpath('./span[1]/text()').extract()[0]
                title_org = title[0:title.find('上調')].strip('《大行報告').strip('》').strip('*')
                title_stock = re.findall('\((.*?)\)', title)
                title_price = re.findall('\d{1,3}.\d{1,2}元|\d{1,3}元', title)
                title_rating = re.findall('\「(.*?)\」', title)
                pTime1 = url_item.xpath('./text()').extract()[2]
                #pTime = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", pTime1) #搜索日期字段
                pTime = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", pTime1) #搜索日期字段
                content = url_item.xpath('./span[2]/text()').extract()
 #               print(pTime[0])
 #               print(title_org)
 #               print(title_stock[0])
 #               print(title_price[0])
 #               print(title_rating[0])
 #               print(content)
                item['pTime'] = pTime[0]
                item['title_org'] = title_org #if title_price else ''
                item['title_stock'] = title_stock[0] #if title_price else ''
                item['title_price'] = title_price[0] #if title_price else ''
                item['title_rating'] = title_rating[0] #if title_price else '' 
                item['title'] = title
                item['content'] = content[0]
            

            elif title.find("首予") != -1:
                title = url_item.xpath('./span[1]/text()').extract()[0]
                title_org = title[0:title.find('首予')].strip('《大行報告').strip('》').strip('*')
                title_stock = re.findall('\((.*?)\)', title)
                title_price = re.findall('\d{1,3}元', title)
                title_rating = re.findall('\「(.*?)\」', title)
                pTime1 = url_item.xpath('./text()').extract()[2]
                #pTime = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", pTime1) #搜索日期字段
                pTime = re.findall(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})", pTime1)
                content = url_item.xpath('./span[2]/text()').extract()
#                print(pTime[0])
#                print(title_org)
#                print(title_stock[0])
#                print(title_price[0])
#                print(title_rating[0])
#                print(content)
                item['pTime'] = pTime[0]
                item['title_org'] = title_org #if title_price else ''
                item['title_stock'] = title_stock[0] #if title_price else ''
                item['title_price'] = title_price[0] #if title_price else ''
                item['title_rating'] = title_rating[0] #if title_price else '' 
                item['title'] = title
                item['content'] = content[0]

            yield item