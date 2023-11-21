from django.shortcuts import render, redirect
from .models import Category, Product, Sale, Tickets, Zona,Shipping_Address,Targets,Sale_Tickets
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from .forms import general_purchase_settings,Create_Address_Form,Create_Target_Form,Create_NEw_Product,Create_New_Ticket,general_purchase_settings_ticket,Create_New_Category,Create_New_Zone, CustomUserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse
from django.utils import timezone

# Create your views here.


def index(request):
    category = Category.objects.all()
    return render(request, 'index.html', {
        'category': category,
    })


def product_catalog(request, id):
    change_category = Category.objects.all()
    category = get_object_or_404(Category, id=id)
    product = Product.objects.filter(category_id=id)
    targets = Category.objects.all()
    return render(request, 'Articulo.html', {
        'category': category,
        'product': product,
        'elegir': change_category,
        'targets': targets
    })


def Detail(request, id):
    change_category = Category.objects.all()
    product_get = get_object_or_404(Product, id=id)
    product = Product.objects.get(id=id)
    return render(request, 'Detail.html', {
        'change_category': change_category,
        'product': product,
        'product_get': product_get
    })


def tickets(request):
    img = Zona.objects.filter(id=1)
    category = Category.objects.all()
    seating = Tickets.objects.all()
    zone = Zona.objects.all()
    return render(request, 'Tickets.html', {
        'category': category,
        'zone': zone,
        'img': img,
        'seating':seating
    })

def seating(request, id):
    zones = get_object_or_404(Zona, id=id)
    zone = Zona.objects.all()
    img = Zona.objects.filter(id=id)
    seating = Tickets.objects.filter(zona_id=id)
    category = Category.objects.all()
    all_seating = Tickets.objects.all()
    return render(request, 'Tickets.html', {
        'zones': zones,
        'zone': zone,
        'seating': seating,
        'category': category,
        'all_seating': all_seating,
        'img': img
    })


def SignUp(request):
    if request.method == 'GET':
        return render(request, 'SignUp.html', {
            'form': UserCreationForm
        })
    else:
        # Validamos contraseñas
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Creamos el usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                # Guardamos Usuario
                user.save()
                # Creamos la cockie para e usuario
                login(request, user)
                # Redireccionamos a a pagina principal.
                return redirect('index')
            except IntegrityError:
                return render(request, 'SignUp.html', {
                    'form': UserCreationForm,
                    'error': 'usename already exist'
                })
        else:
            return render(request, 'SignUp.html', {
                'form': UserCreationForm,
                'error': 'Password dont match'
            })

@login_required
def SignOut(request):
    logout(request)
    return redirect('index')


def SignIn(request):
    if request.method == 'GET':
        return render(request, 'SignIn.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'SignIn.html', {
                'form': AuthenticationForm
            })
        else:
            login(request, user)
            return redirect('index')

@login_required
def Buy_confirm(request, id):
    if request.method == 'GET':
        change_category = Category.objects.all()
        category = get_object_or_404(Product, id=id)
        product = Product.objects.get(id=id)
        address = Shipping_Address.objects.filter(user_id = request.user)
        target = Targets.objects.filter(user_id = request.user)
        form_general_setting = general_purchase_settings
        form_general_setting= general_purchase_settings(initial={'product': product.name,'product_id':product.id,'price':product.price})
        return render(request, 'Comprar.html', {
            'change_category': change_category,
            'category': category,
            'product': product,
            'form_general_setting' : form_general_setting,
            'address': address,
            'target':target
        }) 
    else:
        try:
            product = get_object_or_404(Product, id=id)
            delivery_address_id = request.POST.get('delivery_address')
            payment_method_id = request.POST.get('payment_method')
            delivery_address = get_object_or_404(Shipping_Address, id=delivery_address_id)
            payment_method = get_object_or_404(Targets, id=payment_method_id)
            
            Sale.objects.create(
            user=request.user,
            product=product,
            delivery_address=delivery_address,
            payment_method=payment_method,
            contact_number=request.POST['contact_number'],
            specifications=request.POST['delivery_specifications'],
            amount=request.POST['amount'],
            total=request.POST['total']
            )
            return redirect('Successful')
        except:
            change_category = Category.objects.all()
            category = get_object_or_404(Product, id=id)
            product = Product.objects.get(id=id)
            address = Shipping_Address.objects.filter(user_id = request.user)
            target = Targets.objects.filter(user_id = request.user)
            form_general_setting = general_purchase_settings
            form_general_setting= general_purchase_settings(initial={'product': product.name,'product_id':product.id,'price':product.price})
            return render(request, 'Comprar.html', {
                'change_category': change_category,
                'category': category,
                'product': product,
                'form_general_setting' : form_general_setting,
                'address': address,
                'target':target,
                'error': 'ERROR.'
            })
            
