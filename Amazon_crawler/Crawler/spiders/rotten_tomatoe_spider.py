__author__ = 'mushahidalam'
import scrapy
import logging
from tutorial.items import RottanItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider
from scrapy import log


class RottanSpider(Spider):
    name = "rottan"
    allowed_domains = ["www.rottentomatoes.com"]
    # start_urls = [
    #   "http://www.amazon.com/s/ref=lp_2650363011_nr_p_n_feature_four_bro_1?fst=as%3Aoff&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A2650363011%2Cp_n_feature_four_browse-bin%3A2650442011&bbn=2650363011&ie=UTF8&qid=1444429468&rnid=2650439011",
    #]
    start_urls = ["file://127.0.0.1/Users/mushahidalam/784/CS784-webcrawler/tutorial/spiders/rottantomato.html"]

    def parse(self, response):
        str1 = "#movies-collection > div > div:nth-child("
        str2 = ") > div.movie_info > a::attr('href')"
        #movies-collection > div > div:nth-child(3540) > div.movie_info > a
        #movies-collection > div > div:nth-child(31)3541
        for i in range(31,32):
            str = str1+`i`+str2
            href = response.css(str)
            if href:
                url = href.extract()
                url = url[0]
                url = url.encode('utf-8')
                link = "http://www.rottentomatoes.com" + url
                yield scrapy.Request(link, callback=self.parse_each_element)

    def parse_each_element(self, response):
        str1 = response.url.split("/")[4]
        filename = 'rottan_html/'+str1+ '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        hxs = HtmlXPathSelector(response)

        try:
            title1 = hxs.xpath('//*[@id="movie-title"]/text()').extract()
            title2 = title1[0]
            title2 = title2.encode('utf-8')
            print(title2)
        except:
            print("no cast6 found")

        try:
            director1 = hxs.xpath('//*[@id="mainColumn"]/div[5]/div[2]/div/div/table/tr[3]/td[2]/a/span/text()').extract()
            director2 = director1[0]
            director2 = director2.encode('utf-8')
            print(director2)
        except:
            print("no cast6 found")

        try:
            rtime = hxs.xpath('//*[@id="mainColumn"]/div[5]/div[2]/div/div/table/tr/td/time/text()').extract()
            rtime1 = rtime[0]
            rtime1 = rtime1.encode('utf-8')
            print(rtime1)
        except:
            print("no cast6 found")

        try:
            year1 = hxs.xpath('//*[@id="heroImageContainer"]/div/h1/span/text()').extract()
            year2 = year1[0]
            year2 = year2.encode('utf-8')
            print(year2)
        except:
            print("no year found")

        try:
            rottan_rating1 = hxs.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()').extract()
            rottan_rating2 = rottan_rating1[0]
            rottan_rating2 = rottan_rating2.encode('utf-8')
            print(rottan_rating2)
        except:
            rottan_rating1 = hxs.xpath('//*[@id="all-critics-numbers"]/p[1]/text()').extract()
            rottan_rating2 = rottan_rating1[0]
            rottan_rating2 = rottan_rating2.encode('utf-8')
            print(rottan_rating2)

        try:
            cast11 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[1]/div/a/span/text()').extract()
            cast12 = cast11[0]
            cast12 = cast12.encode('utf-8')
            print(cast12)
        except:
            print("no cast6 found")


        try:
            cast21 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[2]/div/a/span/text()').extract()
            cast22 = cast21[0]
            cast22 = cast22.encode('utf-8')
            print(cast22)
        except:
            print("no cast2 found")

        try:
            cast31 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[3]/div/a/span/text()').extract()
            cast32 = cast31[0]
            cast32 = cast32.encode('utf-8')
            print(cast32)
        except:
            print("no cast3 found")

        try:
            cast41 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[4]/div/a/span/text()').extract()
            cast42 = cast41[0]
            cast42 = cast42.encode('utf-8')
            print(cast42)
        except:
            print("no cast4 found")

        try:
            cast51 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[5]/div/a/span/text()').extract()
            cast52 = cast51[0]
            cast52 = cast52.encode('utf-8')
            print(cast52)
        except:
            print("no cast5 found")

        try:
            cast61 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[6]/div/a/span/text()').extract()
            cast62 = cast61[0]
            cast62 = cast62.encode('utf-8')
            print(cast62)
        except:
            print("no cast6 found")

        try:
            audscore1 = hxs.xpath('//*[@id="scorePanel"]/div[2]/div[1]/a/div/div[2]/div[1]/span/text()').extract()
            audscore2 = audscore1[0]
            audscore2 = audscore2.encode('utf-8')
            print(audscore2)
        except:
            print("no aud found")

        try:
            review11 = hxs.xpath('//*[@id="reviews"]/div[5]/div[1]/div/div[2]/p/text()').extract()
            review12 = review11[0]
            review12 = review12.encode('utf-8')
            print(review12)
        except IndexError:
            review11 = hxs.xpath('//*[@id="reviews"]/div/div[1]/div/div[2]/p/text()').extract()
            review12 = review11[0]
            review12 = review12.encode('utf-8')
            print(review12)
        except:
            print("no reviews found")

        try:
            review21 = hxs.xpath('//*[@id="reviews"]/div[5]/div[1]/div/div[2]/p/text()').extract()
            review22 = review21[0]
            review22 = review22.encode('utf-8')
            print(review22)
        except:
            print('no 2nd review')

        try:
            review31 = hxs.xpath('//*[@id="reviews"]/div[5]/div[1]/div/div[2]/p/text()').extract()
            review32 = review31[0]
            review32 = review32.encode('utf-8')
            print(review32)
        except:
            print('no 3rd review')

        try:
            review41 = hxs.xpath('//*[@id="reviews"]/div[5]/div[1]/div/div[2]/p/text()').extract()
            review42 = review41[0]
            review42 = review42.encode('utf-8')
            print(review42)
        except:
            print('no 4th review')

        try:
            review51 = hxs.xpath('//*[@id="reviews"]/div[5]/div[1]/div/div[2]/p/text()').extract()
            review52 = review51[0]
            review52 = review52.encode('utf-8')
            print(review52)
        except:
            print("no 5th review")


        yield RottanItem(title=title2, time = rtime1, director= director2, year = year2, star1= cast12,
                         star2 = cast22, star3 = cast32, star4 = cast42, star5 = cast52, star6 = cast62,
                         tomatome_rating = rottan_rating2, audience_rating = audscore2, review1 = review12,
                         review2 = review22, review3 = review32, review4 = review42, review5 = review52,)