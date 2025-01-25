from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Users
from courses.models import Cour
from django.contrib import messages
from .forms import CreateUser

# Create your views here.
def login(request):
    if request.method == 'POST':
        entered_username = request.POST['username']
        entered_password = request.POST['password']
        user = authenticate(request, username=entered_username, password=entered_password)
        
        if user is not None: #si l'utilisateur existe ou alors n'est pas absent
            auth_login(request, user) #on connecte le user
            return redirect('channel')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect !")
    return render(request, 'users/login.html')

def signup(request):
    if request.method == 'POST':
        # form = CreateUser(request.POST, request.FILES)
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        birthdate = request.POST.get('birthdate')
        username = request.POST.get('username')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        origin = request.POST.get('origin')
        biography = request.POST.get('biography')
        sector = request.POST.get('sector')
        profile = request.FILES.get('profile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Sauvegarde les données dans la base de données
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'users/signup.html')
        
        # Création de l'utilisateur
        if not Users.objects.filter(username=username).exists():
            user = Users.objects.create_user(
                firstname=firstname,
                lastname=lastname,
                username=username,
                email=email,
                birthdate=birthdate,
                sex=gender,
                profil=profile,
                origins=origin,
                sector=sector,
                biography=biography,
            )
            # Définir le mot de passe (hachage automatique via `set_password`)
            user.set_password(password)
            user.save()

            messages.success(request, "Inscription réussie.")
            return redirect('/account/login/')
        
        else:
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return redirect('/account/signup/')
        
    return render(request, 'users/signup.html')

@login_required
def channel(request):
    user = request.user #les informations du user connecté

    info = {

        'user' : user,
        'username' : user.username,
        'profil' : user.profil,
    }
    return render(request, 'users/channel.html', info)


@login_required
def account(request):
    pass


@login_required
def publish(request):
    return render(request, 'users/publish.html')

@login_required
def success(request):
    pass
