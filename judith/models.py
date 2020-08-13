from django.db import models

# Create your models here.
class BioCastellano(models.Model):
    bio_text = models.TextField()
    bio_file = models.FileField

    def __str__(self):
        return "Bio Castellano"

    class Meta:
        verbose_name = "Bio Castellano"
        verbose_name_plural = "Bio Castellano"

class BioIngles(models.Model):
    bio_text = models.TextField()
    bio_file = models.FileField()

    def __str__(self):
        return "Bio Inglés"
    class Meta:
        verbose_name = "Bio Inglés"
        verbose_name_plural = "Bio Inglés"


class HomePageItems(models.Model):
    homepage_portrait = models.ImageField()
    twitter_url = models.CharField(max_length=40)
    linked_in_url = models.CharField(max_length=40)
    facebook_url = models.CharField(max_length=40)

    def __str__(self):
        return "Homepage Item"
    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"

class PortfolioItem(models.Model):
    portfolio_image = models.ImageField()
    portfolio_description = models.TextField()
    PORTFOLIO_SITE_HOSTING_CHOICES = [
        ('PD', 'PDF'),
        ('EX', 'ExternalSite'),
    ]
    portfolio_item_hosting = models.CharField(
        max_length=2,
        choices=PORTFOLIO_SITE_HOSTING_CHOICES,
        default='PD',
    )
    bio_file = models.FileField()

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.portfolio_description

class BlogPost(models.Model):
    headline = models.CharField(max_length=70)
    subhead = models.TextField()
    blog_body = models.TextField()

    def __str__(self):
        return self.headline


class ContactInformation(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)


    def __str__(self):
        return 'Datos de Contacto'

    class Meta:
        verbose_name = "Datos de Contacto"
        verbose_name_plural = "Datos de Contacto"