@login_required
def SuccessfulPurchase(request):
    return render(request,'successful purchase.html')


@login_required
def products_admin(request):
    change_category = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'Articulo_admin.html',{
        'change_category':change_category,
        'products': products
    })

@login_required
def product_admin(request,id = None):
    change_category = Category.objects.all()

    if id:
        products = Product.objects.filter(category = id)        
        category = Category.objects.get(id = id)
    else:
        products = Product.objects.all()
        category = None
        
    return render(request, 'Articulo_admin.html',{
        'change_category' : change_category,
        'products' : products,
        'category' : category
    })

@login_required
def New_address(request,id_product):
    if request.method == 'GET':
        return render(request,'Create_Address.html',{
            'form': Create_Address_Form
        })
    else:
        try:
            form = Create_Address_Form(request.POST)
            new_address = form.save(commit=False)
            new_address.user = request.user
            new_address.save()
            compra_url = reverse('buy',args=[id_product])
            return redirect(compra_url)
        except ValueError:
           return render(request,'Create_Address.html',{
            'form': Create_Address_Form,
            'error': 'Pleace provide valid data'
        })

@login_required           
def New_target(request,id_product):
    if request.method == 'GET':
        return render(request,'Create_Target.html',{
            'form': Create_Target_Form
        })
    else:
        try:
            form = Create_Target_Form(request.POST)
            new_target = form.save(commit=False)
            new_target.user = request.user
            new_target.save()
            compra_url = reverse('buy',args=[id_product])
            return redirect(compra_url)
        except ValueError:
           return render(request,'Create_Target.html',{
            'form': Create_Target_Form,
            'error': 'Pleace provide valid data'
        })

@login_required    
def Address_Delete(request,id,id_product):
    address = get_object_or_404(Shipping_Address, id = id, user = request.user)
    address.delete()
    compra_url = reverse('buy',args=[id_product])
    return redirect(compra_url)

@login_required
def Target_Delete(request,id,product_id):
    target = get_object_or_404(Targets, id = id, user = request.user)
    target.delete()
    compra_url = reverse('buy',args=[product_id])
    return redirect(compra_url)

@login_required
def Update_Address(request,id,product_id):
    if request.method == 'GET':
        address = get_object_or_404(Shipping_Address, id = id, user = request.user)
        form = Create_Address_Form(instance=address)
        return render(request,'Create_Address.html',{
            'address': address,
            'form':form
        })
    else:
        try:
            address = get_object_or_404(Shipping_Address, id = id, user = request.user)
            form = Create_Address_Form(request.POST,instance=address)
            form.save()
            compra_url = reverse('buy',args=[product_id])
            return redirect(compra_url)
        except ValueError:
            return render(request,'Create_Address.html',{
            'address': address,
            'form':form,
            'error':'Error updating Address'
        })
            
@login_required
def Update_Target(request,id,target_id):
    if request.method == 'GET':
        target = get_object_or_404(Targets, id= id, user = request.user)
        form = Create_Target_Form(instance=target)
        return render(request,'Create_Target.html',{
            'target':target,
            'form' : form
        })
    else:
        try:
            target = get_object_or_404(Targets, id= id, user = request.user)
            form = Create_Target_Form(request.POST, instance=target)
            form.save()
            compra_url = reverse('buy',args=[target_id])
            return redirect(compra_url)
        except ValueError:
            target = get_object_or_404(Targets, id= id, user = request.user)
            form = Create_Target_Form(instance=target)
            return render(request,'Create_Target.html',{
                'target':target,
                'form' : form,
                'error': 'Error updating Target'
            })
            
