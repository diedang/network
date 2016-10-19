from django.contrib import admin

# Register your models here.
from models import Column, Article
#
# admin.register([Column, Article])
class ColumnAdmin(admin.ModelAdmin):
    list_diaplay = ('name','slug','intro')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date','update_time')

admin.site.register(Column,ColumnAdmin)
admin.site.register(Article,ArticleAdmin)