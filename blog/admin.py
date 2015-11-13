from django.contrib import admin

from django.contrib.sites.models import Site

from .models import Post, Comment, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_encrypted')
    list_filter = ['published_date', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'author', 'post')
    list_filter = ['approved_comment', 'author', 'created_date']


class SiteAdmin(admin.ModelAdmin):
    """ ADDING the id to the displayed values """
    list_display = ('id', 'domain', 'name')
    search_fields = ('domain', 'name')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


admin.site.unregister(Site)
""" unregistering Site so we can re-reregister it with SiteAdmin; we customized SiteAdmin to add the id to the display """

admin.site.register(Site, SiteAdmin)
