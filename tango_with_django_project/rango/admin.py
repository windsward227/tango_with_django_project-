from django.contrib import admin
from rango.models import Category, Page,UserProfile
# Register your models here.


#admin.site.register(Category)
#admin.site.register(Page)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'views', 'title']
    list_display = ( 'title','category','url')

admin.site.register(Page,PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)

