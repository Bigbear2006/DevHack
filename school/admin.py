from django.contrib import admin

from .models import News, Teacher, Subject, Enrollment


admin.site.register(News)
admin.site.register(Teacher)
admin.site.register(Subject)


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'date')
    search_fields = ('subject__name__iregex', 'user__username__iregex')
    list_filter = ('subject__name',)
