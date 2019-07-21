from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class Scrap(object):

    def __init__(self, url):
        self.url = url
        self.page_soup = None
        self.data = []

    def scrap(self, ele, att):
        table = self.page_soup.find(ele, attrs=att)
        rows = table.findAll('tr')
        for row in rows:
            cols = row.findAll('td')
            cols = [ele.text.strip() for ele in cols]
            if '1\xa02' not in cols and cols not in self.data:
                self.data.append(cols)

    def read(self, ele, att):
        with webdriver.Firefox() as driver:
            driver.get(self.url)
            self.page_soup = Soup(driver.page_source, 'html.parser')
            self.scrap(ele, att)
            if len(self.data) <= 2:
                print("ERROR: No data on page")
                driver.close()
                return self.data
            try:
                driver.find_element_by_xpath('//*[@id="grdMWCG"]/tbody/tr[27]/td/a').click()
            except NoSuchElementException:
                print("ERROR: Unable to find second page")
                driver.close()
                return self.data
            self.page_soup = Soup(driver.page_source, 'html.parser')
            self.scrap(ele, att)
            driver.close()
        return self.data
