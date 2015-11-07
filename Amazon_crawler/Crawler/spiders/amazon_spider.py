import scrapy
from tutorial.items import DmozItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider
from scrapy import log

class DmozSpider(Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.com"]
    #start_urls = [
    #  "http://www.amazon.com/s/ref=lp_2650363011_nr_p_n_feature_four_bro_1?fst=as%3Aoff&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2Cp_n_feature_four_browse-bin%3A2650442011&bbn=2650363011&ie=UTF8&qid=1444429468&rnid=2650439011",
    #]
    start_urls = []

    str1="http://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2"
    str2="Cp_n_feature_four_browse-bin%3A2650442011&page="
    str3="&bbn=2650363011&ie=UTF8&qid=1444633370"
    for i in range(11,100) :
        str4=str1+str2+`i`+str3
        start_urls.append(str4)
        print str4

    def parse(self, response):
        for href in response.css("div.a-row.a-spacing-small > a::attr('href')"):
            if href:
                url = href.extract()
                log.msg("=========scraping this url======="+url,level=log.INFO)
                yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        str1 = response.url.split("/")[3]
        filename = 'output11/'+str1+ '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        hxs = HtmlXPathSelector(response)

        #extract the cost for new format
        HDcost1 = hxs.xpath('//*[@class="dv-button-inner"]/text()').extract()
        len1 = len(HDcost1)
        del HDcost1[0]
        for i in range(0,len1-1):
            var1 = HDcost1[i]
            var1 = var1.encode('utf-8')
            HDcost1[i] = var1

        #extract the title for new format
        title1 = hxs.xpath('//*[@id="aiv-content-title"]/text()').extract()
        len1 = len(title1)
        for i in range(0,len1):
            var1 = title1[i]
            var1 = var1.encode('utf-8')
            var1=var1.strip()
            title1[i]=var1
        title1 = filter(None,title1)


        #extract the release year for new format
        relyear= hxs.xpath('//*[@class="release-year"]/text()').extract()
        relyear1=relyear[0].encode('utf-8')
        relyear1=relyear1.strip()

        #extrcat the time for new format
        times = hxs.xpath('//*[@id="dv-dp-left-content"]/div[2]/div[2]/dl/dd[2]/text()').extract()
        time1 = times[0].strip()
        time1 = time1.encode('utf-8')

        #extract the director for new format
        dir1 = response.xpath('//*[@id="dv-center-features"]/div[1]/div/table/tr[2]/td/a/text()').extract()
        dir1 = dir1[0].encode('utf-8')
        dir1 = dir1.strip()

        #extract the starring actors
        actors = hxs.select('//*[@id="dv-dp-left-content"]/div[2]/div[2]/dl/dd[1]/text()').extract()
        actors = actors[0].encode('utf-8')
        actors = actors.strip()

        yield DmozItem(title=title1, time=time1, cost=HDcost1,year=relyear1,director=dir1,star=actors,)



