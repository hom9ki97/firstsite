from django.contrib import admin

from .models import AdvUser, Topic, HomeWork, Lessons, CodeExample, Language

admin.site.register(Topic)
admin.site.register(Lessons)
admin.site.register(HomeWork)
admin.site.register(AdvUser)
admin.site.register(CodeExample)
admin.site.register(Language)


# @admin.register(CodeExample)
# class CodeExampleAdmin(admin.ModelAdmin):
#     list_display = ('lesson', 'created_at')  # Поля, отображаемые в списке
#     list_filter = ('lesson', 'created_at')  # Фильтры в правой части админки
#     search_fields = ('lesson', 'description')  # Поля для поиска
#     readonly_fields = ('created_at',)
#
#
# class CodeExampleInline(admin.TabularInline):  # Или admin.StackedInline
#     model = CodeExample
#     extra = 1  # Количество пустых форм для добавления новых примеров кода


# @admin.register(Lessons)
# class LessonsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'topic', 'order')
#     inlines = [CodeExampleInline]
