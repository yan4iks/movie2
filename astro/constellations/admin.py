from django.contrib import admin
from .models import Movie, Director, Genre, Actor

# admin.site.register(Movie)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

#поля, которые будут отображаться в списке объектов
    list_display = ('id', 'title', 'release_date', 'reting_imb', 'is_published')

#поля, которые будут ссылками на страницу редактирования
    list_display_links = ('id', 'title')

#поля, по которым можно будет фильтровать
    list_filter = ('is_published', 'release_date', 'country')

#поля, по которым будет работать поиск
    search_fields = ('title', 'description', 'director')

#автоматическое заполнение слога на основе другого поля
    prepopulated_fields = {"slug": ("title",)}

# Используем фильтр horizontal для поля actors
filter_horizontal = ('actors', )

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    