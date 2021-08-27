from db.HouseMemberCache import HouseMemberCache
from db.SenateMemberCache import SenateMemberCache
import requests
import os
import time

house_cache = HouseMemberCache()
senate_cache = SenateMemberCache()


def scrape_member_images(cache):
    all_members = cache.get_all()

    for member in all_members:
        html = requests.get("https://www.congress.gov/img/member/" + str(member.get('ID')).lower() + ".jpg")
        if html.status_code == 404:
            html = requests.get("https://www.congress.gov/img/member/" + str(member.get('ID')).lower() + "_200.jpg")
        object_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'client', 'static', 'assets',
                                   'members', member.get('FIRST_NAME').lower() + member.get('LAST_NAME').lower() +
                                    '.jpg')
        with open(object_path, 'wb') as handler:
            handler.write(html.content)
        print(member)
        time.sleep(1)


scrape_member_images(house_cache)
scrape_member_images(senate_cache)
