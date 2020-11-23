import dload

from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EC%A0%95%EA%B5%AD") # 여기에 URL을 넣어주세요
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumbnails:
    src = thumbnail['src']
    dload.save(src, f'imgs_homework/{i}.jpg')
    i += 1

driver.quit() # 끝나면 닫아주기