def Shopping_History(request):
    change_category = Category.objects.all()
    sales = Sale.objects.filter(user = request.user)
    sales_tickets = Sale_Tickets.objects.filter(user = request.user)
    return render(request,'S_history.html',{
        'change_category':change_category,
        'sales':sales,
        'sales_tickets':sales_tickets
    })
    
def SaleP_Detail(request,id):
    sale = Sale.objects.get(id = id)
    return render(request,'SaleP_detail.html',{
        'sale': sale
    })

def SalesT_Detail(request,id):
    sales = Sale_Tickets.objects.get(id = id)
    return render(request,'saleT_detail.html',{
        'sale':sales
    })
      
def Sale_COmpleted(request,id):
    
    sale = get_object_or_404(Sale,id = id, user = request.user)
    if request.method == 'POST':
        sale.deadline = timezone.now()
        sale.save()
        return redirect('shopping_history')
    
def Buy_Tickets(request,id):
    if request.method == 'GET':
        change_category = Category.objects.all()
        ticket = Tickets.objects.get(id = id)
        target = Targets.objects.filter(user_id = request.user)
        form_general_purchase_settings =  general_purchase_settings_ticket(initial={
            'ticket_id':ticket.id,'Ticket':ticket.name,'price':ticket.Precio,'total':ticket.Precio
        })
        return render(request, 'Buy_Tickets.html',{
            'change_category':change_category,
            'ticket': ticket,
            'target':target,
            'general_purchase_settings_ticket': form_general_purchase_settings,
            
        })
    else:
        try:
            ticket = get_object_or_404(Tickets, id=id)
            payment_method_id = request.POST.get('payment_method')
            payment_method = get_object_or_404(Targets, id=payment_method_id)
            ticket.comprado = True
            ticket.save()
            Sale_Tickets.objects.create(
            user=request.user,
            ticket=ticket,
            payment_method=payment_method,
            contact_number=request.POST['contact_number'],
            total=request.POST['total']
            )
            return redirect('Successful')
        except:
            change_category = Category.objects.all()
            ticket = Tickets.objects.get(id = id)
            target = Targets.objects.filter(user_id = request.user)
            form_general_purchase_settings =  general_purchase_settings_ticket(initial={
                'ticket_id':ticket.id,'Ticket':ticket.name,'price':ticket.Precio,'total': ticket.Precio
            })
            
            return render(request, 'Buy_Tickets.html',{
                'change_category':change_category,
                'ticket': ticket,
                'target':target,
                'general_purchase_settings_ticket': form_general_purchase_settings,
                'error': 'Pleace Provid Valid Data'
                
            })
            
@login_required           
def New_target_ticket(request,id_ticket):
    if request.method == 'GET':
        return render(request,'Create_Target.html',{
            'form': Create_Target_Form
        })
    else:
        try:
            form = Create_Target_Form(request.POST)
            new_target = form.save(commit=False)
            new_target.user = request.user
            new_target.save()
            compra_url = reverse('buy_tickets',args=[id_ticket])
            return redirect(compra_url)
        except ValueError:
           return render(request,'Create_Target.html',{
            'form': Create_Target_Form,
            'error': 'Pleace provide valid data'
        })

@login_required
def Target_Delete_ticket(request,id,ticket_id):
    target = get_object_or_404(Targets, id = id, user = request.user)
    target.delete()
    compra_url = reverse('buy_tickets',args=[ticket_id])
    return redirect(compra_url)

@login_required
def Update_Target_ticket(request,id,ticket_id):
    if request.method == 'GET':
        target = get_object_or_404(Targets, id= id, user = request.user)
        form = Create_Target_Form(instance=target)
        return render(request,'Create_Target.html',{
            'target':target,
            'form' : form
        })
    else:
        try:
            target = get_object_or_404(Targets, id= id, user = request.user)
            form = Create_Target_Form(request.POST, instance=target)
            form.save()
            compra_url = reverse('buy_tickets',args=[ticket_id])
            return redirect(compra_url)
        except ValueError:
            target = get_object_or_404(Targets, id= id, user = request.user)
            form = Create_Target_Form(instance=target)
            return render(request,'Create_Target.html',{
                'target':target,
                'form' : form,
                'error': 'Error updating Target'
            })

