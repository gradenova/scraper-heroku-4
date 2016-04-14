# -*- coding:utf-8 -*-
import random
import time
import urllib
from bs4 import BeautifulSoup


class Scraper():
    def __init__(self):
        pass

    def scrape_list(self, params):
        self.__snooze()

        soup = self.__get_soup(params['base_url'])
        boxes = soup.select(params['box_selector'])

        result = [self.__extract_for_list(params, box) for box in boxes]

        return '\n'.join(result)

    def scrape_detail(self, params):
        soup = self.__get_soup(params['base_url'])
        boxes = soup.select(params['box_selector'])

        result = [self.__extract_for_detail(params, box) for box in boxes]

        return '\n'.join(result)

    def __get_page_count(self, raw_count):
        if raw_count > 10:
            return 10
        else:
            return raw_count

    def __snooze(self, wait_time=None):
        if(wait_time is not None):
            time.sleep(wait_time)
        else:
            time.sleep(random.randint(1, 3))

    def __get_soup(self, url):
        html = urllib.request.urlopen(url)

        return BeautifulSoup(html)

    def __extract_for_list(self, params, box):
        key = box.select(params['key_selector'])[0].get_text()

        items = []
        selectors = params['scrape_selector'].replace('\r', '').split('\n')
        for element in [box.select(selector) for selector in selectors]:
            items.append(element[0].get_text() if len(element) != 0 else '')

        return ','.join([key] + items)

    def __extract_for_detail(self, params, box):
        # self.__snooze(random.random())

        key = box.select(params['key_selector'])[0].get_text()
        link = box.select(params['link_selector'])[0].get('href')

        soup = self.__get_soup(link)

        items = []
        selectors = params['scrape_selector'].replace('\r', '').split('\n')
        elements = [soup.select(selector) for selector in selectors]
        for element in elements:
            items.append(element[0].get_text() if len(element) != 0 else '')

        return ','.join([key] + items)
