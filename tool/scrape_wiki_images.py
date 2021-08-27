from api.BioguideImageScraper import get_wiki_photo
from db.HouseMemberCache import HouseMemberCache
import requests
import os

member_cache = HouseMemberCache()
members = member_cache.get_all()
print(len(members))
for member in members:
    image_url = get_wiki_photo(member.get('FIRST_NAME'), member.get('MIDDLE_NAME'), member.get('LAST_NAME'))
    img_data = requests.get(image_url).content
    object_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),  '..', 'client', 'static', 'assets',
                               'members', member.get('FIRST_NAME').lower() + member.get('LAST_NAME').lower() + '.jpg')
    with open(object_path,'wb') as handler:
        handler.write(img_data)


