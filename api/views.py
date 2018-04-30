from django.shortcuts import render

from django import views
from django.views.generic import FormView
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UploadFileForm
import time, os, json
from .jsonparser import JsonParser


class PatientView(views.View):
    with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "post.json"), 'r') as f:
        jsonfile = json.loads(f.read())

    def get(self, *args, **kwargs):

        metadata = {"generated": time.ctime()}
        response = {"data": self.jsonfile, "metadata": metadata}
        return JsonResponse(response, safe=False)


class UploadFileView(FormView):
    jsonParser = JsonParser()
    form_class = UploadFileForm
    template_name = 'api/index.html'
    success_url = 'api/success.html'

    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        if form.is_valid():
            self.jsonParser.parsse(file)
            return HttpResponseRedirect('success')
        else:
            return self.form_invalid(form)
