
DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'job'             # Or path to database file if using sqlite3.
DATABASE_USER = 'naved'             # Not used with sqlite3.
DATABASE_PASSWORD = 'naved'         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.


INSTALLED_APPS = (
                                    'django.contrib.comments',
                  'django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django.contrib.admin',
#                  'south',
                  'job',
                  )

TIME_ZONE = 'UTC'