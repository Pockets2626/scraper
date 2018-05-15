import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import sys
import zipfile
from selenium import webdriver


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)


def save_img(url_path, save_filename):
    p = requests.get(url_path)
    try:
        i = Image.open(BytesIO(p.content))
        i.save(save_filename)
    except OSError:
        print('DOne')
        make_zip(folder, zip_name)
        sys.exit()


def make_zip(directory, folder_name):
    with zipfile.ZipFile(folder_name + '.zip', mode='a') as zf:
        print('adding files')
        comic_zip = folder_name + '.zip'
        for file in os.listdir(directory):
            if file.endswith('jpg'):
                zf.write(file)
                os.remove(file)

        print('close')
        zf.close()
        base = os.path.splitext(comic_zip)[0]
        os.rename(comic_zip, base + ".cbz")

# add domain and comic link as well as destination folders


domain = ""
comic = ""  #enter path of specific full page comic here start with /reader
zip_name = comic.split('/')[-2]
print(zip_name)
browser = webdriver.Chrome()  #download driver.exe first
browser.get(domain + comic)  #navigate to the page
create_folder("" + zip_name)
folder = '' + zip_name
os.chdir(folder)

r = requests.get(domain + comic)
data = r.text
soup = BeautifulSoup(data, "html.parser")
images = soup.find_all('img')
for img in images:
    pic = img['src']
    print(pic)
    path = "" + pic
    filename = pic.split('/')[-1]
    print("^filename ",filename)
    page = filename.split('.')[0]
    print("page: ", page)
    save_img(path, filename)
make_zip(folder, zip_name)

browser.close()
