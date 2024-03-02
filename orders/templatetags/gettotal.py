from django import template

register=template.Library()


@register.simple_tag(name="gettotal")
def gettotal(cart):
    total=0
    for i in cart.addeditems.all():
        total+=i.quantity * i.product.price
    return total    
    