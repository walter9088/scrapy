# -*- coding: utf-8 -*-
import urllib2
from collections import OrderedDict
import json

from bs4 import BeautifulSoup


def parserHtml(soup):
    info = soup.select_one("div.article-info")

    tables = soup.findAll('table')
    tab = tables[0]
    table_data = [[cell.text for cell in row.findAll("td")]
                  for row in tab.findAll("tr")]

    for row_num, row in enumerate(tab.findAll("tr")):
        for td_num, td in enumerate(row.findAll("td")):
            if 'colspan' in td.attrs and td.attrs['colspan'].isdigit():
                colspan = int(td.attrs['colspan'])
                for i in range(1, colspan):
                    table_data[row_num].insert(td_num, td.text)
            if 'rowspan' in td.attrs and td.attrs['rowspan'].isdigit():
                rowspan = int(td.attrs['rowspan'])
                for i in range(1, rowspan):
                    table_data[row_num+i].insert(td_num, td.text)
    for row in  table_data:
        print row[1].strip(),row[5].strip()



    #for tr in tab.findAll('tr'):
     #   pass
     #   print tr.getText()
        # for td in tr.findAll('td'):
        #     print td.getText(),
        # print

        # lists = []
    # for tag in tags:
    #     lines = tag.text.splitlines()
    #     for line in lines:
    #         strip_line = line.strip()
    #         if strip_line != u"":
    #             lists.append(strip_line.strip())
    #
    # for list in lists:
    #     print list


def getHtml(url):
    content = urllib2.urlopen(url)
    soup = BeautifulSoup(content)
    return soup



if __name__ == '__main__':
    soup = getHtml('http://www.jxsggzy.cn/web/jyxx/002006/002006001/20180209/b31b43f1-6919-46c7-83b0-4a7667b30e8b.html')
    tag = soup.select_one('tbody')
    parserHtml(soup)