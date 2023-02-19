from django.contrib import admin

from .models import News, Teacher, Subject, Enrollment, Lesson


admin.site.register(News)
admin.site.register(Teacher)


class InlineLesson(admin.StackedInline):
    model = Lesson


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'date')
    search_fields = ('subject__name__iregex', 'user__username__iregex')
    list_filter = ('subject__name', 'accepted')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [InlineLesson]

    class Meta:
        model = Subject
