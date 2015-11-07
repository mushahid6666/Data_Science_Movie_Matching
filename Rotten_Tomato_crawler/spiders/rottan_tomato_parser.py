__author__ = 'mushahidalam'
import scrapy
import logging
from tutorial.items import RottanItem
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider
from stringfunctions import stringfix
import time

uniqueId=0
strfix = stringfix()
class RottanSpider(Spider):
    name = "rottan"
    allowed_domains = ["www.rottentomatoes.com"]
    start_urls = ["file://127.0.0.1/Users/mushahidalam/784/CS784-webcrawler/tutorial/spiders/rottantomato_drama.html"]

    i = 0;
#3541
    def parse(self, response):
        str1 = "#movies-collection > div > div:nth-child("
        str2 = ") > div.movie_info > a::attr('href')"
        for i in range(93, 3142):
            str = str1 + `i` + str2
            href = response.css(str)
            if href:
                url = href.extract()
                url = url[0]
                url = url.encode('utf-8')
                link = "http://www.rottentomatoes.com" + url
                i = i + 1;
                # if i%100==0:
                #     time.sleep(300)
                yield scrapy.Request(link, callback=self.parse_each_element)

    def parse_each_element(self, response):
        global strfix
        global uniqueId
        hxs = HtmlXPathSelector(response)
        try:
            title1 = hxs.xpath('//*[@id="movie-title"]/text()').extract()
            title2 = title1[0]
            title2 = title2.encode('utf-8')
        except:
            title2 = ''
            logging.error('no title found!!!!!!!!!!!!')

        try:
            #str1 = response.url.split("/")[4]
            str1 = title2
            str1 = strfix.removeallspaces(str1)
            str1 = strfix.findbraces(str1)
            str1 = strfix.findslashes(str1)
            str1 = strfix.removeallcolons(str1)
            filename = 'drama_rottan/' + str1 + '.html'
            with open(filename, 'wb') as f:
                f.write(response.body)
        except IOError:#//*[@id="movies-collection"]/div/div[3049]/div[2]/a
            logging.error("Folder not found, go to CS784-webcrawler/tutorial and run the crawler")

        try:
            director2 = hxs.xpath('//*[@id="mainColumn"]/div[5]/div[2]/div/div/table/tr[3]/td[2]/a/span/text()').extract()[0].encode('utf-8')
            #director2 = director1[0]
            #director2 = director2.encode('utf-8')
        except IndexError:
            try:#//*[@id="mainColumn"]/div[6]/div[2]/div/div/table/tbody/tr[3]/td[2]/a/span
                director2 = hxs.xpath('//*[@id="mainColumn"]/div[4]/div[2]/div/div/table/tr[3]/td[2]/a/span/text()').extract()[0].encode('utf-8')
            except IndexError:
                try:
                    director2 = hxs.xpath('//*[@id="mainColumn"]/div[3]/div[2]/div/div/table/tr[3]/td[2]/a/span/text()').extract()[0].encode('utf-8')
                except:
                    director2 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div[2]/div/div/table/tr[3]/td[2]/a/span/text()').extract()[0].encode('utf-8')
            except:
                director2 = ''
                logging.error("no director found" + title2)
        except:
            director2 = ''
            logging.error("no director found" + title2)
