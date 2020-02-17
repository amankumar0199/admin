from django.shortcuts import render,redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from adminapp import forms
from adminapp.models import CustomUser
from geopy.geocoders import Nominatim

from django.views.generic import ListView
from .models import CrudUser

#crud
from .models import CrudUser
from django.views.generic import View
from django.http import JsonResponse



class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'



class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)




class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def signup(request):
    form = forms.UserRegisterForm()
    form1 = forms.choiceRegisterForm()
    form2 = forms.institudeRegisterForm()
    form3 = forms.teacherRegisterForm()
    form4 = forms.studentRegisterForm()
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST)
        form1 = forms.choiceRegisterForm(request.POST)
        form2 = forms.institudeRegisterForm(request.POST)
        form3 = forms.teacherRegisterForm(request.POST)
        form4 = forms.studentRegisterForm(request.POST)

        if form.is_valid() and form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            print(form4)
            c1 = form.save(commit = False)
            email = form.cleaned_data.get('email')
            user_id = email
            c1.username = email
            c1.save()

            c = form1.save(commit = False)
            d = form2.save(commit = False)
            e = form3.save(commit = False)
            f = form4.save(commit = False)
            type = form1.cleaned_data['choice']

            if type == "C":
                email = form.cleaned_data.get('email')
                email = CustomUser.objects.get(email = email).id
                name = form2.cleaned_data.get('institude_name')
                print(name)
                name = str(name)[0:2]
                id = name+str(email)
                c.email_id = email
                d.email_id = email
                print(type)
                d.choice = type
                print(d.choice)
                d.institude_id = id
                c.save()
                d.save()
                return redirect('account_login')
            elif type == "T":
                email = form.cleaned_data.get('email')
                pincode = form1.cleaned_data.get('pincode')
                email = CustomUser.objects.get(email = email).id
                name = form3.cleaned_data.get('first_name')
                print(name)
                name = str(name)[0:2]
                id = name+str(email)
                geolocator = Nominatim(timeout=3)
                location = geolocator.geocode(pincode)
                distance = str(location.latitude)+", "+str(location.longitude)
                e.distance = distance
                c.email_id = email
                e.email_id = email
                e.teacher_id = id
                e.choice = type
                c.save()
                e.save()
                return redirect('account_login')
            elif type == "S":
                email = form.cleaned_data.get('email')
                email = CustomUser.objects.get(email = email).id
                name = form4.cleaned_data.get('first_name')
                print(name)
                name = str(name)[0:2]
                id = name+str(email)

                c.email_id = email
                f.email_id = email
                f.student_id = id
                f.choice = type
                c.save()
                f.save()
                return redirect('account_login')

    return render(request, 'register.html',{'form':form,'form1':form1,'form2':form2,'form3':form3,'form4':form4,})
