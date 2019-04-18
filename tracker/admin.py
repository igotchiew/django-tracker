from django.contrib import admin
from .models import Schedule, Workout


class WorkoutInline(admin.TabularInline):
    model = Workout


class ScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    inlines = [WorkoutInline]
    list_display = ('date',)

admin.site.register(Schedule, ScheduleAdmin)
