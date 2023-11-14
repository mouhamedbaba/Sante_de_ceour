from django import template

register = template.Library()

@register.filter
def percent(valeur, total):
    if total == 0:
        return 0
    val =  (valeur / total) * 100
    return val