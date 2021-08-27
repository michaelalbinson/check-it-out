from db.model.ACongressionalMember import ACongressionalMember
from db.SenateMemberCache import SenateMemberCache


class SenateMember(ACongressionalMember):
    SENATE_RANK = None
    SENATE_CLASS = None

    def __init__(self):
        pass

    def save(self):
        pass

    def get(self, _id):
        pass

    def as_dict(self):
        data = self.get_base_member_dict()
        data['senate_class'] = self.SENATE_CLASS
        data['state_rank'] = self.STATE_RANK
        return data

    def _from_db(self, db_row):
        self.set_common_member_fields(db_row)
        self.SENATE_CLASS = db_row["SENATE_CLASS"]
        self.STATE_RANK = db_row["STATE_RANK"]
        return self

    @staticmethod
    def get_all():
        all_structured_members = []
        all_members = SenateMemberCache().get_all()
        for member in all_members:
            all_structured_members.append(SenateMember.from_db(member).as_dict())
        return all_structured_members

    @staticmethod
    def from_db(db_object):
        sm = SenateMember()
        sm._from_db(db_object)
        return sm
