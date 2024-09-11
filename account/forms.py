from django import forms
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class FormSettings(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormSettings, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

class CustomUserForm(FormSettings):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance'):
            instance = kwargs.get('instance')
            self.fields['password'].required = False
            if self.instance.pk is not None:
                self.fields['password'].widget.attrs['placeholder'] = "Remplissez ce champ uniquement si vous souhaitez mettre à jour le mot de passe"
        else:
            self.fields['first_name'].required = True
            self.fields['last_name'].required = True

    def clean_email(self):
        form_email = self.cleaned_data['email'].lower()
        if self.instance.pk is None:  # Insert
            if CustomUser.objects.filter(email=form_email).exists():
                raise forms.ValidationError("L’e-mail donné est déjà enregistré")
        else:  # Update
            db_email = self.Meta.model.objects.get(id=self.instance.pk).email.lower()
            if db_email != form_email:  # There has been changes
                if CustomUser.objects.filter(email=form_email).exists():
                    raise forms.ValidationError("L’email donné est déjà enregistré")
        return form_email

    def clean_password(self):
        password = self.cleaned_data.get("password", None)
        if self.instance.pk is not None:
            if not password:
                return self.instance.password
        return make_password(password)

    class Meta:
        model = CustomUser
        fields = ['last_name', 'first_name', 'email', 'password']
        labels = {
            'last_name': 'Nom',
            'first_name': 'Prénom',
            'email': 'Email',
            'password': 'Mot de passe',
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Nom'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Prénom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}),
        }
