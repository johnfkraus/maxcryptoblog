import datetime
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import truncatechars  # or truncatewords
import blog.encryption
import blog.blog_mail_sender
import allauthdemo
from allauthdemo import settings
# from django.contrib.auth import get_user_model as user_model
# User = user_model()


class Post(models.Model):
    author = models.ForeignKey('allauthdemo_auth.DemoUser')
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    ciphertext = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    password = models.CharField(null=True, max_length=45)
    save_password = models.BooleanField(default=True)  # label="Save password? /(not recommended/)")
    salt = models.BinaryField(default=allauthdemo.settings.SALT)
    # image = models.ImageField(upload_to='images')

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
            self.content = self.ciphertext
            return True
        else:
            self.content = self.text
            return False

    def encrypt(self):
        self.salt = settings.SALT
        self.ciphertext = blog.encryption.encrypt(self.password, self.text, self.salt)
        self.text = 'None'
        self.content = self.ciphertext
        if self.save_password is False:
            self.password = None

    def decrypt(self):
        self.text = blog.encryption.decrypt(self.password, self.ciphertext)
        self.ciphertext = 'None'
        self.content = self.text
        if self.save_password is False:
            self.password = None

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Post._meta.fields]

    def content2(self):
        content_string = self.title + '\n'
        if self.is_encrypted:
            content_string += self.ciphertext
        else:
            content_string += self.text
        return content_string

    def set_content(self):
        content_string = self.title + '\n'
        if self.is_encrypted:
            content_string += self.ciphertext
        else:
            content_string += self.text
        self.content = content_string
        return content_string

    def get_content(self):
        content_string = self.title + '\n'
        if self.is_encrypted:
            content_string += self.ciphertext
        else:
            content_string += self.text
        self.content = content_string
        return content_string


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    # author = models.ForeignKey('auth.User', related_name="users")
    author = models.ForeignKey('allauthdemo_auth.DemoUser', related_name="users")
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


class EmailMessage(models.Model):
    post = models.ForeignKey('blog.Post', related_name='emailmessages')
    # author = models.ForeignKey('auth.User', related_name="users")
    sender = models.ForeignKey('allauthdemo_auth.DemoUser', related_name="emailmessage_users")
    # author = models.CharField(max_length=200)
    # message_content = models.TextField('post.content')
    message_content = models.TextField(blank=True, null=True)
    # content = post.content  # text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    destin_email = models.CharField(max_length=200)
    subject = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.destin_email + '; ' + self.message_content

    def short_text(self):
        return truncatechars(self.__str__, 350)

    def send(self):
        num_messages_sent = blog.blog_mail_sender.send(self)
        print('sent', num_messages_sent, 'email message(s)')
        return num_messages_sent


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
