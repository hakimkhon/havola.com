from django.shortcuts import render

def check_user(request):
  user = request.user
  print(user.is_authenticated)
  return render(request, 'check_auth.html', {'user': user})
