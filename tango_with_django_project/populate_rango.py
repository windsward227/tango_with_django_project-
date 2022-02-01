import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django 
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
 {'title': 'Official Python Tutorial',
 'url':'http://docs.python.org/3/tutorial/'},
 {'title':'How to Think like a Computer Scientist',
 'url':'http://www.greenteapress.com/thinkpython/'},
 {'title':'Learn Python in 10 Minutes',
 'url':'http://www.korokithakis.net/tutorials/python/'} ]
 {'title':'Official Django Tutorial',
 'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
 {'title':'Django Rocks',
 'url':'http://www.djangorocks.com/'},
 {'title':'How to Tango with Django',
 'url':'http://www.tangowithdjango.com/'} ]

    other_pages = [
 {'title':'Bottle',
 'url':'http://bottlepy.org/docs/dev/'},
 {'title':'Flask',
 'url':'http://flask.pocoo.org'} ]

    cats = {'Python': {'pages': python_pages, 'views':128,'likes':64},
 'Django': {'pages': django_pages,'views':64,'likes':32},
 'Other Frameworks': {'pages': other_pages,'views':32,'likes':16} }