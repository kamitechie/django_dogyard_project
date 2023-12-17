from django.shortcuts import render, redirect, get_object_or_404
from .models import Dog, InjuryMedicalRecord, BorrowDog, AdoptionDog
from datetime import date, timedelta
from .forms import NewDogForm, InjuryMedicalRecordForm, AdoptionDogForm, BorrowDogForm, EditDogForm
import base64


TODAY = date.today()
# Create your views here.
def home(request):
    return render(request, 'home.html')

def dogs_list(request):
    # Retrieve dogs without a date of death
    dogs_without_date_of_death = Dog.objects.exclude(medical_record__date_of_death__isnull=False)
    dogs_and_ages = []

    # def get_parents_names_by_id(parent_id):
    #     try:
    #         parent = Dog.objects.get(dog_id=parent_id)
    #         return parent.dogs_name
    #     except Dog.DoesNotExist:
    #         return "N/A"

    for dog in dogs_without_date_of_death:
        age = (TODAY - dog.birth_date).days // 365
        # mothers_name = get_parents_names_by_id(dog.mother)
        # fathers_name = get_parents_names_by_id(dog.father)
        dogs_and_ages.append((dog, age))

    return render(request, 'dogs_list.html', {'dogs_and_ages': dogs_and_ages})


def hospital(request):
    hospital_dogs = InjuryMedicalRecord.objects.all()
    return render(request, 'hospital.html', {'hospital_dogs': hospital_dogs})

def borrow(request):
    borrowed_dogs = BorrowDog.objects.all()
    return render(request, 'borrow.html', {'borrowed_dogs': borrowed_dogs})

def adopt(request):
    adopted_dogs = AdoptionDog.objects.all()
    return render(request, 'adopted.html', {'adopted_dogs': adopted_dogs})

def puppies(request):
    age_threshold = TODAY - timedelta(days=365 * 2)  # 2 years in days

    puppy_dogs = Dog.objects.filter(birth_date__gt=age_threshold)
    # puppy age in months
    for dog in puppy_dogs:
        birth_date = dog.birth_date
        age_in_months = (TODAY.year - birth_date.year) * 12 + (TODAY.month - birth_date.month)
        dog.age_in_months = age_in_months
    return render(request, 'puppies.html', {'puppy_dogs': puppy_dogs})

def a_pool(request):
    a_pool_dogs = Dog.objects.exclude(medical_record__date_of_death__isnull=False).filter(pool='A')
    dogs_and_ages = []


    for dog in a_pool_dogs:
        age = (TODAY - dog.birth_date).days // 365
        dogs_and_ages.append((dog, age))

    return render(request, 'a_pool.html', {'dogs_and_ages': dogs_and_ages})

def b_pool(request):
    b_pool_dogs = Dog.objects.exclude(medical_record__date_of_death__isnull=False).filter(pool='B')
    dogs_and_ages = []

    for dog in b_pool_dogs:
        age = (TODAY - dog.birth_date).days // 365
        dogs_and_ages.append((dog, age))
    return render(request, 'b_pool.html', {'dogs_and_ages': dogs_and_ages})

def c_pool(request):
    c_pool_dogs = Dog.objects.exclude(medical_record__date_of_death__isnull=False).filter(pool='C')
    dogs_and_ages = []

    for dog in c_pool_dogs:
        age = (TODAY - dog.birth_date).days // 365
        dogs_and_ages.append((dog, age))
    return render(request, 'c_pool.html', {'dogs_and_ages': dogs_and_ages})

def d_pool(request):
    d_pool_dogs = Dog.objects.exclude(medical_record__date_of_death__isnull=False).filter(pool='D')
    dogs_and_ages = []

    for dog in d_pool_dogs:
        age = (TODAY - dog.birth_date).days // 365
        dogs_and_ages.append((dog, age))
    return render(request, 'd_pool.html', {'dogs_and_ages': dogs_and_ages})

