from datetime import datetime

import serpy
from django.utils.translation import gettext_lazy as _

MESSAGE_DEFAULT = _("Sin información en la tabla")


class ProvidersSerializer(serpy.Serializer):
    id = serpy.Field()
    uuid = serpy.Field()
    name_provider = serpy.Field()
    nit_provider = serpy.Field()
    name_contact_person = serpy.Field()
    number_contact_person = serpy.MethodField()
    is_active = serpy.Field()
    created_at = serpy.MethodField()
    modified_at = serpy.MethodField()
    bank = serpy.MethodField()

    def get_number_contact_person(self, obj):
        if obj.number_contact_person is None:
            return MESSAGE_DEFAULT

    def get_bank(self, obj):
        if obj.bank is not None:
            _account = obj.number_account_banking
            return {
                "name_bank": obj.bank.name_bank.upper(),
                "accoun_banking": _account if _account else MESSAGE_DEFAULT,
            }

    def get_created_at(self, obj):
        if obj.created_at is not None:
            return datetime.strftime(obj.created_at, "%Y-%m-%d %H:%M")

    def get_modified_at(self, obj):
        if obj.modified_at is not None:
            return datetime.strftime(obj.modified_at, "%Y-%m-%d %H:%M")
