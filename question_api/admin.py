from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    readonly_fields=('id',)
    
admin.site.register(Question, QuestionAdmin)
