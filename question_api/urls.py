from django.urls import path
from . import views
urlpatterns = [
    path('api/question',views.QuestionList.as_view(), name='question_list'),
    path('api/question/<int:pk>', views.ContactDetail.as_view(), name='contact_detail')
]