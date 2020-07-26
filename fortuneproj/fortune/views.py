from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserInfoForm


class Top(FormView):
    form_class = UserInfoForm
    template_name = 'fortune/top.html'
    success_url = reverse_lazy('fortune:top')
