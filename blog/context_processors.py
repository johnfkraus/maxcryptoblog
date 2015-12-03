from django.conf import settings  # import the settings file


def app_title(request):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {'APP_TITLE': settings.APP_TITLE}


def current_site(request):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {'current_site': settings.APP_TITLE}


def user_email_enabled(request):
    # return the value you want as a dictionary. you may add multiple values in there.
    return {'USER_EMAIL_ENABLED': settings.USER_EMAIL_ENABLED}
