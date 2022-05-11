from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # AuthenticationForm - login uchun form
from django.contrib.auth.forms import User # AuthenticationForm - login uchun form
# from core.forms import RegisterForm
from .forms import LoginForm

@login_required
def check_user(request):
  user = request.user # AnonymousUser  
  print(user.is_authenticated)
  return render(request, 'check_auth.html', {'user': user})

# @login_required(login_url='/users/login')
# def check_user(request):
#   user = request.user # AnonymousUser  
#   print(user.is_authenticated)
#   return render(request, 'check_auth.html', {'user': user})

def register(request):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'registration/registration_finish.html', {})
  
  return render(request, 'registration/register.html', {'form': form})

def login_view(request):
  form = LoginForm()

  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      # user = User.objects.get(username=username) #->Error
      users = User.objects.filter(username=username)
      print(users)
      if not users:
        return render(request, "registration/login.html", 
        {'form': form, 'error': "bunfay fiydalanuvhi bor"})
      else:
        user = users[0]
        # if user.password != password:
        #   pass
        if user.check_password(password): #-> True, False
          # print('User - ', user, 'username = ', username, 'parol = ', user.password)
          print('Parol togri')
        else:
          print('Parol no togri')
        
  return render(request, "registration/login.html", {'form': form})
      