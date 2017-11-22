from api.models import Evaluation
from rest_framework_mongoengine import serializers


class EvaluationSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Evaluation
        fields = ('__all__')
