from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from judith.models import PortfolioItem, BioCastellano, BioIngles, ContactInformation


class HomepageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        bio_ingles = BioIngles.objects.all().first()
        bio_castellano = BioCastellano.objects.all().first()
        contact_info = ContactInformation.objects.all().first()
        data['bio_ingles'] = bio_ingles
        data['bio_castellano'] = bio_castellano
        data['contact_info'] = contact_info
        return data


class PortfolioView(ListView):
    model = PortfolioItem

    @staticmethod
    def row_of_three_maker(queryset):
        """
        :param queryset: A queryset from the portfolio model
        :return: A list of lists with 3 items each. Each item in the list is a portfolio
        until the end, where padding is added in the form of a string until three list
        items is reached.
        """
        rows = list()
        row = list()
        for index, item in enumerate(queryset):
            space = index % 3
            print("SPACE IS: ", index, space)
            row.append(item)
            if len(row) == 3:
                row_to_copy = row.copy()
                rows.append(row_to_copy)
                row = list()
        if len(row) == 1:
            row.append("")
            row.append("")
            rows.append(row)
        if len(row) == 2:
            row.append("")
            rows.append(row)
        return rows

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        # Crear listas de 3 de los items en el portafolio para que podamos
        # poner 3 por linea en la página
        portfolio_queryset = PortfolioItem.objects.all().order_by("pk")
        list_of_rows = self.row_of_three_maker(portfolio_queryset)
        data['portfolio_items'] = list_of_rows
        return data