#//*[@id="mainColumn"]/div[6]/div[2]/div/div/table/tbody/tr[8]/td[2]/time
        try:
            year1 = hxs.xpath('//*[@id="heroImageContainer"]/div/h1/span/text()').extract()
            year2 = year1[0]
            year2 = year2.encode('utf-8')
            year2 = year2[2:]
            year2 = year2[:-1]
        except IndexError:
            try:
                year1 = hxs.xpath('//*[@id="heroImageContainer"]/a/h1/span/text()').extract()
                year2 = year1[0]
                year2 = year2.encode('utf-8')
                year2 = year2[2:]
                year2 = year2[:-1]
            except IndexError:
                year1 = hxs.xpath('//*[@id="movie-title"]/span/text()').extract()
                year2 = year1[0]
                year2 = year2.encode('utf-8')
                year2 = year2[2:]
                year2 = year2[:-1]
        except:
            year2 = ''
            logging.error("no year found" + title2)

        try:
            rottan_rating1 = hxs.xpath('//*[@id="tomato_meter_link"]/span[2]/span/text()').extract()
            rottan_rating2 = rottan_rating1[0]
            rottan_rating2 = rottan_rating2.encode('utf-8')
            logging.error(rottan_rating2)
        except:
            rottan_rating2 = '0'
            logging.error("Not rotten rating for " + title2)
        flag6=0
        flag7=0
        flag8=0
        flag9=0
        flag10=0
        try:#//*[@id="mainColumn"]/div[10]/div/div/div[1]/div/a/span
            cast11 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[1]/div/a/span/text()').extract()
            cast12 = cast11[0]
            cast12 = cast12.encode('utf-8')
            flag9 = 1
        except IndexError:
            try:
                cast11 = hxs.xpath('//*[@id="mainColumn"]/div[7]/div/div/div[1]/div/a/span/text()').extract()
                cast12 = cast11[0]
                cast12 = cast12.encode('utf-8')
                flag7=1
            except :
                try:
                    cast11 = hxs.xpath('//*[@id="mainColumn"]/div[8]/div/div/div[1]/div/a/span/text()').extract()
                    cast12 = cast11[0]
                    cast12 = cast12.encode('utf-8')
                    flag8=1
                except IndexError:
                    try:
                        cast11 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div/div/div[1]/div/a/span/text()').extract()
                        cast12 = cast11[0]
                        cast12 = cast12.encode('utf-8')
                    except:
                        cast11 = hxs.xpath('//*[@id="mainColumn"]/div[10]/div/div/div[1]/div/a/span/text()').extract()
                        cast12 = cast11[0]
                        cast12 = cast12.encode('utf-8')
                        logging.error("no cast1 found" + title2)
                        flag10=1
        except:
            cast12 = ''
            logging.error("no cast1 found" + title2)

        if flag10==1:
            try:
                cast21 = hxs.xpath('//*[@id="mainColumn"]/div[10]/div/div/div[2]/div/a/span/text()').extract()
                cast22 = cast21[0]
                cast22 = cast22.encode('utf-8')
            except:
                cast22 = ''
                logging.error("no cast2 found" + title2)

            try:
                cast31 = hxs.xpath('//*[@id="mainColumn"]/div[10]/div/div/div[3]/div/a/span/text()').extract()
                cast32 = cast31[0]
                cast32 = cast32.encode('utf-8')
            except:
                cast32 = ''
                logging.error("no cast3 found" + title2)

            try:
                cast41 = hxs.xpath('//*[@id="mainColumn"]/div[10]/div/div/div[4]/div/a/span/text()').extract()
                cast42 = cast41[0]
                cast42 = cast42.encode('utf-8')
            except:
                cast42 = ''
                logging.error("no cast4 found" + title2)

            try:
                cast51 = hxs.xpath('//*[@id="mainColumn"]/div[10]/div/div/div[5]/div/a/span/text()').extract()
                cast52 = cast51[0]
                cast52 = cast52.encode('utf-8')
            except:
                cast52 = ''
                logging.error("no cast5 found" + title2)

            try:
                cast61 = hxs.xpath('//*[@id="mainColumn"]/div[10]/div/div/div[6]/div/a/span/text()').extract()
                cast62 = cast61[0]
                cast62 = cast62.encode('utf-8')
            except:
                cast62 = ''
                logging.error("no cast6 found" + title2)
        elif flag9 == 1:
            try:
                cast21 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[2]/div/a/span/text()').extract()
                cast22 = cast21[0]
                cast22 = cast22.encode('utf-8')
            except:
                cast22 = ''
                logging.error("no cast2 found" + title2)

            try:
                cast31 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[3]/div/a/span/text()').extract()
                cast32 = cast31[0]
                cast32 = cast32.encode('utf-8')
            except:
                cast32 = ''
                logging.error("no cast3 found" + title2)

            try:
                cast41 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[4]/div/a/span/text()').extract()
                cast42 = cast41[0]
                cast42 = cast42.encode('utf-8')
            except:
                cast42 = ''
                logging.error("no cast4 found" + title2)

            try:
                cast51 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[5]/div/a/span/text()').extract()
                cast52 = cast51[0]
                cast52 = cast52.encode('utf-8')
            except:
                cast52 = ''
                logging.error("no cast5 found" + title2)

            try:
                cast61 = hxs.xpath('//*[@id="mainColumn"]/div[9]/div/div/div[6]/div/a/span/text()').extract()
                cast62 = cast61[0]
                cast62 = cast62.encode('utf-8')
            except:
                cast62 = ''
                logging.error("no cast6 found" + title2)
        elif flag7 ==1:
            try:
                cast21 = hxs.xpath('//*[@id="mainColumn"]/div[7]/div/div/div[2]/div/a/span/text()').extract()
                cast22 = cast21[0]
                cast22 = cast22.encode('utf-8')
            except:
                cast22 = ''
                logging.error("no cast2 found" + title2)

            try:
                cast31 = hxs.xpath('//*[@id="mainColumn"]/div[7]/div/div/div[3]/div/a/span/text()').extract()
                cast32 = cast31[0]
                cast32 = cast32.encode('utf-8')
            except:
                cast32 = ''
                logging.error("no cast3 found" + title2)

            try:
                cast41 = hxs.xpath('//*[@id="mainColumn"]/div[7]/div/div/div[4]/div/a/span/text()').extract()
                cast42 = cast41[0]
                cast42 = cast42.encode('utf-8')
            except:
                cast42 = ''
                logging.error("no cast4 found" + title2)

            try:
                cast51 = hxs.xpath('//*[@id="mainColumn"]/div[7]/div/div/div[5]/div/a/span/text()').extract()
                cast52 = cast51[0]
                cast52 = cast52.encode('utf-8')
            except:
                cast52 = ''
                logging.error("no cast5 found" + title2)

            try:
                cast61 = hxs.xpath('//*[@id="mainColumn"]/div[7]/div/div/div[6]/div/a/span/text()').extract()
                cast62 = cast61[0]
                cast62 = cast62.encode('utf-8')
            except:
                cast62 = ''
                logging.error("no cast6 found" + title2)
        elif flag8 == 1:
            try:
                cast21 = hxs.xpath('//*[@id="mainColumn"]/div[8]/div/div/div[2]/div/a/span/text()').extract()
                cast22 = cast21[0]
                cast22 = cast22.encode('utf-8')
            except:
                cast22 = ''
                logging.error("no cast2 found" + title2)

            try:
                cast31 = hxs.xpath('//*[@id="mainColumn"]/div[8]/div/div/div[3]/div/a/span/text()').extract()
                cast32 = cast31[0]
                cast32 = cast32.encode('utf-8')
            except:
                cast32 = ''
                logging.error("no cast3 found" + title2)

            try:
                cast41 = hxs.xpath('//*[@id="mainColumn"]/div[8]/div/div/div[4]/div/a/span/text()').extract()
                cast42 = cast41[0]
                cast42 = cast42.encode('utf-8')
            except:
                cast42 = ''
                logging.error("no cast4 found" + title2)

            try:
                cast51 = hxs.xpath('//*[@id="mainColumn"]/div[8]/div/div/div[5]/div/a/span/text()').extract()
                cast52 = cast51[0]
                cast52 = cast52.encode('utf-8')
            except:
                cast52 = ''
                logging.error("no cast5 found" + title2)

            try:
                cast61 = hxs.xpath('//*[@id="mainColumn"]/div[8]/div/div/div[6]/div/a/span/text()').extract()
                cast62 = cast61[0]
                cast62 = cast62.encode('utf-8')
            except:
                cast62 = ''
                logging.error("no cast6 found" + title2)
        else:
            try:
                cast21 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div/div/div[2]/div/a/span/text()').extract()
                cast22 = cast21[0]
                cast22 = cast22.encode('utf-8')
            except:
                cast22 = ''
                logging.error("no cast2 found" + title2)
            try:
                cast31 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div/div/div[3]/div/a/span/text()').extract()
                cast32 = cast31[0]
                cast32 = cast32.encode('utf-8')
            except:
                cast32 = ''
                logging.error("no cast3 found" + title2)

            try:
                cast41 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div/div/div[4]/div/a/span/text()').extract()
                cast42 = cast41[0]
                cast42 = cast42.encode('utf-8')
            except:
                cast42 = ''
                logging.error("no cast4 found" + title2)

            try:
                cast51 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div/div/div[5]/div/a/span/text()').extract()
                cast52 = cast51[0]
                cast52 = cast52.encode('utf-8')
            except:
                cast52 = ''
                logging.error("no cast5 found" + title2)

            try:
                cast61 = hxs.xpath('//*[@id="mainColumn"]/div[6]/div/div/div[6]/div/a/span/text()').extract()
                cast62 = cast61[0]
                cast62 = cast62.encode('utf-8')
            except:
                cast62 = ''
                logging.error("no cast6 found" + title2)

