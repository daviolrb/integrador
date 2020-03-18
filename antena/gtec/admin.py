from django.contrib import admin
from .models import Post, Vaga, Cliente, Reserva

class PostAdmin(admin.ModelAdmin):
    list_display  = ('title','author', 'created_at', 'updated_at', 'status')
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Vaga)
admin.site.register(Reserva)
admin.site.register(Cliente)