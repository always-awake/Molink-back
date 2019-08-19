from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import models


class Link(APIView):
	def post(self, request, format=None):
		user=request.user
		try:
			parent_folder = models.Folder.objects.get(id=request.data['parent_id'], creator=user)
		except models.Folder.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)
		serializer = serializers.LinkCreateSerializer(data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save(creator=user, parent=parent_folder)
			return Response(data=serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




