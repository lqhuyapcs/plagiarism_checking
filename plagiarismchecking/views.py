from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from plagiarismchecking.models import PlagiarismCheck
from plagiarismchecking.plagiarism_checking_api import PlagiarismCheckSerializer
import json
from plagiarismchecking.plagiarism_bert import BertTextSimilarity
from plagiarismchecking.plagiarism_levenshtein import LevenshteinTextSimilarity

def PlagiarismCheckList(request):
    """
    List all plagiarism check, or create a new plagiarism check.
    """
    if request.method == 'GET':
        plargiarismchecks = PlagiarismCheck.objects.all()
        serializer = PlagiarismCheckSerializer(plargiarismchecks, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        received_json_data = json.loads(request.body.decode("utf-8"))
        response_json_data = {}
        response_json_data['received_id'] = received_json_data['id']
        sentence1 = response_json_data['sentence1'] = received_json_data['sentence1']
        sentence2 = response_json_data['sentence2'] = received_json_data['sentence2']
        response_json_data['err_msg'] = 'none'
        response_json_data['language'] = received_json_data['language']
        response_json_data['method'] = received_json_data['method']
        # processing levenshtein
        if received_json_data['method'] == 'levenshtein':
            response_json_data['is_paraphrase'] = LevenshteinTextSimilarity(sentence1, sentence2)
        # processing bert
        if received_json_data['method'] == 'bert':
            response_json_data['is_paraphrase'] = BertTextSimilarity(sentence1, sentence2)
        # get data after processing to save to db and response
        serializer = PlagiarismCheckSerializer(data=response_json_data)
        if serializer.is_valid():
            serializer.save()
            serializer.data['success'] = 'true'
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
