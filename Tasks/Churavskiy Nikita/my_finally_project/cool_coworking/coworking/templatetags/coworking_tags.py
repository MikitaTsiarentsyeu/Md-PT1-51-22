from django import template
from coworking.models import*

register = template.Library()


@register.inclusion_tag("coworking/show_footer_tag.html")
def show_footer():
    return 
