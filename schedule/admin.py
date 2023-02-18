from django.contrib import admin
from .models import Faculty, Course, Group, Schedule, Lesson


class InlineCourseAdmin(admin.StackedInline):
    model = Course


class InlineGroupAdmin(admin.StackedInline):
    model = Group


class InlineLessonAdmin(admin.StackedInline):
    model = Lesson


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    inlines = [InlineCourseAdmin]
    search_fields = ('name__iregex',)

    class Meta:
        model = Faculty


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [InlineGroupAdmin]
    list_display = ('number', 'faculty')
    list_filter = ('number', 'faculty')
    search_fields = ('faculty__name__iregex',)

    class Meta:
        model = Course


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [InlineLessonAdmin]
    list_display = ('name', 'course',)
    list_filter = ('name',)
    search_fields = ('name__iregex',)

    class Meta:
        model = Group


