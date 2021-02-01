from django.contrib import admin
from blogapp.models import Post, Comment

# Register your models here.
#customizing admin interface and these things are related to admin interface only not views or models
class PostAdmin(admin.ModelAdmin):
    list_display=['title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status']
    list_filter=('status','author', 'created', 'publish') #filter contents on basis of status and author and other mentioned field
    search_fields=('title', 'body')
    raw_id_fields=('author',) #based on ID value will be considered
    date_hierarchy='publish'
    prepopulated_fields={'slug': ('title',)} #slug will be populated on basis of title
    ordering=['status', 'publish']

class CommentAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'post', 'body', 'created', 'updated', 'active']
    list_filter=('post', 'created')
    search_fields=('name', 'email')

admin.site.register(Post, PostAdmin)
# will display all fields in form of objects--> admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
