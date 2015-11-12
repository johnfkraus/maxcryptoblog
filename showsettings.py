from django.conf import settings
# dir(settings)
settings.configure()


def show_settings():
    from django.conf import settings
    for name in dir(settings):
        print(name, getattr(settings, name))

show_settings()
