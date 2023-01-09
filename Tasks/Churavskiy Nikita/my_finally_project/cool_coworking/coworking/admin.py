from django.contrib import admin
from .models import*
from django.utils.safestring import mark_safe

class coworkingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create','content','get_html_photo','is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'photo', 'get_html_photo', 'time_create')
    readonly_fields = ('time_create','get_html_photo')


    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_html_photo.short_description = 'Фото'

admin.site.register(coworking, coworkingAdmin)


class locationAdmin(admin.ModelAdmin):
    list_display = ('street', 'num', 'number','content',)
    search_fields = ('street', 'num')

admin.site.register(location, locationAdmin)


class citiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'photo', 'slug', 'content','id')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(cities, citiesAdmin)


class AddpageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'num', 'email', 'time_update', 'content','cat_id')
    search_fields = ('title',)

admin.site.register(Addpage, AddpageAdmin)


class AboutBelarusAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'content', 'get_html_photo','time_update')
    search_fields = ('title',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_html_photo.short_description = 'Фото'


admin.site.register(AboutBelarus, AboutBelarusAdmin)


admin.site.site_title = 'Админ-панель сайта о Коворкинге'
admin.site.site_header = 'Админ-панель сайта о Коворкинге'





