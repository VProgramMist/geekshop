from django import template

register = template.Library()


@register.filter(name='pricing')
def pricing(value):
    str_value = str(value)
    return f"{str_value[:-6] + ' ' + str_value[-6:-3] + ',' + str_value[-2:] if value > 1000 else str_value[:-3] + ',' + str_value[-2:]}"
