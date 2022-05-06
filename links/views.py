from django.http import Http404
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Link
from links import models
from .forms import LinkForm, RegisterForm

def home(request):    
    return render(request, "details/home.html")


def link_list(request):
    links = Link.objects.all()
    context = {
        "title": "Bu sarlavha",
        "linklar": links
    }
    return render(request, "link/link_list.html", context)


def link_detail(request, pk):
    link = get_object_or_404(models.Link, id = pk)
    # try:
    #     link = Link.objects.get(id = pk)
    # except Exception as e:
    #     print(e)
    #     raise Http404('Afsuski siz izlagan link topilmadi!' )
    return render(request, "link/link_detail.html", {'link': link})


# def link_create(request):   
#     errors = {}
#     date = {}
                # print(f"============={ request.mathod }=============")
                # if request.mathod == 'GET':
                #     print('bu get so\'rovi edi')
                #     print('request.GET=', request.GET)
    
    # if request.method == 'POST':
    #     print(request.POST)
    #     name_of_link = request.POST.get('name')
    #     description_of_link = request.POST.get('description')
    #     url_of_link = request.POST.get('url')
    #     date['name'] = name_of_link
    #     date['description'] = description_of_link
    #     date['url'] = url_of_link

    #     if name_of_link and url_of_link:
    #         new_link = Link.objects.create(
    #             name = name_of_link,
    #             description = description_of_link,
    #             url = url_of_link
    #         )
    #         return redirect('/list')
    #     else:
    #         if not name_of_link:
    #             errors['name'] = 'Iltimos link nomini kiriting'
    #         if not url_of_link:
    #             errors['url'] = 'Iltimos link urlini kiriting'

    # return render(request, "link/link_create.html", {'errors': errors, 'date': date})


def link_create(request):   
    form = LinkForm()
    errors = {}
    date = {}
    
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('link:link_list')

    return render(request, "link/link_create.html", {
        'errors': errors, 'date': date, 'form': form
    })


def link_update(request, pk):
    link = get_object_or_404(Link, id = pk)
    form = LinkForm(instance=link)

    if request.method == 'POST':
        form = LinkForm(instance=link, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('link:link_list') 

    return render(request, "link/link_update.html", {'form': form})


def register(request):
    form = RegisterForm()
    print('is_boound', form.is_bound)
    print('fields', form.fields)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print('data', form.data)
        if form.is_valid():
            pass
        print('cleaned_form', form.cleaned_data)
    return render(request, "link/register.html", {'form': form})