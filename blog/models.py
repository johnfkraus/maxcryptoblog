import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars  # or truncatewords
import blog.encryption


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    ciphertext = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    password = models.CharField(null=True, max_length=45)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def update(self):
        self.last_update_date = timezone.now()
        self.save()

    def unpublish(self):
        self.published_date = None
        self.save()

    def is_encrypted(self):
        if self.text == 'None':
            return True
        else:
            return False

    def encrypt(self):
        self.ciphertext = blog.encryption.encrypt(self.password, self.text)
        self.text = 'None'

    def decrypt(self):
        self.text = blog.encryption.decrypt(self.password, self.ciphertext)
        self.ciphertext = 'None'

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Post._meta.fields]


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.User', related_name="users")
    # author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def short_text(self):
        return truncatechars(self.text, 100)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
