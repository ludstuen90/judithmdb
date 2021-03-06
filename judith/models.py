from django.db import models
from datetime import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class BioCastellano(models.Model):
    bio_text = RichTextField()
    bio_below_the_fold_text = RichTextField()
    show_cv = models.BooleanField(help_text="Destildar para esconder el link al CV en el bio")
    bio_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return "Bio Castellano"

    class Meta:
        verbose_name = "Bio Castellano"
        verbose_name_plural = "Bio Castellano"


class BioIngles(models.Model):
    bio_text = RichTextField(help_text="Agregue la primera mitad del bio acá")
    bio_below_the_fold_text = RichTextField(help_text="Agregue la segunda mitad del bio acá (que en mobile, aparece cuando hagan clic en leer más")
    show_cv = models.BooleanField(help_text="Destildar para esconder el link al CV en el bio")
    bio_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return "Bio Inglés"
    class Meta:
        verbose_name = "Bio Inglés"
        verbose_name_plural = "Bio Inglés"


class HomePageItems(models.Model):
    homepage_portrait = models.ImageField()

    def __str__(self):
        return "Homepage Item"
    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"


class PortfolioItem(models.Model):
    class Meta:
        ordering = ['-priority']

    PORTFOLIO_SITE_HOSTING_CHOICES = [
        ('EX', 'ExternalSite'),
        ('PD', 'PDF')
    ]
    priority = models.IntegerField(help_text="El ítem con el número más grande va a aparecer primero en el portafolio")
    portfolio_description = models.TextField()
    portfolio_image = models.ImageField()

    portfolio_item_hosting = models.CharField(
        max_length=2,
        choices=PORTFOLIO_SITE_HOSTING_CHOICES,
        default='EX',
    )
    external_site_url = models.CharField(blank=True, max_length=300)
    bio_file = models.FileField(blank=True)

    def __str__(self):
        return self.portfolio_description


class EnglishPortfolioItem(PortfolioItem):
    class Meta:
        verbose_name = "Portfolio (EN)"
        verbose_name_plural = "Portfolio (EN)"


class CasetllanoPortfolioItem(PortfolioItem):
    class Meta:
        verbose_name = "Portfolio (ES)"
        verbose_name_plural = "Portfolio (ES)"


class BlogPost(models.Model):
    headline = models.CharField(max_length=70)
    subhead = models.TextField()
    fecha_de_publicacion = models.DateTimeField(
                    auto_now_add=True,
                    )
    blog_image = models.ImageField()
    blog_body = models.TextField()

    def __str__(self):
        return self.headline


class ContactInformation(models.Model):
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    twitter_url = models.CharField(max_length=40, blank=True)
    linked_in_url = models.CharField(max_length=40, blank=True)
    youtube_url = models.CharField(max_length=70, blank=True)
    instagram_url = models.CharField(max_length=40, blank=True)
    telegram_url = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return 'Datos de Contacto'

    class Meta:
        verbose_name = "Datos de Contacto"
        verbose_name_plural = "Datos de Contacto"
