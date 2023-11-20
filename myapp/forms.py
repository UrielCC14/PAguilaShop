from django import forms
from django.forms import ModelForm
from .models import Shipping_Address,Targets,Product,Category,Tickets,Zona

class general_purchase_settings(forms.Form):
    
    delivery_address = forms.CharField(
        label="Delivery Address:", max_length=200, widget=forms.HiddenInput(attrs={'class': 'form-control bg-transparent text-light','id':'id_address'}))

    payment_method = forms.CharField(
        label="Payment Method:", max_length=200, widget=forms.HiddenInput(attrs={'class': 'form-control bg-transparent text-light','id':'id_target'}))

    contact_number = forms.CharField(
        label="Contact Number:", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}))

    delivery_specifications = forms.CharField(
        label="Delivery Specifications:", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}))
    
    amount = forms.CharField(
        label="Amount:", max_length=200, widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light','id':'amount'}))
    
    product_id = forms.CharField(
        label="Product:", max_length=200, widget=forms.HiddenInput(attrs={'class': 'form-control bg-transparent text-light'}))
    
    product = forms.CharField(
        label="Product:", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}))
    
    price = forms.CharField(
        label="Price:", max_length=200, widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light','id':'price'}))
    
    total = forms.CharField(
        label="Total:", max_length=200, widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light','id':'total'}))
    
    
class Create_Address_Form(forms.ModelForm):
    class Meta:
        model = Shipping_Address
        fields = ['country','city','address','postal_code']
        widgets = {
            'country': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your country'}),
            'city': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your city'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your Address'}),
            'postal_code': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Write your postal_code'}),
        }
        
class Create_Target_Form(forms.ModelForm):
    class Meta:
        model = Targets
        fields = ['target_number','target_name','cvv','expiration_date']
        widgets = {
            'target_number': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Write your target_number'}),
            'target_name': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your target_name'}),
            'cvv': forms.NumberInput(attrs={'class':'form-control','placeholder': 'Write your CVV'}),
            'expiration_date': forms.TextInput(attrs={'class':'form-control','placeholder': 'Write your expiration_date'}),
        }
        
class Create_NEw_Product(forms.ModelForm):
    
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select a category",
        widget=forms.Select(attrs={'class': 'form-control bg-transparent text-light'})
    )
    imagen = forms.ImageField(  # Campo para la imagen
        widget=forms.ClearableFileInput(attrs={'class': 'form-control bg-transparent text-light'})
    )
    
    class Meta:
        model = Product
        fields = ['name','temporada','description','price','imagen','category']
   
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write the product name'}),
            'temporada': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write the season'}),
            'description': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write the description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write the price'}),
        }
        
        
class Create_New_Ticket(forms.ModelForm):
    
    zona = forms.ModelChoiceField(
        queryset=Zona.objects.all(),
        empty_label="Select a Zone",
        widget=forms.Select(attrs={'class': 'form-control bg-transparent text-light'})
    )
    
    class Meta:
        model = Tickets
        fields =['name','Precio','zona']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write the product name'}),
            'Precio': forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light', 'placeholder': 'Write the season'}),
        }
        
class general_purchase_settings_ticket(forms.Form):
    
    payment_method = forms.CharField(
        label="Payment Method:", max_length=200, widget=forms.HiddenInput(attrs={'class': 'form-control bg-transparent text-light','id':'id_target'}))

    contact_number = forms.CharField(
        label="Contact Number:", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}))
    
    ticket_id = forms.CharField(
        label="Product:", max_length=200, widget=forms.HiddenInput(attrs={'class': 'form-control bg-transparent text-light'}))
    
    Ticket = forms.CharField(
        label="Product:", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control bg-transparent text-light'}))
    
    price = forms.CharField(
        label="Price:", max_length=200, widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light','id':'price'}))
    
    total = forms.CharField(
        label="Total:", max_length=200, widget=forms.NumberInput(attrs={'class': 'form-control bg-transparent text-light','id':'total'}))
    

class Create_New_Category(forms.ModelForm):
    class Meta:     
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control bg-transparent text-light','placeholder': 'Write a Name'}),
            'description': forms.Textarea(attrs={'class':'form-control bg-transparent text-light','placeholder': 'Write a description'}),
        }
        
class Create_New_Zone(forms.ModelForm):
    
    image = forms.ImageField(  # Campo para la imagen
        widget=forms.ClearableFileInput(attrs={'class': 'form-control bg-transparent text-light'})
    )
    
    class Meta:
        model = Zona
        fields = ['nombre','descripcion','image']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control bg-transparent text-light','placeholder': 'Write a Name'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control bg-transparent text-light','placeholder': 'Write a description'}),
        }