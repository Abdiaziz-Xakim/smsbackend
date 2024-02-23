# from django.contrib import admin
# from .models import Result

# # Register your models here.

# @admin.register(Result)
# class ResultAdmin(admin.ModelAdmin):
#     list_display = ('student', 'session', 'term', 'current_class', 'subject', 'test_score', 'exam_score', 'total_score', 'grade')
#     list_filter = ('session', 'term', 'current_class', 'subject')
#     search_fields = ('student__first_name', 'student__last_name', 'subject__name')
#     ordering = ('subject', 'student',)

# from django.contrib import admin
# from .models import Result, SubjectResult

# class SubjectResultInline(admin.TabularInline):
#     model = SubjectResult

# class ResultAdmin(admin.ModelAdmin):
#     inlines = [SubjectResultInline]

# admin.site.register(Result, ResultAdmin)

from django.contrib import admin
from .models import Result, SubjectResult

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'term', 'current_class')
    list_filter = ('session', 'term', 'current_class')

@admin.register(SubjectResult)
class SubjectResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'subject', 'test_score', 'exam_score', 'total_score', 'grade')
    list_filter = ('result__session', 'result__term', 'result__current_class')
    readonly_fields = ('total_score', 'grade')

    def total_score(self, obj):
        return obj.total_score()

    def grade(self, obj):
        return obj.grade()

    total_score.short_description = 'Total Score'
    grade.short_description = 'Grade'

