from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
  context = {
    "title":"Hello World!",
    "content":"Welcome to the homepage." 
  }
  if request.user.is_authenticated():
    context["premium_content"] = "yeah!!"
  return render(request, "home_page.html", context)

def about_page(request):
  context = {
    "title":"About Page!",
    "content":"Welcome to the about page."
  }
  return render(request, "home_page.html", context)

def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context = {
    "title":"Contact!",
    "content":"Welcome to the contact Page.",
    "form":contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  # if request.method == "POST":
      # print(request.POST)
      # print(request.POST.get('fullname'))
      # print(request.POST.get('email'))
      # print(request.POST.get('content'))
  return render(request, "contact/view.html", context)

def login_page(request):
  form = LoginForm(request.POST or None)
  context = {
    "form":  form
  }
  print("User logged in")
  print(request.user.is_authenticated())
  if form.is_valid():
      print(form.cleaned_data)
      username = form.cleaned_data.get("username")
      password = form.cleaned_data.get("password")
      user = authenticate(request, username=username, password=password)
      print(user)
      print(request.user.is_authenticated())
      if user is not None:
          print(request.user.is_authenticated())
          login(request, user)
      
      # Redirect to a success page.
      # context['form'] = LoginForm()  
          return redirect("/")
      else:
      # Return an 'invalid login' error message.
        print("Error")
  return render(request,"auth/login.html",context)

User = get_user_model() 
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
      print(form.cleaned_data)
      username = form.cleaned_data.get("username")
      email = form.cleaned_data.get("email")
      password = form.cleaned_data.get("password")
      new_user = User.objects.create_user(username, email, password)
      print(new_user)
    return render(request,"auth/register.html",context)



def home_page_old(request):
  html="""
  <!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <div class='text-center'>
    <h1>Hello, world!</h1>
    </div>

    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: jQuery and Bootstrap Bundle (includes Popper) -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>

    <!-- Option 2: jQuery, Popper.js, and Bootstrap JS
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    -->
  </body>
</html>
  """
  return HttpResponse(html)