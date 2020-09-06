from django.contrib import admin
from judith.models import BioCastellano, BioIngles, HomePageItems, PortfolioItem, BlogPost, ContactInformation, EnglishPortfolioItem, CasetllanoPortfolioItem



class EditOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = "Administración del Portfolio"
admin.site.site_title = "Administración: Judith Morales"
admin.site.index_title = "Bienvenida, Judith!"


# Register your models here.
admin.site.register(BioCastellano, EditOnlyAdmin)
admin.site.register(BioIngles, EditOnlyAdmin)
admin.site.register(HomePageItems, EditOnlyAdmin)
# admin.site.register(PortfolioItem)
admin.site.register(EnglishPortfolioItem)
admin.site.register(CasetllanoPortfolioItem)
admin.site.register(BlogPost)
admin.site.register(ContactInformation, EditOnlyAdmin)
