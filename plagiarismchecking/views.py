from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from plagiarismchecking.models import PlagiarismCheckRequest
from plagiarismchecking.models import PlagiarismCheckResponse
from plagiarismchecking.models import PlagiarismCheckSave
from plagiarismchecking.plagiarism_checking_api import PlagiarismCheckRequestSerializer
from plagiarismchecking.plagiarism_checking_api import PlagiarismCheckResponseSerializer
from plagiarismchecking.plagiarism_checking_api import PlagiarismCheckSaveSerializer
import json
from plagiarismchecking.plagiarism_bert import BertTextSimilarity
from plagiarismchecking.plagiarism_levenshtein import LevenshteinTextSimilarity

def PlagiarismCheckList(request):
    """
    List all plagiarism check, or create a new plagiarism check.
    """
    if request.method == 'GET':
        plargiarismchecks = PlagiarismCheckSave.objects.all()
        serializer = PlagiarismCheckSaveSerializer(plargiarismchecks, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
            request_json_data = json.loads(request.body.decode("utf-8"))
            request_serializer = PlagiarismCheckRequestSerializer(data=request_json_data)
            response_json_data = {}
            response_json_data['id'] = request_json_data['id']
            sentence1 = request_json_data['sentence1']
            sentence2 = request_json_data['sentence2']
            # get error messages request

            if not request_serializer.is_valid():
                response_json_data['success'] = False
                response_json_data['err_msg'] = "Error with request json"
                response_json_data['is_paraphrase'] = None
                response_serializer = PlagiarismCheckResponseSerializer(data=response_json_data)
                if response_serializer.is_valid():
                    return JsonResponse(response_serializer.data, status=400)

            # processing levenshtein
            if request_json_data['method'] == 'levenshtein':
                response_json_data['is_paraphrase'] = LevenshteinTextSimilarity(sentence1, sentence2)

            # processing bert
            if request_json_data['method'] == 'bert':
                response_json_data['is_paraphrase'] = BertTextSimilarity(sentence1, sentence2)

            # get data after processing to save to db and response
            response_json_data['success'] = True
            response_json_data['err_msg'] = 'None'
            response_serializer = PlagiarismCheckResponseSerializer(data=response_json_data)
            save_json_data = {}
            save_json_data['input'] = request_json_data
            save_json_data['output'] = response_json_data
            save_serializer = PlagiarismCheckSaveSerializer(data=save_json_data)
            save_serializer.is_valid(raise_exception=True)
            save_serializer.save()
            print(save_serializer)
            if response_serializer.is_valid():
                return JsonResponse(response_serializer.data, status=201)
            return JsonResponse(response_serializer.data, status=400)
