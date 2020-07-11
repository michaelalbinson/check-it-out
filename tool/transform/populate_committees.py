from api.propublica.PropublicaScraper import PropublicaScraper
from db.CommitteeCache import CommitteeCache

scraper = PropublicaScraper()
committee_cache = CommitteeCache()
chambers = ['house']

for chamber in chambers:
    for session in range(110, 117):
        result = PropublicaScraper.get_committees(session, chamber)
        print(result)
        exit()