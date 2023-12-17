from django import forms
from .models import Dog, InjuryMedicalRecord, AdoptionDog, BorrowDog

class NewDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = [ 'photo', 'dogs_name', 'birth_date', 'gender', 'pool', 'mother', 'father']

    photo = forms.FileField(label='Upload Photo', required=False)
    mother = forms.ModelChoiceField(
        queryset=Dog.objects.filter(gender='f'),  # Adjust this queryset as needed
        label='Select a Mother',
        to_field_name='dog_id',  # Specify the field to use for the values (ID)
        empty_label=None  # Prevent displaying an empty choice
    )
    father = forms.ModelChoiceField(
        queryset=Dog.objects.filter(gender='m'),  # Adjust this queryset as needed
        label='Select a Father',
        to_field_name='dog_id',  # Specify the field to use for the values (ID)
    )


class InjuryMedicalRecordForm(forms.ModelForm):
    class Meta:
        model = InjuryMedicalRecord
        fields = '__all__'  # Include all fields from the model in the form

    # Customize the queryset for the 'dog' field to display dog names
    dog = forms.ModelChoiceField(
        queryset=Dog.objects.all(),  # Adjust this queryset as needed
        label='Select a Dog',
        to_field_name='dog_id',  # Specify the field to use for the values (ID)
        empty_label=None  # Prevent displaying an empty choice
    )

class AdoptionDogForm(forms.ModelForm):
    class Meta:
        model = AdoptionDog
        fields =  ['dog', 'adoption_date', 'owners', 'reason', 'is_adopted' ] # Include all fields from the model in the form

    # Customize the queryset for the 'dog' field to display dog names
    dog = forms.ModelChoiceField(
        queryset=Dog.objects.all(),  # Adjust this queryset as needed
        label='Select a Dog',
        to_field_name='dog_id',  # Specify the field to use for the values (ID)
        empty_label=None  # Prevent displaying an empty choice
    )

class BorrowDogForm(forms.ModelForm):
    class Meta:
        model = BorrowDog
        fields =  '__all__' # Include all fields from the model in the form

    # Customize the queryset for the 'dog' field to display dog names
    dog = forms.ModelChoiceField(
        queryset=Dog.objects.all(),  # Adjust this queryset as needed
        label='Select a Dog',
        to_field_name='dog_id',  # Specify the field to use for the values (ID)
        empty_label=None  # Prevent displaying an empty choice
    )

class EditDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = [ 'photo', 'dogs_name', 'birth_date', 'gender', 'pool', 'mother', 'father']

    photo = forms.FileField(label='Upload Photo', required=False)