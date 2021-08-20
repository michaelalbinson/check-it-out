import json

from db.BillCache import BillCache
from db.model.Bill import Bill
from db.summarization.ExtractiveSummarizer import ExtractiveSummarizer


def bill_api_routes(app):
    @app.route("/api/bill/<string:bill_id>", methods=['GET'])
    def get_bill_api(bill_id):
        bill = Bill().get(bill_id)
        short_summary = ExtractiveSummarizer(bill.as_dict()).get_summary()
        dict_bill = bill.as_dict()
        dict_bill.update({'short_summary': short_summary})
        if bill is None:
            return json.dumps({'success': False})

        data = {
            'success': True,
            'data': dict_bill
        }

        return json.dumps(data)

    @app.route("/api/bill/search/", methods=['GET'])
    def get_all_bills():
        bills = Bill.get_all()
        if bills is None:
            return json.dumps({'success': False})

        return json.dumps({'success': True, 'data': bills})

    @app.route("/api/bill/search/<string:terms>", methods=['GET'])
    def get_bill_search(terms):
        bills = Bill.search(terms)
        if bills is None:
            return json.dumps({'success': False})

        return json.dumps({'success': True, 'data': bills})