#Apartados de Administrador
def user_has_admin_permissions(user):
    # Comprueba si el usuario tiene permisos de administrador.
    # Esto es solo un ejemplo, debes ajustarlo según tus necesidades.
    return user.is_authenticated and user.is_staff


@user_passes_test(user_has_admin_permissions)
def Create_Products(request):
    if request.method == 'GET':
        return render(request, 'Create_Product.html',{
            'form': Create_NEw_Product
        })
    else:
        try:
            form = Create_NEw_Product(request.POST, request.FILES)
            if form.is_valid():
                new_product = form.save(commit=False)
                new_product.category = form.cleaned_data['category']
                new_product.save()
                admin_url = reverse('product_admin',args=[1])
                return redirect(admin_url)
        except:
            return render(request, 'Create_Product.html', {
                'form': form,
                'error': 'Invalid data. Please check the form.'
            })

@user_passes_test(user_has_admin_permissions)
def Update_Product(request,id):
    if request.method == 'GET':
        product = get_object_or_404(Product,id = id)
        form = Create_NEw_Product(instance=product)
        return render(request,'Create_Product.html',{
            'product':product,
            'form':form
        })
    else:
        try:
            product = get_object_or_404(Product,id = id)
            form = Create_NEw_Product(request.POST,request.FILES,instance=product)
            form.save()
            admin_url = reverse('product_admin',args=[1])
            return redirect(admin_url)
        except:
            product = get_object_or_404(Product,id = id)
            form = Create_NEw_Product(instance=product)
            return render(request,'Create_Product.html',{
                'product':product,
                'form':form,
                'error': 'Error updating Product'
            })
            
@user_passes_test(user_has_admin_permissions)
def Product_Delete(request,id):
    product = get_object_or_404(Product,id = id)
    product.delete()
    admin_url = reverse('product_admin',args=[1])
    return redirect(admin_url)

@user_passes_test(user_has_admin_permissions)
def Tickets_admin(request):
    change_category = Zona.objects.all()
    tickets = Tickets.objects.all()
    return render(request,'all_tickets_admin.html',{
        'change_category':change_category,
        'tickets': tickets
    })
    
@user_passes_test(user_has_admin_permissions)
def Ticket_admin(request,id):
    change_category = Zona.objects.all()
    tickets = Tickets.objects.filter(zona_id = id)
    zone = Zona.objects.get(id = id)
    return render(request,'Ticekts_admin.html',{
        'change_category':change_category,
        'tickets': tickets,
        'zone':zone,
    })

@user_passes_test(user_has_admin_permissions)
def Sales_Ad(request):
    sales = Sale.objects.all()
    return render(request,'Sales_Admin.html',{
        'sales':sales
    })
    
@user_passes_test(user_has_admin_permissions)
def SalesT_Ad(request):
    sales = Sale_Tickets.objects.all()
    return render(request,'SalesT_admin.html',{
        'sales':sales
    })
    
@user_passes_test(user_has_admin_permissions)
def Detilss_Adm(request,id):
    sale = Sale.objects.get(id = id)
    return render(request,'Details_Admin.html',{
        'sale': sale
    })
    
@user_passes_test(user_has_admin_permissions)
def DetilssT_Adm(request,id):
    sale = Sale_Tickets.objects.get(id = id)
    return render(request,'DetailsT_Admin.html',{
        'sale': sale
    })

@user_passes_test(user_has_admin_permissions)
def CategoryAdmin(request):
    change_category = Category.objects.all()
    return render(request,'category_admin.html',{
        'change_category':change_category,
    })

@user_passes_test(user_has_admin_permissions)
def New_Category(request):
    if request.method == 'GET':
        return render(request, 'new_category.html',{
            'form':Create_New_Category
        })
    else:
        try:
            form = Create_New_Category(request.POST)   
            if form.is_valid():
                form.save()
                return redirect('CategoryAdmin')
        except IntegrityError:
            return render(request, 'new_category.html',{
                'form':Create_New_Category,
                'error':'Invalid data. Please check the form.'
            })
    return render(request, 'new_category.html', {
        'form': Create_New_Category,
        'error': 'Invalid data. Please check the form.'
        })

