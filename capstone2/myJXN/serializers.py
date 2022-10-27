# apis/serializers.py
from multiprocessing import Event
from rest_framework import serializers
from .models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Entry