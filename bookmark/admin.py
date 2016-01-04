from django.contrib import admin

# Register your models here.
from .models import t_url
from .models import t_tag
from .models import t_url_tag

admin.site.register(t_url)
admin.site.register(t_tag)
admin.site.register(t_url_tag)
