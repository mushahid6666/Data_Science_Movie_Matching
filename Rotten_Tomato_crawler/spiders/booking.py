import scrapy
from scrapy.utils.response import open_in_browser
from tutorial.items import DmozItem
import logging

class DmozSpider(scrapy.Spider):
    name = "booking"
    allowed_domains = ["booking.com"]
    start_urls = [
        "http://www.booking.com/searchresults.html?sid=27b946f7943ffd668c16e63033944117;dcid=4;checkin_monthday=24&checkin_year_month=2015-9&checkout_monthday=25&checkout_year_month=2015-9&class_interval=1&csflt=%7B%7D&dest_id=-2090174&dest_type=city&dtdisc=0&group_adults=1&group_children=0&hlrd=0&hyb_red=0&inac=0&label_click=undef&nha_red=0&no_rooms=1&offset=0&offset_unavail=1&redirected_from_city=0&redirected_from_landmark=0&redirected_from_region=0&review_score_group=empty&room1=A&sb_price_type=total&score_min=0&si=ai%2Cco%2Cci%2Cre%2Cdi&src=index&ss=Bangalore&ss_all=0&ssb=empty&sshis=0&",
    ]

    def parse(self, response):
        #open_in_browser(response)
        #logging.warning(' item received for %s', response.url)
        for href in response.css("table.sr_item_legacy > tbody > tr > td > h3 >a::attr('href')"):
            if href:
                #url = response.urljoin(href.extract())
                logging.warning(' item received for %s', href.extract())
                url = response.url[0:22] + href.extract()
                temp = "?checkin_monthday=30&checkin_year_month=2015-9&checkout_monthday=1&checkout_year_month=2015-10&tab=&origin=hp&error_url=%2Fhotel%2Fin%2Foakwood-premier-prestige-bangalore.en-us.html%3Fsid%3D6203104057c44e344a60584419015a62%3Bdcid%3D4%3B&do_availability_check=on&dcid=4&sid=6203104057c44e344a60584419015a62#availability_target"
                url = url + temp
                logging.warning(' after merging %s', url)
                yield scrapy.Request(url, callback=self.parse_dir_contents)
            else:
                logging.warning('No item received for ', href)

    def parse_dir_contents(self, response):
        logging.warning('reponse.url before splitting %s', response.url)
        str1 = response.url.split("?")[0]
        str2 = str1.split("/")[-1]
        filename = 'booking/'+str1
        logging.warning('Final file name %s', filename)
        with open(filename, 'wb') as f:
            f.write(response.body)
