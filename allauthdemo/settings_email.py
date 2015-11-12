# allauthdemo/settings_email.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'crypt.blog.dude@gmail.com'  # my gmail account'
EMAIL_HOST_PASSWORD = '@WSX2wsx!QAZ1qaz'
DEFAULT_FROM_EMAIL = 'crypt.blog.dude@gmail.com'   # my gmail account'
DEFAULT_TO_EMAIL = 'johnkraus3@gmail.com'  # to email'
