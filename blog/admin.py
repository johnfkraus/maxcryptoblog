from django.contrib import admin

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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
