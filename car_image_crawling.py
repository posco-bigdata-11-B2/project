import urllib
from urllib.request import urlopen

from bs4 import BeautifulSoup as bs
import requests

car_list = ['santa fe'] # 여기에 차 기종이름을 추가하거나 바꾸면 됩니다.


car_list = [car.replace(' ', '+') for car in car_list]

rank = 1
for r in car_list:
    url = f'https://www.google.com/search?q={r}&sxsrf=ALeKk01WuCtRoFmDGbZmzgJxG5b6wz8VrQ:1592534710712&' \
          'source=lnms&tbm=isch&sa=X&ved=2ahUKEwjEtuWN7ozqAhVbIIgKHcJdD9MQ_AUoAXoECBgQAw&biw=1920&bih=1089'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req)
    soup = bs(html, "html.parser")
    img = soup.find_all(class_='t0fcAb')
    print(img)
    print(type(img))
    print(len(img))

    n = 1  # 이미지 따로 저장하기 위한 카운트
    for i in img:
        print(n)
        imgUrl = i.attrs['src']
        with urlopen(imgUrl) as f:
            with open('aaaaa/car_train/santa_fe/' + str(rank) + '_' +
                      r.replace('+', '_') + str(n) + '.jpg', mode='wb') as h:  # w - write b - binary
                img = f.read()
                h.write(img)
        n += 1
        if n >= 30:
            break
    rank += 1