def e_pool(request):
    e_pool_dogs = Dog.objects.exclude(medical_record__date_of_death__isnull=False).filter(pool='E')
    dogs_and_ages = []

    for dog in e_pool_dogs:
        age = (TODAY - dog.birth_date).days // 365
        dogs_and_ages.append((dog, age))
    return render(request, 'e_pool.html', {'dogs_and_ages': dogs_and_ages})

def racing_pool(request):
    racing_pool_dogs = Dog.objects.exclude(medical_record__date_of_death__isnull=False).filter(pool='Racing')
    dogs_and_ages = []

    for dog in racing_pool_dogs:
        age = (TODAY - dog.birth_date).days // 365
        dogs_and_ages.append((dog, age))
    return render(request, 'racing_pool.html', {'dogs_and_ages': dogs_and_ages})

def family(request):
    return render(request, 'family_tree.html')

def team(request):
    return render(request, 'team_maker.html')

def schedule(request):
    return render(request, 'schedule.html')

def information(request):
    return render(request, 'info.html')


def add_dog(request):
    if request.method == 'POST':
        form = NewDogForm(request.POST, request.FILES)
        if form.is_valid():
            dog_instance = form.save(commit=False)

            # Read the uploaded file and store it as binary data
            if 'photo' in request.FILES:
                dog_instance.photo = request.FILES['photo'].read()

            dog_instance.save()
            return redirect('dogs_list')  # Redirect to the dogs list page after successful submission
    else:
        form = NewDogForm()

    return render(request, 'add_new_dog.html', {'form': form})

def add_puppy(request):
    if request.method == 'POST':
        form = NewDogForm(request.POST, request.FILES)
        if form.is_valid():
            dog_instance = form.save(commit=False)

            # Read the uploaded file and store it as binary data
            if 'photo' in request.FILES:
                dog_instance.photo = request.FILES['photo'].read()

            dog_instance.save()
            return redirect('puppies')  # Redirect to the puppies page after successful submission
    else:
        form = NewDogForm()

    return render(request, 'add_new_puppy.html', {'form': form})

def add_hospital_dog(request):
    if request.method == 'POST':
        form = InjuryMedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hospital_dogs')  # Redirect to the puppies page after successful submission
    else:
        form = InjuryMedicalRecordForm()

    return render(request, 'add_hospital_dog.html', {'form': form})

def add_adoption_dog(request):
    if request.method == 'POST':
        form = AdoptionDogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adopted_dogs')  # Redirect to the puppies page after successful submission
    else:
        form = AdoptionDogForm()

    return render(request, 'add_adoption_dog.html', {'form': form})

def add_borrow_dog(request):
    if request.method == 'POST':
        form = BorrowDogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('borrowed_dogs')  # Redirect to the puppies page after successful submission
    else:
        form = BorrowDogForm()

    return render(request, 'add_borrow_dog.html', {'form': form})


def show_form_from_dogs(request):
    return render(request, 'edit_dog.html', {'source_page': 'dogs_list'})

def show_form_from_puppies(request):
    return render(request, 'edit_dog.html', {'source_page': 'puppies'})


def edit_dog(request, dog_id):
    dog = get_object_or_404(Dog, dog_id=dog_id)


    if request.method == 'POST':
        form = EditDogForm(request.POST, request.FILES, instance=dog)
        source_page = request.GET.get('source_page')

        if form.is_valid():
            # Check if a new photo has been provided
            new_photo_data = request.FILES.get('photo')
            if new_photo_data:
                dog.photo = new_photo_data.read()
            form.save()

        # Conditional redirection based on the source page
        if source_page == 'dogs_list':
            return redirect('dogs_list')
        elif source_page == 'puppies':
            return redirect('puppies')
        else:
            return redirect('home')  # Redirect to a home page in case of an unknown source

    else:
        # Prepopulate the form with the existing data
        form = EditDogForm(instance=dog)



    return render(request, 'edit_dog.html', {'form': form})


