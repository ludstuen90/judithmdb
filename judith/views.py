from django.shortcuts import render
from django.views.generic import TemplateView
from judith.models import PortfolioItem, BioCastellano, BioIngles, ContactInformation


class HomepageView(TemplateView):
    template_name = "about.html"

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
        print("QUERYSET AL PRINCIPIO", len(queryset))
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
        print("AT THE END, THE LENGTH OF THE ROW IS: ", len(row))
        print("ROW AT END IS: ", type(row))
        return rows

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # Crear listas de 3 de los items en el portafolio para que podamos
        # poner 3 por linea en la página
        portfolio_queryset = PortfolioItem.objects.all().order_by("pk")
        list_of_rows = self.row_of_three_maker(portfolio_queryset)
        bio_ingles = BioIngles.objects.all().first()
        bio_castellano = BioCastellano.objects.all().first()
        contact_info = ContactInformation.objects.all().first()
        print("Blog castellano es: ", bio_castellano)
        for x in list_of_rows:
            print("!! ROW", len(x))
        data['portfolio_items'] = list_of_rows
        data['bio_ingles'] = bio_ingles
        data['bio_castellano'] = bio_castellano
        data['contact_info'] = contact_info
        return data
