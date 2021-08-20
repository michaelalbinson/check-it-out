from client.TemplateManager.TemplateManager import template_manager
from db.model.Bill import Bill


def bill_client_routes(app):
    @app.route("/summarization", methods=['GET'])
    def get_bills():
        return template_manager.get_template('bill.html')

    @app.route("/bill", methods=['GET'])
    def get_bill_null_id():
        return template_manager.get_template('bill_not_found.html')

    @app.route("/bill/", methods=['GET'])
    def get_bill_null_id_slash():
        return template_manager.get_template('bill_not_found.html')

    @app.route("/bill/<string:bill_id>", methods=['GET'])
    def get_bill(bill_id):
        print(bill_id)
        return template_manager.get_template('bill.html')

    @app.route("/bills", methods=['GET'])
    def get_bill_client_search():
        return template_manager.get_template('bills.html')
