from rest_framework.serializers import Serializer, CharField, EmailField, URLField

class CallbackSerializer(Serializer):
    code = CharField()
