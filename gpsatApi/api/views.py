from django.http import Http404
from .models import Evaluation
from .serializer import EvaluationSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Evaluations(APIView):
    def get(self, request, format=None):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EvaluationDetail(APIView):

    def get_object(self, pk):
        try:
            return Evaluation.objects.get(pk=pk)
        except Evaluation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        evaluations = self.get_object(pk)
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        evaluation = self.get_object(pk)
        serializer = EvaluationSerializer(evaluation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        evaluation = self.get_object(pk)
        evaluation.delete()
        return Response(status=status.HTTP_200_OK)
