from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TodoItem, Students
from .serializers import StudentSerializer

# Create your views here.


def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


class StudentsView(APIView):

    def get(self, request, id):
        result = Students.objects.get(id=id)
        if id:
            serializers = StudentSerializer(result)
            return Response({'success': 'success', "students": serializers.data}, status=200)

        result = Students.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status': 'success', "students": serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        result = Students.objects.get(id=id)
        serializer = StudentSerializer(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        result = get_object_or_404(Students, id=id)
        result.delete()
        return Response({"status": "success", "data": "Record Deleted"})
