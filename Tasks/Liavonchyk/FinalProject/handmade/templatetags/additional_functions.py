from bs4 import BeautifulSoup
from urllib.request import urlopen
from django import template

register = template.Library()

@register.simple_tag
def bynusd():
    return bynusd_func()

def bynusd_func():
    html = urlopen('https://kurs.onliner.by/')
    soup = BeautifulSoup(html, features="html.parser")
    tag_list = soup.find_all('p', {'class':'value'})
    nb = tag_list[2].text
    return float(nb.replace(",",".").replace(" BYN",""))
