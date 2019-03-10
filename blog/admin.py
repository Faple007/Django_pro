from django.contrib import admin
from .models import Post,Tag

class TagInline(admin.TabularInline):
    model = Tag
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')
    fields  = ('title', 'text','published_date')
    search_fields = ('title',)
    inlines = [TagInline]  


 
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)