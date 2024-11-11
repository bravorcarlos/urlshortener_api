from rest_framework import serializers
from .models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['url', 'code', 'created_at', 'updated_at', 'click_count']
        read_only_fields = ['code', 'click_count']