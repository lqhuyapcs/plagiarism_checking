from rest_framework import serializers
from .models import PlagiarismCheck

class PlagiarismCheckSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PlagiarismCheck
        fields = ('received_id','sentence1', 'sentence2', 'err_msg', 'is_paraphrase', 'language', 'method')