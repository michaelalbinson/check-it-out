import json

from db.model.Bill import Bill


def bill_api_routes(app):
    @app.route("/api/bill/<string:bill_id>", methods=['GET'])
    def get_bill_api(bill_id):
        bill = Bill().get(bill_id)
        if bill is None:
            return json.dumps({'success': False})

        data = {
            'success': True,
            'data': bill.as_dict()
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
