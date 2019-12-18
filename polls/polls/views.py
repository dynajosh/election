from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from contestant.models import Contestant
from .render import render_to_pdf
from django.views.generic import View

# just added
import os
from django.template import Context
from xhtml2pdf import pisa
from django.conf import settings




from contestant.models import Contestant
import sqlite3
from sqlite3 import Error




"""
CREATING THE HOMEPAGE: The department_name and session fields are variables that
can be changed to meet custom needs.
context is a dictionary that is parsed into the template.
"""
def home_page(request, *args, **kwargs):
    department_name = "NAQSS"
    session = "2019/2020"
    context = {"department_name": department_name, "session": session }
    return render(request, "home.html", context)


def example_page(request, *args, **kwargs):
    return render(request, "example.html")
 


# DON'T MESS WITH THIS CODE!!!!!
# This part validates users login taking from the login form 
# and checking if they match the data already stored in the txt files
def login_view(request):
    # Create the datbases for matric numbers and passwords
    connect_matric = sqlite3.connect('matrices.db')
    connect_password = sqlite3.connect('userps.db')
    # cursors for each of the databases
    cursor_matric = connect_matric.cursor()
    cursor_password = connect_password.cursor()

    # creating the tables for all the entries of matric numbers and passwords

    # cursor_matric.execute("CREATE TABLE entries(matric_number text)")
    cursor_matric.execute("INSERT INTO entries VALUES('QTS/2015/039'),('QTS/2015/040')" )
    connect_matric.commit()

    # cursor_password.execute("CREATE TABLE entries(password text)")
    cursor_password.execute("INSERT INTO entries VALUES('simi'),('falz')")
    connect_password.commit()
    # a = input("enter username: ")
    # b = input("enter password: ")
    a = str(request.POST.get('username'))
    b = str(request.POST.get('password'))
    cursor_matric.execute("SELECT matric_number from entries WHERE matric_number = (?)", (a,))
    xxx = cursor_matric.fetchone()
    print(xxx)    
    if xxx != None:
        if a == xxx[0]:
            x = 1
            print('True')
            cursor_matric.execute("UPDATE entries set matric_number = (?) WHERE matric_number = (?)", (a +"voted", a,))
            connect_matric.commit()
    else:
        x = 0
        # print("we couldn't find a match for matric number")
    
    cursor_password.execute("SELECT password from entries WHERE password = (?)", (b,))
    yyy = cursor_password.fetchone()
    print(yyy)    
    if yyy != None:
        if b == yyy[0]:
            y = 1
            print('True')
            cursor_password.execute("UPDATE entries set password = (?) WHERE password = (?)", (b +"voted", b,))
            connect_password.commit()
    else:
        y = 0
        # print("we couldn't find a match for password")
    if x == 1 and y == 1:
        return redirect('/vote/president')
        # print("success")
        successful = "/vote/president"
        # # break
        # print("Username entered: ", a)
        # print("Password entered: ", b)        
    else:
        print("failed")
        # failed = "#"
        # print("Username entered: ", a)
        # print("Password entered: ", b)

    successful = ""
    failed = ""
    form = "a"
    page_heading = "Login to vote here!"
    template_name = 'login.html'
    context = {"form": form, "page_heading": page_heading}
    return render(request, template_name, context)

# login_view()


def results_view(request, *args, **kwargs):
    department_name = "NAQSS"
    session = "2019/2020"
    page_heading = "Election Results"
    qs = Contestant.objects.all()

    context = {"department_name": department_name, "session": session, "page_heading": page_heading, "list": qs}
    return render(request, "results.html", context)

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


def results_download(request):
    template_path = 'results_download.html'
    department_name = "NAQSS"
    session = "2019/2020"
    page_heading = "Election Results"
    qs = Contestant.objects.all()

    context = {"department_name": department_name, "session": session, "page_heading": page_heading, "list": qs}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    # html = template.render(Context(context))
    html = template.render(context)


    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# class GeneratePDF(View):
#     def get(self, request, *args, **kwargs):
#         template = get_template('results.html')
#         department_name = "NAQSS"
#         session = "2019/2020"
#         page_heading = "Election Results"
#         qs = Contestant.objects.all()
#         context = {"department_name": department_name, "session": session, "page_heading": page_heading, "list": qs}
#         # pdf = render_to_pdf('results.html', context)
#         html = template.render(context)
#         # pdf = render_to_pdf('results.html', context)
#         # return HttpResponse(pdf, content_type='application/pdf')
#         return HttpResponse(html)