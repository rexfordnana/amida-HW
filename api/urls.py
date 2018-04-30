from django.urls import path
from .views import PatientView, UploadFileView
from django.views.generic import TemplateView
urlpatterns = [
    path('', UploadFileView.as_view(), name='upload'),
    path('api/sample', PatientView.as_view(), name='patient'),
    path('success', TemplateView.as_view(template_name ='api/success.html'), name='success')
]
