from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "articles_homework"
ws1.append(["제목", "링크", "신문사", "썸네일"])

url = f"https://search.naver.com/search.naver?&where=news&query=%EB%B0%A9%ED%83%84%EC%86%8C%EB%85%84%EB%8B%A8&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div > ul > li')
for article in articles:
    a_tag = article.select_one('dl > dt > a')

    title = a_tag.text
    url = a_tag['href']
    comp = article.select_one('dl > dd.txt_inline > span._sp_each_source').text.split(' ')[0].replace('언론사','')
    thumb = article.select_one('div > a > img')['src']
    ws1.append([title, url, comp, thumb])

driver.quit()
wb.save(filename='articles_homework.xlsx')
