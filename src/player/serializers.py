from rest_framework import serializers


class SearchPlayersInOtherClansSerializer(serializers.Serializer):
    search = serializers.CharField(max_length=50, min_length=3)


