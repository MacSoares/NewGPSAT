from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Evaluation
from .serializer import EvaluationSerializer


from rest_framework import views, mixins, permissions, exceptions
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework import parsers, renderers



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def evaluations_list(request):
    if request.method == 'GET':
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return JSONResponse(serializer.data)
