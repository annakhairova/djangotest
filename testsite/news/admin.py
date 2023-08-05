from django.contrib import admin

# Register your models here.

from .models import News, Category

class NewsAdmin(admin.ModelAdmin):      # указываем, что это подкласс
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')      #что публиковать в таблице админки
    list_display_links = ('id', 'title')            # какие поля должны быть ссылками
    search_fields = ('title', 'content')          # поля, по которым можно осуществлять поиск (появляется кнопочка поиска по таблице)
    list_editable = ('is_published',)      # указываем, какие поля мы можем редактировать прямо из списка
    list_filter = ('is_published', 'category')        # указываем, по каким полям мы хотим фильтровать

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)       # регистрация модели, а затем класс, который ее настроил
admin.site.register(Category, CategoryAdmin)
