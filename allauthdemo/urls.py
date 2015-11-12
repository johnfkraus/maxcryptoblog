from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

import allauthdemo.views
import blog.views

# from . import views_email


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    url(r'^', include('blog.urls')),
    # url(r'^about$', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),

    url(r'^about$', TemplateView.as_view(template_name='blog/about.html'), name='about'),
    url(r'^terms/$', TemplateView.as_view(template_name='visitor/terms.html'), name='website_terms'),
    url(r'^contact$', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'allauthdemo.auth.views.account_profile', name='account_profile'),
    url(r'^member/$', allauthdemo.views.member_index, name='user_home'),
    # url(r'^member/action$', allauthdemo.views.member_action, name='user_action'),
    url(r'^member/action$', blog.views.post_list, name='user_action'),  # blog/post_list'),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
# E-mail
url(r"^email/$", views_email.email, name="account_email"),
url(r"^confirm-email/$", views_email.email_verification_sent,
    name="account_email_verification_sent"),
url(r"^confirm-email/(?P<key>\w+)/$", views_email.confirm_email,
    name="account_confirm_email"),
"""
