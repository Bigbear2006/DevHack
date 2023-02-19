from django.contrib.auth import get_user_model
import django.views.generic as gnr
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserDetailView(LoginRequiredMixin, gnr.DetailView):
    login_url = 'http://127.0.0.1/accounts/google/login/'
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        user = self.get_object()
        context['accepted'] = user.enrollments.filter(accepted=True)
        context['not_accepted'] = user.enrollments.filter(accepted=False)
        return context


class UserUpdateView(UserPassesTestMixin, gnr.UpdateView):
    model = get_user_model()
    template_name = 'settings.html'
    fields = ('phone', 'clas_s', 'email', 'username')

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user
