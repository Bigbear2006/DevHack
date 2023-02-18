import django.views.generic as gnr
from django.db.models import Q

from .models import Group, Schedule, Lesson


class ScheduleView(gnr.ListView):
    model = Group
    template_name = 'schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        query = self.request.GET.get('q')
        group = Group.objects.get(Q(name__iregex=query))
        schedule = Lesson.objects.filter(group=group)
        return schedule
