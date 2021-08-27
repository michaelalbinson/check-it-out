import json
import requests
import os
from flask import request

from db.HouseMemberCache import HouseMemberCache
from db.SenateMemberCache import SenateMemberCache
from db.model.SenateMember import SenateMember
from db.model.HouseMember import HouseMember


def member_api_routes(app):
    @app.route("/api/member/<string:member_id>", methods=['GET'])
    def get_member_api(member_id):
        out_data = None
        house_member = HouseMemberCache().get_house_member_by_id(member_id)
        if house_member is not None:
            out_data = HouseMember.from_db(house_member).as_dict()
        else:
            senate_member = SenateMemberCache().get_senate_member_by_id(member_id)
            if senate_member is not None:
                out_data = SenateMember.from_db(senate_member).as_dict()
        print(out_data)

        object_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'client', 'static', 'assets',
                                   'members', out_data.get('first_name').lower() + out_data.get('last_name').lower() +
                                   '.jpg')
        if not os.path.isfile(object_path):
            html = requests.get("https://www.congress.gov/img/member/" + str(out_data.get('id')).lower() + ".jpg")
            if html.status_code == 404:
                html = requests.get("https://www.congress.gov/img/member/" + str(out_data.get('id')).lower()
                                    + "_200.jpg")
            with open(object_path, 'wb') as handler:
                handler.write(html.content)

        if out_data is None:
            return json.dumps({'success': False})

        return json.dumps(
            {'success': True, 'data': out_data}
        )

    @app.route("/api/members", methods=['GET'])
    def get_all_members_api():
        page_num = request.args.get('page')
        if page_num is None:
            return json.dumps({'success': True, 'data': HouseMember.get_all() + SenateMember.get_all()})

        return json.dumps({'success': False, 'data': []})
