import json

from db.BillCache import BillCache
from db.model.Bill import Bill


def bill_api_routes(app):
    @app.route("/api/bill/<string:bill_id>", methods=['GET'])
    def get_bill_api(bill_id):
        bill = BillCache().get_bill(bill_id)
        if bill is None:
            return json.dumps({'success': False})

        data = {
            'success': True,
            'data': Bill.from_db_object(bill).get_json()
        }

        return json.dumps(data)

    @app.route("/api/bill/search/<string:terms>", methods=['GET'])
    def get_bill_search(terms):
        bills = Bill.search(terms)
        if bills is None:
            return json.dumps({'success': False})

        data = {
            'success': True,
            'data': bills
        }

        return json.dumps(data)
