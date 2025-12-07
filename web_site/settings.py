ALLOWED_HOSTS = ['*']  # or specify your Render domain

DEBUG = False

# Add Render domain
ALLOWED_HOSTS = ['yourdomain.onrender.com', 'localhost', '127.0.0.1']

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')