# //*[@id="mainColumn"]/div[7]/div/div/div[1]/div/a/span
# //*[@id="mainColumn"]/div[4]/div[2]/div/div/table/tbody/tr[6]/td[2]/time
#//*[@id="mainColumn"]/div[6]/div[2]/div/div/table/tbody/tr[8]/td[2]/time
        if flag7==1:
            try:
                rtime = hxs.xpath('//*[@id="mainColumn"]/div[3]/div[2]/div/div/table/tr/td/time/text()').extract()
                rtime1 = rtime[0]
                rtime1 = rtime1.encode('utf-8')
            except:
                rtime1 = ''
                logging.error("no rtime found" + title2)
        elif flag8==1:
            try:
                rtime = hxs.xpath('//*[@id="mainColumn"]/div[4]/div[2]/div/div/table/tr/td/time/text()').extract()
                rtime1 = rtime[0]
                rtime1 = rtime1.encode('utf-8')
            except IndexError:
                rtime = hxs.xpath('//*[@id="mainColumn"]/div[5]/div[2]/div/div/table/tr/td/time/text()').extract()
                rtime1 = rtime[0]
                rtime1 = rtime1.encode('utf-8')
            except:
                rtime1 = ''
                logging.error("no rtime found" + title2)
        elif flag9==1 :
            try:
                rtime = hxs.xpath('//*[@id="mainColumn"]/div[5]/div[2]/div/div/table/tr/td/time/text()').extract()
                rtime1 = rtime[0]
                rtime1 = rtime1.encode('utf-8')
            except:
                rtime1 = ''
                logging.error("no rtime found" + title2)
        elif flag10==1 :
            try:#//*[@id="mainColumn"]/div[6]/div[2]/div/div/table/tbody/tr[8]/td[2]/time
                rtime = hxs.xpath('//*[@id="mainColumn"]/div[6]/div[2]/div/div/table/tr/td/time/text()').extract()
                rtime1 = rtime[0]
                rtime1 = rtime1.encode('utf-8')
            except:
                rtime1 = ''
                logging.error("no rtime found" + title2)
        else:
            try:
                rtime = hxs.xpath('//*[@id="mainColumn"]/div[2]/div[2]/div/div/table/tr/td/time/text()').extract()
                rtime1 = rtime[0]
                rtime1 = rtime1.encode('utf-8')
            except:
                rtime1 = ''
                logging.error("no rtime found" + title2)

        try:
            audscore1 = hxs.xpath('//*[@id="scorePanel"]/div[2]/div[1]/a/div/div[2]/div[1]/span/text()').extract()
            audscore2 = audscore1[0]
            audscore2 = audscore2.encode('utf-8')
        except:
            audscore2 = '0'
            logging.error("no aud found" + title2)

        try:
            review11 = hxs.xpath('//*[@id="reviews"]/div[1]/div[1]/div/div[2]/p/text()').extract()
            review12 = review11[0]
            review12 = review12.encode('utf-8')
        except IndexError:
            try:
                review11 = hxs.xpath('//*[@id="reviews"]/div/div[1]/div/div[2]/p/text()').extract()
                assert isinstance(review11, object)
                review12 = review11[0]
                review12 = review12.encode('utf-8')
            except:
                review12 = ''
                logging.error("no reviews found" + title2)
        except:
            review12 = ''
            logging.error("no reviews found" + title2)

        try:
            review21 = hxs.xpath('//*[@id="reviews"]/div[2]/div[1]/div/div[2]/p/text()').extract()
            review22 = review21[0]
            review22 = review22.encode('utf-8')
        except:
            review22 = ''
            logging.error('no 2nd review' + title2)

        try:
            review31 = hxs.xpath('//*[@id="reviews"]/div[3]/div[1]/div/div[2]/p/text()').extract()
            review32 = review31[0]
            review32 = review32.encode('utf-8')
        except:
            review32 = ''
            logging.error('no 3rd review' + title2)

        try:
            review41 = hxs.xpath('//*[@id="reviews"]/div[4]/div[1]/div/div[2]/p/text()').extract()
            review42 = review41[0]
            review42 = review42.encode('utf-8')
        except:
            review42 = ''
            logging.error('no 4th review' + title2)

        try:
            review51 = hxs.xpath('//*[@id="reviews"]/div[5]/div[1]/div/div[2]/p/text()').extract()
            review52 = review51[0]
            review52 = review52.encode('utf-8')
        except:
            review52 = ''
            logging.error("no 5th review" + title2)

        title2 = strfix.findcomma(title2.strip())
        rtime1 = strfix.findcomma(rtime1.strip())
        director2 = strfix.findcomma(director2.strip())
        year2 = strfix.findcomma(year2.strip())
        cast12 = strfix.findcomma(cast12.strip())
        cast22 = strfix.findcomma(cast22.strip())
        cast32 = strfix.findcomma(cast32.strip())
        cast42 = strfix.findcomma(cast42.strip())
        cast52 = strfix.findcomma(cast52.strip())
        cast62 = strfix.findcomma(cast62.strip())
        rottan_rating2 = strfix.findcomma(rottan_rating2.strip())
        audscore2 = strfix.findcomma(audscore2.strip())
        review12 = review12.strip()
        review22 = review22.strip()
        review32 = review32.strip()
        review42 = review42.strip()
        review52 = review52.strip()
        uniqueId +=1
        yield RottanItem(id=uniqueId, title=title2, time=rtime1, director=director2, year=year2, star1=cast12,
                         star2=cast22, star3=cast32, star4=cast42, star5=cast52, star6=cast62,
                         tomatome_rating=rottan_rating2, audience_rating=audscore2, review1=review12,
                         review2=review22, review3=review32, review4=review42, review5=review52, )
