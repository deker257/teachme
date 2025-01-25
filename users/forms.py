from django import forms
from django.contrib.auth.hashers import make_password
from .models import Users

class CreateUser(forms.ModelForm):

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'type': 'password'}),
        label="Confirmez le mot de passe"
    )

    class Meta:
        model = Users
        fields = ['lastname', 'firstname', 'birthdate', 'username', 'email', 'sex', 'origins', 'sector', 'biography', 'profil', 'password']
        widgets =   {
            'birthdate' : forms.DateInput(attrs={'type': 'date'}),
            'profil' : forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'password' : forms.PasswordInput(attrs={'type':'password'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        # Hashage du mot de passe avant la sauvegarde
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user