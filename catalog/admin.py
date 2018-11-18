from django.contrib import admin

# Register your models here.

from catalog.models import *

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
