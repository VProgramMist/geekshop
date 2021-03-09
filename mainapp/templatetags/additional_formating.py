from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='pricing')
def pricing(value):
    str_value = str(value)
    return str_value[:-6] + ' ' + str_value[-6:-3] + ',' + str_value[-2:] if value > 1000 else str_value[
                                                                                               :-3] + ',' + str_value[
                                                                                                            -2:]


@register.filter(name='dating')
def dating(value):
    try:
        date = datetime.strptime(value, '%d.%m.%Y')
    except:
        date = datetime.strptime(value, '%Y-%m-%d')
    return datetime.strftime(date, '%Y-%m-%d')
