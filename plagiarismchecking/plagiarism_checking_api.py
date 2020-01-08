from rest_framework import serializers
from .models import PlagiarismCheckResponse
from .models import PlagiarismCheckRequest
from .models import PlagiarismCheckSave
from drf_writable_nested import WritableNestedModelSerializer
# serializer of request
class PlagiarismCheckRequestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlagiarismCheckRequest
        fields = ('id','sentence1','sentence2','language','method')

# serializer of response
class PlagiarismCheckResponseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlagiarismCheckResponse
        fields = ('success', 'err_msg', 'id', 'is_paraphrase')

# serializer to save to DB
class PlagiarismCheckSaveSerializer(WritableNestedModelSerializer):
    input = serializers.JSONField()
    output = serializers.JSONField()
    class Meta:
        model = PlagiarismCheckSave
        fields = ('id', 'input', 'output')

