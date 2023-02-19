import django.views.generic as gnr
from django.db.models import Q
from .models import Group, Lesson

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


class ScheduleView(gnr.ListView):
    model = Group
    template_name = 'schedule.html'
    context_object_name = 'schedule'

    def get_queryset(self):
        query = self.request.GET.get('q')
        group = Group.objects.get(Q(name__iregex=query))
        schedule = Lesson.objects.filter(group=group)
        sch = [schedule.filter(day=day) for day in days]
        return sch
