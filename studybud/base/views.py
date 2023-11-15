from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .serialzers import *
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,"base/home.html",context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
        context = {'room':room}
    return render(request,"base/room.html",context)


class ReactView(APIView):
    def get(self,request,format=None):
        rooms = Room.objects.all()
        serializer = ReactSerializer(rooms,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)