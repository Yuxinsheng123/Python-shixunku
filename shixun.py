import requests
from bs4 import BeautifulSoup
import openpyxl

def fetch_movie_data(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies_list = []
    movies = soup.find_all('div', class_='item')

    for movie in movies:
        # 电影详情链接
        movie_detail_url = movie.find('a')['href']
        # 图片链接
        image_url = movie.find('img')['src']
        # 中文名和外国名
        title = movie.find('span', class_='title').contents
        chinese_title = title[0].strip()
        foreign_title = title[1].get_text().strip() if len(title) > 1 else ''
        # 评分
        rating = movie.find('span', class_='rating_num').get_text()
        # 评价数
        rating_num = movie.find('div', class_='star').findAll('span')[-1].contents[0].strip('人评价')
        # 概况
        summary = movie.find('span', class_='inq').contents[0] if movie.find('span', class_='inq') else ''
        # 相关信息
        info = movie.find('div', class_='bd').find('p').get_text().strip()

        movies_list.append({
            "movie_detail_url": movie_detail_url,
            "image_url": image_url,
            "chinese_title": chinese_title,
            "foreign_title": foreign_title,
            "rating": rating,
            "rating_num": rating_num,
            "summary": summary,
            "info": info,
        })

    return movies_list

def save_to_excel(movies, filename):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = 'Douban Top250 Movies'
    sheet.append(["电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息"])

    for movie in movies:
        sheet.append(list(movie.values()))

    wb.save(filename)

if __name__ == '__main__':
    top250_movies = []
    for start in range(0, 250, 25):
        url = f'https://movie.douban.com/top250?start={start}&filter='
        top250_movies.extend(fetch_movie_data(url))

    save_to_excel(top250_movies, 'Douban Top250 Movies2.xlsx')