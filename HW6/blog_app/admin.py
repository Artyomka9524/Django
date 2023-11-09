from django.contrib import admin
from .models import Article, Author, Comment

@admin.action(description='опубликовать выбранные статьи')                       #создаем в админке действие на установке  в поле is_published=True - выбранные статьи опубликовать
def publish_all_articles(modeladmin, request, queryset):
    queryset.update(is_published=True)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']        #формирования списка полей
    ordering = ['title']              #ортировка 2-х уровневая по полям
    search_fields = ['title']               # поиск по полю
    list_filter = ['title', 'author']           #создание фильтра
    list_per_page = 5                       # вывод кол записей 5 на одной страниц

    fieldsets = [  # детализированное измсенение в админке полей
        (
            None,
            {
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'fields': ['publication_date', 'is_published'],
            },
        ),
    ]
    actions = [publish_all_articles]                    # передаем действие в админку

admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)


# Register your models here.
