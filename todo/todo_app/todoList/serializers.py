from rest_framework import serializers


class ItemSerializers(serializers.Serializer):
    name_user = serializers.CharField(max_length=30)
    title = serializers.CharField(max_length=100)
    text = serializers.CharField(max_length=500)
    date = serializers.DateTimeField('Deadline')
    done = serializers.BooleanField(default=False)