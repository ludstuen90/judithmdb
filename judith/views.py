from django.shortcuts import render
from django.views.generic import TemplateView
from judith.models import PortfolioItem


class HomepageView(TemplateView):
    template_name = "about.html"

    @staticmethod
    def row_of_three_maker(queryset):
        rows = list()
        row = list()
        print("QUERYSET AL PRINCIPIO", len(queryset))
        for index, item in enumerate(queryset):
            space = index % 4
            print("SPACE IS: ", space)
            if space == 0:
                print("TRIGGERING ELSE")
                row_to_copy = row.copy()
                rows.append(row_to_copy)
                row = list()
            else:
                row.append(item)
        if len(row) != 0:
            rows.append(row)
        rows.pop(0)
        return rows

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        # Crear listas de 3 de los items en el portafolio para que podamos
        # poner 3 por linea en la página
        portfolio_queryset = PortfolioItem.objects.all()
        list_of_rows = self.row_of_three_maker(portfolio_queryset)
        for x in list_of_rows:
            print("!! ROW", len(x))
        data['portfolio_items'] = list_of_rows
        return data
