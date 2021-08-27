import requests
import os
import time


class LibraryOfCongress:
    def __init__(self):
        self.delay_interval = 100

    def get_images(self, first_name, last_name, middle_name=None):
        if middle_name is None:
            middle_name = ""
        html = requests.get("https://www.loc.gov/photos/?q=nancy_pelosi&fo=json")
        json_file = html.json()
        # print(json_file)
        # print(len(json_file.get('content').get('results')))
        img_url = json_file.get('content').get('results')[0].get('image_url')[-1]
        img_data = requests.get(img_url).content
        object_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'client', 'static', 'assets',
                                   'members',
                                   'nancypelosi.jpg')
        with open(object_path, 'wb') as handler:
            handler.write(img_data)


if __name__ == "__main__":
    l = LibraryOfCongress()
    l.get_images("a", "b", "c")