from django.contrib import admin
from judith.models import BioCastellano, BioIngles, HomePageItems, PortfolioItem, BlogPost, ContactInformation

# Register your models here.
admin.site.register(BioCastellano)
admin.site.register(BioIngles)
admin.site.register(HomePageItems)
admin.site.register(PortfolioItem)
admin.site.register(BlogPost)
admin.site.register(ContactInformation)


admin.site.site_header = "Administración del Portfolio"
admin.site.site_title = "Administración: Judith Morales"
admin.site.index_title = "Bienvenida, Judith!"
