# *-* coding: utf-8 *-*
import textwrap
from django.db import models


class MarketProduct(models.Model):
    pk_product = models.CharField(max_length=50, verbose_name='Código', primary_key=True)
    product_description = models.TextField('Descrição do Produto')
    product_stock = models.FloatField('Estoque', default=0.0, null=True, blank=True)

    class Meta:
        db_table = 'market_product'
        verbose_name = "Produtos"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return textwrap.shorten(self.product_description, width=50, placeholder='...')
