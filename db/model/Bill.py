from db.summarization import ExtractiveSummarizer
from db.model.ADBItem import ADBItem
from db.summarization import BillMetadataBuilder
from db.BillCache import BillCache
from db.model.util.DateUtil import DateUtil

"""
Class for interface with specific summarization
"""


class Bill(ADBItem):
	_author = ''
	_bill_url = ''  # propublica.org url -- bill_uri
	_committees = list()  # hold on to all associated committees in a list (using their committee codes)
	_congress_url = ''  # congress.gov url
	_history = dict()  # dict of dicts for easy json conversion:
	# {introduced: {date: <date>, success: <boolean>},
	#	house: {...},
	#	congress: {...},
	#	president {...},
	# 	law: {date: <date>, }}

	_number = ''
	_slug = ''
	_short_summary = None  # refers to the title
	_long_summary = None  # the actual summary (can be null)
	_sponsor_party = ''  # R, D or I
	_state = ''  # the easily human-readable version
	_title = ''  # refers to the short_title
	_short_title = ''  # refers to the short_title
	_session = None
	_introduced_date = None
	_vetoed = False
	_enacted = False
	_active = False

	def __init__(self):
		pass

	@staticmethod
	def search(string):
		result = BillMetadataBuilder.get_stripped_bag_of_words(string)
		all_words = set(result)
		all_words = ExtractiveSummarizer.stem_list(all_words)
		print(all_words)
		result = BillCache().get_top_bills_from_keywords(all_words)
		print(result)

		return [Bill().get(res[0]).as_short_form_dict() for res in result[:100]]

	def save(self):
		pass

	def get(self, _id):
		result = BillCache().get_bill_from_bill_id(_id)
		self._from_db(result)
		return self

	""" Helper Methods """

	def as_dict(self):
		return {
			'id': self._id,
			'state': self._state,
			'author': self._author,
			'title': self._title,
			'short_title': self._short_title,
			'summary': self._long_summary,
			'active': self._active
		}

	def as_short_form_dict(self):
		return {
			'id': self._id,
			'author': self._author,
			'introduced': DateUtil.ord_to_iso(self._introduced_date),
			'title': self._title,
			'short_title': self._short_title,
			'summary': self._long_summary,
			'active': self._active
		}

	def _from_db(self, db_object):
		self._title = db_object.get('TITLE')
		self._short_title = db_object.get('SHORT_TITLE')
		self._author = db_object.get('AUTHOR')
		self._id = db_object.get('ID')
		self._session = db_object.get("SESSION")
		self._long_summary = db_object.get("SUMMARY")
		self._bill_url = db_object.get("BILL_URL")
		self._introduced_date = db_object.get("INTRODUCED_DATE")
		self._latest_major_action = db_object.get("LATEST_MAJOR_ACTION")

		self._active = ADBItem.to_bool(db_object.get("ACTIVE"))
		self._enacted = ADBItem.to_bool(db_object.get("ENACTED"))
		self._vetoed = ADBItem.to_bool(db_object.get("VETOED"))

	@staticmethod
	def from_db(db_object):
		bill = Bill()
		bill._from_db(db_object)
		return bill
