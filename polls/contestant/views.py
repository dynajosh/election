from django.shortcuts import render
from django.http import HttpResponse
from .models import Contestant
from .forms import ContestantModelForm
from django.template.loader import get_template
# Create your views here.


# This view handles the creation of new Contestants
def create_contestant_view(request):
    form = ContestantModelForm(request.POST or None, request.FILES or None)
    page_heading = "Create a new contestant here!"
    if form.is_valid():
        obj = form.save(commit = False)
        obj.name = form.cleaned_data.get("name")
        obj.save()
        form = ContestantModelForm()
    template_name = 'create/form.html'
    context = {"form": form, "page_heading": page_heading}
    return render(request, template_name, context)


#===========================================================================================================
#This code displays canditates contesting for the  post of the president
def president_view(request, *args, **kwargs):
    #list out everyone contesting for president
    qs = Contestant.objects.all()
    section = "Category : President"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
        # else:
        #     print("nah buyer")
    return render(request, "vote_president.html", context)

 
#This code displays canditates contesting for the  post of the vice president
def vice_president_view(request, *args, **kwargs):
    #list out everyone contesting for president
    qs = Contestant.objects.all()
    section = "Category : Vice President"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_vice_president.html", context)


#This code displays canditates contesting for the  post of the general secretary
def general_secretary_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : General Secretary"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_general_secretary.html", context)


#This code displays canditates contesting for the  post of the assistant general secretary
def assistant_general_secretary_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : Assistant General Secretary"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_assistant_general_secretary.html", context)


#This code displays canditates contesting for the  post of the treasurer
def treasurer_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : Treasurer"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_treasurer.html", context)


#This code displays canditates contesting for the  post of the financial secretary
def financial_secretary_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : Financial Secretary"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_financial_secretary.html", context)


#This code displays canditates contesting for the  post of the librarian
def librarian_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : Librarian"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_librarian.html", context)


#This code displays canditates contesting for the  post of the sports director
def sports_director_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : Sports Director"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_sports_director.html", context)


#This code displays canditates contesting for the  post of the P.R.O
def pro_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : P.R.O"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_pro.html", context)

#This code displays canditates contesting for the  post of the Social Director
def social_director_view(request, *args, **kwargs):
    qs = Contestant.objects.all()
    section = "Category : Social Director"
    context = {"list": qs, "section": section}
    if request.method == "POST":
        vote = request.POST.get('vote', '')
        xxx = Contestant.objects.filter(reg_number=vote)
        for g in xxx:
            g.votes += 1
            print(g.votes)
            g.save()
    return render(request, "vote_social_director.html", context)