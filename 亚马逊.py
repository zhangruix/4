import json

import MySQLdb
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}


data = {
    '__mk_zh_CN': '亚马逊网站',
'node': '2037295071',
'pf_rd_m': 'A1U5RCOVU0NYF2',
'pf_rd_s': 'merchandised-search-9',
'pf_rd_r': 'R94WFE0Y55N2XKK3GAGF',
'pf_rd_t': '101',
'pf_rd_p': '00837944-56c1-46ce-8a41-5322f11e452a',
'pf_rd_i': '1337022071'
}



def getURL(url):
    html = requests.get(url,headers=headers,data=data).text
    getDetail(html)

def getDetail(html):

    ele = etree.HTML(html)

    num = 0
    div = ele.xpath('//div[@class="a-section a-spacing-none"]')

    for i in div:
        # print(type(div),div)
        try:
            name = i.xpath('//a/span[@class="a-size-medium a-color-base a-text-normal"]/text()')[num]
        except:
            'unknown'
        # print(name)
        try:
            aurth = i.xpath('//div[@class="a-row a-size-base a-color-secondary"]/span[@class="a-size-base"][2]/text()')[num]
        except:
            'unknown'
        # print(aurth)

        conn = MySQLdb.connect(host='localhost', user='root', password='123456', port=3306, db='z-spider', charset='utf8')
        cursor = conn.cursor()

        # try:
        sql = 'INSERT INTO shu (name,aurth) VALUES (%s,%s)'
        cursor.execute(sql, (name, aurth))
        # except:
        #     'unknown'

        conn.commit()
        print('正在保存'+str(num))
        num += 1






if __name__ == '__main__':
    while 1:
        for page in range(1,400):
        # url = 'https://www.amazon.cn/s?bbn=1337022071&rh=n%3A116087071%2Cn%3A%21116089071%2Cn%3A%21116176071%2Cn%3A1337022071%2Cp_72%3A123699071&dc&fst=as%3Aoff&qid=1566560009&rnid=123698071&ref=lp_1337022071_nr_p_72_0'
            url = 'https://www.amazon.cn/s?i=digital-text&bbn=1337022071&rh=n%3A116087071%2Cn%3A116089071%2Cn%3A116176071%2Cn%3A1337022071%2Cp_72%3A123699071&dc&fst=as%3Aoff&qid=1566565434&rnid=123698071&ref=sr_pg_'+str(page)
            getURL(url)