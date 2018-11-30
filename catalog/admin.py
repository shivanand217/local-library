from django.contrib import admin

from catalog.models import *

# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)
admin.site.register(Genre)

class AuthorInline(admin.TabularInline):
    model = Book
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','date_of_birth','date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [AuthorInline]

# inlining of models to see Book Instance in admin Book page
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    # sectioning the detail view
    
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id'),
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
    
