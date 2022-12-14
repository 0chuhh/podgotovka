from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.views import LoginView
from .models import product
import json

class Temp(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        self.request.session[0] = 'hello'

        context = super().get_context_data(**kwargs)
        context['parts'] = ['1','2','3']
        return context

class ProductView(ListView):

    def get(self, request, *args, **kwargs):
        try:
            count = self.request.GET['count']
        except:
            count = 0
        prds = product.objects.filter(count=count)

        response = [dict(map(lambda kv: (kv[0], str(kv[1])), model_to_dict(pr).items())) for pr in prds]
        return JsonResponse({'products': response})

    def post(self,request, *args, **kwards):
        try:
            count = self.request.POST['count']
            print(self.request.POST)
        except:
            count = 0
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            print(body['name'])

        newProd = product(count=count, name='hello')
        return JsonResponse({'OK':'OK'})

class Login(LoginView):
    template_name = 'login.html'
# Create your views here.
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'REG.html'