import django.views.generic as gnr
from .models import News, Teacher, Subject, Enrollment
from django.db.models import Q
from .models import Lesson

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


class NewsListView(gnr.ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'all_news'
    queryset = News.objects.all().order_by('-date')


class NewsDetailView(gnr.DetailView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


class TeacherListView(gnr.ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers'


class TeacherDetailView(gnr.DetailView):
    model = Teacher
    template_name = 'teacher_detail.html'
    context_object_name = 'teacher'


class SubjectListView(gnr.ListView):
    model = Subject
    template_name = 'subjects.html'
    context_object_name = 'subjects'


class SubjectDetailView(gnr.DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'subj'

    def post(self, request, *args, **kwargs):
        subj = self.get_object()
        user = request.user
        if 'enrollment' in request.POST:
            if user.is_authenticated:
                try:
                    Enrollment.objects.get(subject=subj, user=user)
                except Enrollment.DoesNotExist:
                    Enrollment.objects.create(subject=subj, user=user)

        if 'cancel' in request.POST:
            if user.is_authenticated:
                try:
                    Enrollment.objects.get(subject=subj, user=user).delete()
                except Enrollment.DoesNotExist:
                    pass

        return super().get(request, *args, **kwargs)


class ScheduleView(gnr.ListView):
    model = Lesson
    template_name = 'schedule.html'
    context_object_name = 'schedule'

    # def get_queryset(self):
    #     schedule = Lesson.objects.all()
    #     sch = [schedule.filter(day=day) for day in days]
    #     return sch