@user_passes_test(user_has_admin_permissions)
def Update_Category(request,id):
    change_category = Category.objects.all()
    if request.method == 'GET':
        category = get_object_or_404(Category,id = id)
        form = Create_New_Category(instance = category)
        return render(request,'update_category.html',{
            'category':category,
            'form':form,
            'change_category':change_category
        })
    else:
        try:
            category = get_object_or_404(Category,id = id)
            form = Create_New_Category(request.POST,instance= category)
            form.save()
            return redirect('CategoryAdmin')
        except IntegrityError:
            change_category = Category.objects.all()
            category = get_object_or_404(Category,id = id)
            form = Create_New_Category(instance = category)
            return render(request,'update_category.html',{
                'category':category,
                'form':form,
                'change_category':change_category,
                'error':'Error updating Category'
            })
            
@user_passes_test(user_has_admin_permissions)
def Delete_Category(request,id):
    category = get_object_or_404(Category,id = id)
    category.delete()
    return redirect('CategoryAdmin')

@user_passes_test(user_has_admin_permissions)
def New_Zone(request):
    if request.method == 'GET':
        return render(request,'create_zone.html',{
            'form':Create_New_Zone
        })
    else:
        try:
            form = Create_New_Zone(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('tickets_admin')
            else:
                return render(request,'create_zone.html',{
                    'form':Create_New_Zone,
                    'error':'Invalid data. Please check the form.'
                })
        except:
            return render(request,'create_zone.html',{
                    'form':Create_New_Zone,
                    'error':'Invalid data. Please check the form.'
                })
            
@user_passes_test(user_has_admin_permissions)
def New_Ticket(request):
    if request.method == 'GET':
        return render(request,'create_ticket.html',{
            'form':Create_New_Ticket
        })
    else:
        try:
            form = Create_New_Ticket(request.POST)
            if form.is_valid():
                form.save()
                return redirect('tickets_admin')
            else:
                return render(request,'create_ticket.html',{
                'form':Create_New_Ticket,
                'error': 'Invalid data. Please check the form.'
            })    
        except IntegrityError:
            return render(request,'create_ticket.html',{
                'form':Create_New_Ticket,
                'error': 'Invalid data. Please check the form.'
            })
            
@user_passes_test(user_has_admin_permissions)
def Delete_Zone(request,id):
    zone = get_object_or_404(Zona, id = id)
    zone.delete()
    return redirect('tickets_admin')

@user_passes_test(user_has_admin_permissions)
def Update_Zone(request,id):
    if request.method == 'GET':
        zone = get_object_or_404(Zona,id = id)
        return render(request,'update_zone.html',{
            'form':Create_New_Zone(instance= zone)
        })
    else:
        try:
            zone = get_object_or_404(Zona,id = id)
            form = Create_New_Zone(request.POST, instance=zone)
            form.save()
            return redirect('tickets_admin')
        except:
            zone = get_object_or_404(Zona,id = id)
            return render(request,'update_zone.html',{
                'form':Create_New_Zone(instance= zone),
                'error': 'Error updating Zone'
            })
            
@user_passes_test(user_has_admin_permissions)
def Delete_Ticket(request,id):
    ticket = get_object_or_404(Tickets, id = id)
    ticket.delete()
    return redirect('tickets_admin')

@user_passes_test(user_has_admin_permissions)
def Update_Ticket(request,id):
    if request.method == 'GET':
        ticket = get_object_or_404(Tickets,id = id)
        return render(request, 'update_ticket.html',{
            'form': Create_New_Ticket(instance=ticket)
        })
    else:
        try:
            ticket = get_object_or_404(Tickets,id = id)
            form = Create_New_Ticket(request.POST, instance=ticket)
            form.save()
            return redirect('tickets_admin')
        except:
            ticket = get_object_or_404(Tickets,id = id)
            return render(request, 'update_ticket',{
                'form': Create_New_Ticket(instance=ticket),
                'error': 'Error updating Ticket'
            })
            
def register_super_user(request):
    if request.method == 'GET':
        return render(request, 'create_superUser.html', {
            'form': CustomUserCreationForm()
        })
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            user = form.save()
            # Asignar permisos de administrador al nuevo usuario
            group = Group.objects.get(name='Administradores')
            user.groups.add(group)
            login(request, user)
            return redirect('index')  # Ajusta la redirección según tu configuración
        else:
            print("Formulario no válido:", form.errors)

    return render(request, 'create_superUser.html', {'form': form})