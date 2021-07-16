from django.contrib import admin
from .models import Type, Anime, Seiyu, Producer, Genre, Comment, Profile, Rating, Character


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Seiyu)
class SeiyuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    readonly_fields = ('user', 'score', 'anime')


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class CharacterInline(admin.StackedInline):
    model = Character
    extra = 1


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'url')
    list_display_links = ('title',)
    list_filter = ('type', 'producer', 'genres')
    search_fields = ('title', 'description')
    inlines = [CharacterInline, RatingInline, CommentInline]
    save_on_top = True


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'anime', 'url')
    list_display_links = ('name',)
    search_fields = ('name',)






