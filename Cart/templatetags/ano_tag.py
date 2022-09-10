from itertools import product
from django import template
from product.models import Product
register = template.Library()

@register.simple_tag
def show(details,det=None,arg=None):
    if arg == None:
        x = Product.objects.get(id=det)
        return x.image.url
    else:
        return details[det][arg]

@register.simple_tag
def show_price(details,id,count=None):
    size = show(details,id,'size')
    color = show(details,id,'color')
    if count:
        count = show(details,id,'count')
    product = Product.objects.get(id=id)
    price_color = 0
    try:
        x = product.color_set.get(color=color)
        price_color = x.Ekhtelaf
    except:
        pass
    price_size = 0
    try:
        x = product.size_set.get(size=size)
        price_size = x.Ekhtelaf
    except:
        pass
    total_price = price_color + price_size + product.main_discount_cal(inti=True)
    if count ==None:
        return total_price
    else:
        return total_price*count

@register.simple_tag
def tedad_mahsole(details):
    x = Product.objects.get(id=details)
    return x.tedad_mahsole

# @register.simple_tag
# def total_single_price(details,id,count):
#     total_price = show_price()