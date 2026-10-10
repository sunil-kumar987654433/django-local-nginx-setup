from django.shortcuts import render
from django.views import View
# Create your views here.


class HomeViewSet(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name="accounts/home.html", context=context)


class TextViewSet(View):
    def get(self, request):
        context = {
        }
        return render(request, template_name="accounts/test.html", context=context)