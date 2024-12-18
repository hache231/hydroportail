from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )


class UserForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        label='Nom d\'utilisateur',
        widget=forms.TextInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    firstname = forms.CharField(
        max_length=100,
        label='Prénom',
        widget=forms.TextInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    lastname = forms.CharField(
        max_length=100,
        label='Nom',
        widget=forms.TextInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    middlename = forms.CharField(
        max_length=100,
        required=False,
        label='Post-nom',
        widget=forms.TextInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    sex = forms.ChoiceField(
        choices=[('M', 'Homme'), ('F', 'Femme')],
        label='Sexe',
        widget=forms.Select(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    birthday = forms.DateField(
        label='Date de naissance',
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )
    fonction = forms.CharField(
        max_length=100,
        label='Fonction',
        widget=forms.TextInput(attrs={
            'class': 'col-span-1 block w-full px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-md focus:border-blue-500 focus:outline-none focus:ring mb-4'
        })
    )