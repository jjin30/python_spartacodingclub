from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("kakaotalk.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('하고','').replace('그냥','').replace('이제','').replace('샵검색','').replace('제가','').replace('오늘','').replace('그래서','').replace('진짜','').replace('너무','').replace('지금','').replace('저도','').replace('저는','').replace('근데','').replace('ㅋ','').replace('ㅠ','').replace('ㅜ','').replace('이모티콘\n','').replace('사진\n','').replace('삭제된 메시지입니다','')

# print(text)

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Windows/Fonts/NanumGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")
