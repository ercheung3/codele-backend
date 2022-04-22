from rest_framework import serializers
from .models import Question

#Converts SQL to JSON
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','name','text','source','link','difficulty')