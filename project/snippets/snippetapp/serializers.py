from rest_framework import serializers
from snippetapp.models import Snippet,LANGUAGE_CHOICES,STYLE_CHOICES

from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,allow_blank=True,max_length=100)
    code = serialisers.CharField(style={'base_template':'testarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choice=LANGUAGE_CHOICES,default='python')
    style = serializers.ChoiceField(choice=STYLE_CHOICES,default='friendly')

    def create(self,validated_data):
    	"""
        创建
    	"""
    	return Snippet.objects.create(**validated_data)

    def uadate(self,instance,validated_data):
    	"""
        更新
    	"""

    	instance.title = validated_data.get('title',instance.title)
    	instance.code = validated_data.get('code',instance.code)
    	instance.linenos = validated_data.get('linenos',instance,linenos)
    	instance.language = validated_data.get('language',instance.language)
    	instance.style = validated_data.get('style',instance.style)
    	return  instance
    	
