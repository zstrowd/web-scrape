import requests
from bs4 import BeautifulSoup
import csv

def main():
    url = 'https://www.lightnovelhub.org/ranking-04061612/ratings'
    print(f"Scrapping: {url}")

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    novels = soup.find_all('li', class_='novel-item')

    with open("novels.csv", mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        writer.writerow(['Title', 'Status', 'Rating', 'Genre', 'Image URL'])

        # looping through each novel and exctracting data
        for novel_item in novels:

            novel_title = novel_item.find('h2', class_='title').find('a').get_text(strip=True)
            novel_rating = novel_item.find('strong').get_text(strip=True)
            novel_status = novel_item.find('span', class_="status").get_text(strip=True)
            novel_categories = [span.get_text() for span in novel_item.find('div', class_='scroll').find_all('span')]
            img_tag = novel_item.find('img')
            image_url = img_tag['data-src'] if 'data-src' in img_tag.attrs else img_tag['src']

            # writing data into csv file
            writer.writerow([novel_title, novel_status, novel_rating, novel_categories, image_url])

if __name__ == "__main__":
    main()