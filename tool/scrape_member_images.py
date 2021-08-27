from db.HouseMemberCache import HouseMemberCache
import requests
import os
import time

house_cache = HouseMemberCache()


def scrape_house_member_images():
    all_members = house_cache.get_all()

    for member in all_members:
        html = requests.get("https://www.congress.gov/img/member/" + str(member.get('ID')).lower() + ".jpg")
        object_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'client', 'static', 'assets',
                                   'members', member.get('FIRST_NAME').lower() + member.get('LAST_NAME').lower() +
                                    '.jpg')
        with open(object_path, 'wb') as handler:
            handler.write(html.content)
        print(member)
        time.sleep(1)


scrape_house_member_images()
