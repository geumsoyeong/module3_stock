import scrapy
from naverscraper.items import NaverscraperItem

class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ['finance.naver.com/sise/sise_quant.nhn?sosok=0']
    start_urls = ['http://finance.naver.com/sise/sise_quant.nhn?sosok=0']

    def parse(self, response):
        items = []
        ranks = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[1]/text()').extract()
        titles = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[2]/a/text()').extract()
        prices = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[3]/text()').extract()
        ratios_updowns = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[4]/img/@alt').extract()
        ratios = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[4]/span/text()').extract()
        lows = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[5]/span/text()').extract()
        volumes = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[6]/text()').extract()
        payments = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[7]/text()').extract()
        buys = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[8]/text()').extract()
        sells = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[9]/text()').extract()
        capitalizations = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[10]/text()').extract()
        pers = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[11]/text()').extract()
        roes = response.xpath('//*[@id="contentarea"]/div[3]/table/tr/td[12]/text()').extract()




        items = []
        for idx in range(len(titles)):
            item = NaverscraperItem()
            item['stock_rank'] = ranks[idx]
            item['title'] = titles[idx]
            item['price'] = prices[idx]
            item['ratio_updown'] = ratios_updowns[idx]
            item['ratio'] = ratios[idx].strip()
            item['low'] = lows[idx].strip()
            item['volume'] = volumes[idx]
            item['payment'] = payments[idx]
            item['buy'] = buys[idx]
            item['sell'] = sells[idx]
            item['capitalization'] = capitalizations[idx]
            item['per'] = pers[idx]
            item['roe'] = roes[idx]


            items.append(item)
            print(item)
        return items


