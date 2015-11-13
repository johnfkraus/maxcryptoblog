
UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'allauthdemo' WHERE id=1;


DELETE from auth_user;  -- or just the first user?
INSERT INTO auth_user(id, password, last_login, is_superuser, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES (1, 'pbkdf2_sha256$20000$2hf4uiCz3vcu$vG5klhoRz2l3rGI3wwyJw+dopxtmwkdEpBKcmAAlg/A=', '2015-11-09 20:34:24.929877', 1, 'Mr.', 'Admin', 'johnkraus3@gmail.cm', 1, 1, '2015-11-09 20:34:24.929877');

