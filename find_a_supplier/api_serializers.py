from rest_framework import fields


class APIArticleSummariesSerializer(fields.ListField):

    @staticmethod
    def serialize_child(child, field):
        value = getattr(child, field.name)
        if value is None:
            return None
        serializer = field.serializer or fields.CharField()
        return serializer.to_representation(value)

    def to_representation(self, value):
        return [
            {
                field.name: self.serialize_child(child=item, field=field)
                for field in value.model.api_fields
            }
            for item in value.all()
        ]
