from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuario
from .models import EncargadoOperacion
from .models import EncargadoLogistico
from .models import CTO
from .models import CEO
from .models import Dueño
from .models import Cajero
from .models import Conductor

admin.site.register(Usuario)
admin.site.register(EncargadoOperacion)
admin.site.register(EncargadoLogistico)
admin.site.register(CTO)
admin.site.register(CEO)
admin.site.register(Dueño)
admin.site.register(Cajero)
admin.site.register(Conductor)

