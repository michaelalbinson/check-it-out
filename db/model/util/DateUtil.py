from datetime import date


class DateUtil:
	@staticmethod
	def ord_to_iso(_date):
		return date.fromordinal(_date).isoformat()
