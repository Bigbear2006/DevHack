from django.contrib.auth import get_user_model
import django.views.generic as gnr


class UserDetailView(gnr.DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user'


class UserUpdateView(gnr.UpdateView):
    model = get_user_model()
    template_name = 'settings.html'
    fields = ('phone', '_class', 'username')
