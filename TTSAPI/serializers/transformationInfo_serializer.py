from rest_framework import serializers

from TTSAPI.models import TransformationInfo


class TransformationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransformationInfo()
        fields = "__all__"
