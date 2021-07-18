from django.contrib import admin
from django import forms
from django.utils.html import mark_safe
from .models import Type, Anime, Seiyu, Producer, Genre, Comment,\
    Profile, Rating, Character, AnimeScreenshots, Status

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.conf import settings


class AnimeAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Anime
        fields = '__all__'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_picture')
    readonly_fields = ('get_picture',)

    def get_picture(self, obj):
        if obj.picture:
            return mark_safe(f'<img src={obj.picture.url} width="50" height="60">')
        return mark_safe(f'<img src="{settings.STATIC_URL}nopic.png" width="50" height="60">')

    get_picture.short_description = 'Picture'


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name', 'url')


# @admin.register(Status)
# class StatusAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'url')
#     list_display_links = ('id', 'name',)
#     readonly_fields = ('anime_set', )


@admin.register(Seiyu)
class SeiyuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_picture', 'url')
    list_display_links = ('name',)
    readonly_fields = ('get_picture',)

    def get_picture(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60">')

    get_picture.short_description = 'Picture'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_picture', 'url')
    list_display_links = ('name',)
    readonly_fields = ('get_picture',)

    def get_picture(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="70" height="40">')

    get_picture.short_description = 'Picture'


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    readonly_fields = ('user', 'score', 'anime')


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    readonly_fields = ('user', )


class AnimeScreenshotInline(admin.TabularInline):
    model = AnimeScreenshots
    readonly_fields = ('get_picture', )
    extra = 1

    def get_picture(self, obj):
        return mark_safe(f'<img src={obj.screenshot.url} width="60" height="50">')

    get_picture.short_description = 'Screenshot'


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'year', 'get_poster', 'url')
    list_display_links = ('title',)
    list_filter = ('type', 'producer', 'genres', 'year')
    search_fields = ('title', 'description')
    readonly_fields = ('get_poster',)
    fieldsets = (
        (None, {
            'fields': ('title', ('type', 'status', 'producer'))
        }),
        (None, {
            'fields': (('poster', 'get_poster'), )
        }),
        (None, {
           'fields': (('year', 'release_date'), )
        }),
        (None, {
            'fields': ('description',)
        }),
        (None, {
            'fields': (('genres', 'characters'), )
        }),
        (None, {
            'fields': ('url', )
        }),
    )
    inlines = [AnimeScreenshotInline, RatingInline, CommentInline]
    form = AnimeAdminForm
    save_on_top = True
    save_as = True

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60">')

    get_poster.short_description = 'Poster'


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_picture', 'url')
    list_display_links = ('name',)
    search_fields = ('name',)
    readonly_fields = ('get_picture', )

    def get_picture(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="50" height="60">')

    get_picture.short_description = 'Picture'




