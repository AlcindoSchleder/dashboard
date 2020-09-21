# _*_ coding: utf-8 _*_
# import mpld3
# from mpld3.plugins import Zoom, LineLabelTooltip
# from matplotlib import pyplot as plt
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import TemplateView
# from .models import DatasetModel

# Create your views here.


class DashboardView(TemplateView):

    template_name = 'home/index.html'
    allowed_methods = ['GET', 'POST']

    def get(self, request, *args, **kwargs):
        message = kwargs.get('message', '')
        qs_register = None
        if request.user.is_authenticated:
            user = request.user
            try:
                qs_register = request.user.fk_registers_users.filter(fk_user=user)
                register = qs_register[0]
                if register.register_image is None or \
                        register.register_image == '':
                    user_image = None
                else:
                    user_image = register.register_image.url
            except ObjectDoesNotExist:
                user = None
                user_image = None
        else:
            user = None
            user_image = None
        params = {
            'user': user,
            'user_image': user_image,
            'profile': True,
            'qs_registers': qs_register,
            'message': message
        }
        return render(request, self.template_name, params)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)


# class ShowGraphView(TemplateView):
#
#     template_name = 'home/index.html'
#     model = None
#
#     xvalues = None
#     coinbase_values = None
#     mercado_values = None
#     kraken_values = None
#     bitflyer_values = None
#     binance_values = None
#
#     coinbase_lines = None
#     mercado_lines = None
#     kraken_lines = None
#     binance_lines = None
#     bitflyer_lines = None
#
#     def extract_values(self, data_rows: list):
#         self.xvalues = list(map(lambda x: x['Timestamp'], data_rows))
#         self.coinbase_values = list(map(lambda x: x['conibase'], data_rows))
#         self.mercado_values = list(map(lambda x: x['mercado'], data_rows))
#         self.kraken_values = list(map(lambda x: x['kraken'], data_rows))
#         self.bitflyer_values = list(map(lambda x: x['bitflyer'], data_rows))
#         self.binance_values = list(map(lambda x: x['binance'], data_rows))
#
#     def create_lines(self):
#         self.coinbase_lines = plt.plot(self.xvalues, self.coinbase_values, label="coinbase")
#         self.mercado_lines = plt.plot(self.xvalues, self.mercado_values, label="mercado")
#         self.kraken_lines = plt.plot(self.xvalues, self.kraken_values, label="kraken")
#         self.binance_lines = plt.plot(self.xvalues, self.binance_values, label="binance")
#         self.bitflyer_lines = plt.plot(self.xvalues, self.bitflyer_values, label="bitflyer")
#
#     def create_graph(self):
#         # Add legend
#         fig = plt.figure(1, figsize=(25, 10))
#         plt.title('Evolução do bitcoin em 2020', fontsize=16, fontweight='bold')
#
#         # Add title and x, y labels
#         plt.legend(loc='lower left')
#         plt.suptitle("Variação no mês de Março de 2020", fontsize=10)
#         plt.xlabel("Data")
#         plt.ylabel("Valor R$")
#         plt.grid(True)
#
#         mpld3.plugins.connect(
#             fig, Zoom(),
#             LineLabelTooltip(self.coinbase_lines[0]),
#             LineLabelTooltip(self.mercado_lines[0]),
#             LineLabelTooltip(self.kraken_lines[0]),
#             LineLabelTooltip(self.binance_lines[0]),
#             LineLabelTooltip(self.bitflyer_lines[0])
#         )
#         fig_html = mpld3.fig_to_html(fig)
#         params = {
#             'figure': fig_html,
#             'opts': self.model._meta,
#             'app_label': self.model._meta.app_label,
#         }
#         return fig_html, params
#
#     def get(self, request, *args, **kwargs):
#         params = None
#         start_date = datetime.strptime('2020-04-01 00:00:01', '%Y-%m-%d %H:%M:%S')
#         self.model = DatasetModel()
#         data_rows = self.model.initialize_db(start_date, 100)
#
#         if data_rows is not None:
#             self.extract_values(data_rows)
#             self.create_lines()
#             params = self.create_graph()
#
#         return render(request, self.template_name, params)
