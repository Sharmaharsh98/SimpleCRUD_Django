from .models import Cakeshop
from django import forms

class CakeshopForm(forms.ModelForm):
    class Meta:
        model = Cakeshop
        fields = '__all__'

        labels = {
            'choose_cake': 'Choose a Cake',
            'choose_icing': 'Choose a icing',
            'choose_flavors': 'Choose a flavors',
            'no_of_servings': 'Number of servings',
            'any_allergies': 'Do you have any allergies?',
            'number': 'Phone Number',
        }

        type = (('','---'),('choco', 'Chocolate'), ('white', 'White'), ('red', 'Red Velvet'), ('con', 'Confetti'), ('black', 'Black Forrest'),
            ('o', 'Other'))

        shape = (('square', 'Square'), ('circle', 'Circle'), ('rec', 'Rectangle'), ('o', 'Other'))

        icing = (('','---'),('butter', 'Buttercream'), ('Cream', 'Cream Cheese'), ('vanilla', 'Vanilla'), ('choco', 'Chocolate'), ('fon', 'Fondant'),
           ('o', 'Other'))

        flavors = (('van', 'Vanilla'), ('almond', 'Almond'), ('lemon', 'Lemon'), ('dried', 'Dried fruits'), ('chip', 'Chocolate Chips'),
                   ('oran','Orange'),('o', 'Other'))

        widgets = {
            'choose_cake': forms.Select(choices=type),
            'shape': forms.RadioSelect(choices=shape),
            'choose_icing': forms.Select(choices=icing),
            'choose_flavors': forms.CheckboxSelectMultiple(choices=flavors),
            'no_of_servings': forms.NumberInput(),
            'any_allergies': forms.Textarea(attrs={'rows':2}),
            'speacial_request': forms.Textarea(attrs={'rows':3}),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'address': forms.Textarea(attrs={'rows':3,"placeholder":"Enter your parmanent address"}),
            'city': forms.TextInput(),
            'number': forms.TextInput(),
            'date_required': forms.DateInput(attrs={'type':'date'}),
            'time_required': forms.TimeInput(attrs={'type':'time'})

        }