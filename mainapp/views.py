from django.shortcuts import render
from django.http import HttpResponse
from . tasks import *


# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse('Done')




from django.views.generic.edit import FormView
from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts
from django.contrib import messages
from django.shortcuts import redirect


class GenerateRandomUserView(FormView):
    template_name = 'core.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect("mainapp:generate")
    

