import os
import requests
from bs4 import BeautifulSoup


class ImageCracker:
    def __init__(self, content_base_url, image_base_url, base_file_path=None):
        self.CONTENT_BASE_URL = content_base_url
        self.IMAGE_BASE_URL = image_base_url
        self.BASE_FILE_PATH = base_file_path
        self.soup = None
        self.links = None

    def get_html_content(self):
        html_content = requests.get(self.CONTENT_BASE_URL).text
        return html_content

    def make_soup(self):
        html_content = self.get_html_content()
        self.soup = BeautifulSoup(html_content, 'html.parser')

    def get_image_links(self, img_type):
        links = []
        for image in self.soup.find_all('img'):
            link = image.get(img_type)
            if link is not None:
                links.append(link)
        if not links:
            raise Exception('No images to download.')
        self.links = links

    def make_dirs_and_download_images(self, external):
        for link in self.links:
            if self.BASE_FILE_PATH:
                try:
                    t = link.split('/')
                    t.pop()
                    if external:
                        del t[0:3]
                    dir_name = '/'.join(t)
                    complete_path = self.BASE_FILE_PATH + dir_name + '/'
                    if not os.path.exists(complete_path):
                        print(f'Creating directory {complete_path}')
                        os.makedirs(complete_path)
                except Exception:
                    print('Cannot make directories. Please check permissions')
                    raise
            try:
                if external:
                    print('Downloading')
                    bytes_content = requests.get(link).content
                else:
                    print(f'Downloading {self.IMAGE_BASE_URL + link}')
                    bytes_content = requests.get(self.IMAGE_BASE_URL + link).content
                file_name = link.split('/').pop()
                if self.BASE_FILE_PATH:
                    with open(complete_path + file_name, 'wb') as f:
                        f.write(bytes_content)
                else:
                    with open(file_name, 'wb') as f:
                        f.write(bytes_content)
            except Exception:
                print("Error in downloading images.")
                raise

    def get_images(self, img_type='src', external=False):
        self.make_soup()
        if img_type not in ['src', 'data-src']:
            raise Exception('Please use either src or data-src.')
        else:
            self.get_image_links(img_type)
        self.make_dirs_and_download_images(external)

