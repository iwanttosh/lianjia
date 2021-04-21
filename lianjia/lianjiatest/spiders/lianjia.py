import scrapy
from lianjiatest.items import LianjiatestItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    start_urls = [
        "https://bj.lianjia.com/ershoufang/pg2/"]

    def parse(self, response):

        hotellist = response.xpath("//div[@class='leftContent']")
        for hotel in hotellist:
            item = LianjiatestItem()
            hName = hotel.xpath("//ul/li/div/div/a/text()")
            hPrice = hotel.xpath("//ul/li/div/div/div[@class='totalPrice']/span/text()")
            hAdr = hotel.xpath("//ul/li/div//div[@class='positionInfo']/a/text()")
            hMsg = hotel.xpath("//ul/li/div/div/div[@class='houseInfo']/text()")
            for i in range(0, 30):
                if hName and hPrice and hAdr and hMsg:
                    item['hName'] = hName.extract()[i].strip()
                    item['hPrice'] = hPrice.extract()[i].strip()
                    item['hAdr'] = hAdr.extract()[i].strip()
                    item['hMsg'] = hMsg.extract()[i].strip()
                    yield item
            pass
        pass
        for i in range(1, 100):
            nextURL = "https://bj.lianjia.com/ershoufang/pg%s" % i

            yield scrapy.Request(url=nextURL, callback=self.parse, dont_filter=False)
