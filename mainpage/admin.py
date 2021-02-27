from django.contrib import admin
from mainpage.models import Notice

admin.site.register(Notice)

# @admin.register(Notice)
# class NoticeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'writer', 'content', 'pub_date')
