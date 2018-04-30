from django.shortcuts import render

from django import views
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, JsonResponse
from .forms import UploadFileForm
import time, os, json, codecs
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
    # form = UploadFileForm
    template_name = 'api/index.html'
    success_url = 'api/success.html'

    def post(self, request, *args, **kwargs):
        # form = self.get_form(self.form_class)
        form = UploadFileForm(request.POST, request.FILES)
        file = request.FILES['file']
        # utf8_file = file.read().decode('utf-8')
        if form.is_valid():
            self.jsonParser.parsse(file)
            return HttpResponseRedirect('success')
        else:
            return self.form_invalid(form)
