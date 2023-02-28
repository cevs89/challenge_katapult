from datetime import datetime

import serpy


class BanksSerializer(serpy.Serializer):
    id = serpy.Field()
    uuid = serpy.Field()
    name_bank = serpy.Field()
    is_active = serpy.Field()
    created_at = serpy.MethodField()
    modified_at = serpy.MethodField()

    def get_created_at(self, obj):
        if obj.created_at is not None:
            return datetime.strftime(obj.created_at, "%Y-%m-%d %H:%M")

    def get_modified_at(self, obj):
        if obj.modified_at is not None:
            return datetime.strftime(obj.modified_at, "%Y-%m-%d %H:%M")
