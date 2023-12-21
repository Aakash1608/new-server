from django.shortcuts import render
from rest_framework.decorators import action
from .serializer import FileSerializer, UserSerializer
from .models import User, File
from django.http import response
from rest_framework.response import Response
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet, ModelViewSet
import os
import shutil
import pathlib

# Create your views here.


class FileViewset(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    @action(detail=False, methods=['POST'], url_path=r"upload/(?P<username>\w+)")
    def upload(self, request, username=None):
        if not request.FILES.get('file', False):
            return Response({"msg":"file key is missing in body"}, status=status.HTTP_400_BAD_REQUEST)
        
        file = request.FILES.getlist('file')[0]
        file_name = file.name
        try:
            userInstance = User.objects.get(username=username)

            # os.mknod(f'/data/{username}/')
            path = pathlib.Path().resolve()
            destination = open(path + f'/data/{username}/' + file.name, 'w')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            file_path = '/data/{username}/{file.name}'
            data = {
                "file_path": file_path,
                "file_name": file_name
            }
            serializer = FileSerializer(user=userInstance, data=data)
            if serializer.is_valid():
                serializer.save()

                return Response({"msg": "upload success"}, status=status.HTTP_200_OK)
            return Response({"msg": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except: 
            path = pathlib.Path().resolve()
            # os.mkdir(os.path.join(path, f"/data/"))
            os.makedirs(os.path.join(path, f"/../data/{username}/"))
            print(os.path.join(path, f"/data/{username}/", file.name))
            destination = open(os.path.join(path, f"/data/{username}/", file.name), 'w')
            newUser = UserSerializer(data={"username": username})

            if not newUser.is_valid():
                return Response({"msg": "something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            newUser.save()
            userInstance = User.objects.get(username=username)
            # os.mkdir(f'/data/{username}/')
            
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            file_path = '/data/{username}/{file.name}'
            data = {
                "file_path": file_path,
                "file_name": file_name
            }
            serializer = FileSerializer(user=userInstance, data=data)
            if serializer.is_valid():
                serializer.save()

                return Response({"msg": "upload success"}, status=status.HTTP_200_OK)
            



