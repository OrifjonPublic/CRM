from django.contrib import admin
from user.models import User, Manager, Administrator, Teacher, Pupil



admin.site.register(User)
admin.site.register(Manager)
admin.site.register(Teacher)
admin.site.register(Pupil)

# Register your models here.
