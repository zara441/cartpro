from django import template



register=template.Library()


@register.simple_tag(name="total")
def total(cart):
    pass
