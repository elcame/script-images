#importing the requests library
import requests
import urllib.request
import os

def save_image(filename, image_url):
    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(image_url, filename)


def main():
    # Number of pages
    n_pag = 2

    for i in range(n_pag):
        URL = f"https://reqres.in/api/users?page={i+1}"
        r = requests.get(url=URL)
        json = r.json()
        for user in json["data"]:
            print(user, end='\n')
            id = user['id']
            if id < 10:
                id = f'0{id}'
            id = str(id)
            first_name = user['first_name']
            last_name = user['last_name']

            if not os.path.exists('images/'):
                os.mkdir('images/')
            save_image(
                f'images/{id}-{first_name}{last_name}.jpg',
                user['avatar']
            )


if __name__ == '__main__':
    main()