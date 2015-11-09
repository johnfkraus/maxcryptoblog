from django.contrib import admin

from .models import Post, Comment, Question, Choice

admin.site.register(Comment)

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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Post, PostAdmin)
