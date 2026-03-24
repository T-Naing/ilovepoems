from django.contrib import admin

# Register your models here.
from .models import Poem
from .models import Poet

admin.site.register(Poem)
admin.site.register(Poet)

