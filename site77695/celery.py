import os
from celery import Celery

# Django ayar dosyasını belirt
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site77695.settings')

app = Celery('site77695')

# Ayarları Django settings.py'den al
app.config_from_object('django.conf:settings', namespace='CELERY')

# Uygulamadaki tüm tasks.py dosyalarını otomatik bul
app.autodiscover_tasks()
