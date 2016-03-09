from django.contrib import admin

from .models import Response,Scores,Sets,Correct_Answers
# Register your models here.

admin.site.register(Response)
admin.site.register(Scores)
admin.site.register(Sets)
admin.site.register(Correct_Answers)