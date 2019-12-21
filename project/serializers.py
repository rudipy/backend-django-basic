# project/serializers.py
from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'medium_url',
            'description',
        )
        model = Project
