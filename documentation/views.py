from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from documentation.models import Project, Item


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'website', 'description', 'created_on', 'id']


class ViewAllProjects(APIView):
    @extend_schema(responses=ProjectSerializer(many=True))
    def get(self, request):
        """List all projects that you have access for"""
        return Response(ProjectSerializer(instance=Project.objects.all(), many=True).data)


class ItemSerializer(serializers.Serializer):
    added_by = serializers.CharField(label='E-mail of the adder')
    added_on = serializers.DateTimeField(label='Date of addition')
    title = serializers.CharField(label='Item title')
    importance = serializers.IntegerField(label='Relative importance, 1 is most important where 20 is least important')
    id = serializers.IntegerField(label='Item ID')


class ViewAllItems(APIView):
    @extend_schema(responses=ItemSerializer(many=True))
    def get(self, request, project_id: int):
        """List all items of a project"""
        result = []
        project = Project.objects.get(id=project_id)
        for item in Item.objects.filter(project=project).all():
            result.append({'id': item.id,
                           'importance': item.importance,
                           'title': item.title,
                           'added_on': item.added_on.isoformat(),
                           'added_by': item.added_by.email})
        return Response(result)
