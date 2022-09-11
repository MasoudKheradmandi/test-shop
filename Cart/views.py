from django.shortcuts import render,get_object_or_404,redirect
from .models import Order,OrderDetail
from product.models import Product
from .forms import NewOrderForm
from django.http import HttpResponse
import json
from payment.models import PayedOrder , PayedOrderDetail
from django.utils import timezone
from account.models import Profile
from account.forms import InfoForm
# Create your views here.
def add_user_order(request):
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
            if order is None:
                order = Order.objects.create(owner_id=request.user.id,is_paid=False)
    
        product_id =form.cleaned_data['product_id']    
        color = form.cleaned_data['color']
        size =form.cleaned_data['size']
        count = form.cleaned_data['count']
        
        product = Product.objects.get(id=product_id)
        
        if count < 1 or count > product.tedad_mahsole : 
            return redirect('/cart/')
        
        price_color = 0
        try:
            x = product.color_set.get(color=color)
            price_color = x.Ekhtelaf
        except:
            pass
        price_size = 0
        try:
            x = product.size_set.get(size=size)
            price_size = x.Ekhtelaf
        except:
            pass
        total_price = price_color + price_size + product.main_discount_cal(inti=True)
        if request.user.is_authenticated:
            if order.orderdetail_set.filter(product=product):
                order.orderdetail_set.filter(
                    product=product
                ).update(count=count,size=size,color=color,price=total_price)
            else:

                order.orderdetail_set.create(
                    product=product,price=total_price,count=count,size=size,color=color
                )
            return redirect('/cart')
        else:
            try:
                x = request.COOKIES['OrderDetail']
                jsonstyle = json.loads(x)
                jsonstyle[product_id] = {'id':product_id,'color':color,'size':size,'count':count}
                jsonstyle2 = json.dumps(jsonstyle)
                response = redirect('/cart')
                response.delete_cookie('OrderDetail')
                response.set_cookie('OrderDetail',jsonstyle2,172800)
                return response 
            except:
                order = Order.objects.create()
                response = redirect('/cart')
                x = {product_id:{'id':product_id,'color':color,'size':size,'count':count}}
                jsonstyle = json.dumps(x)
                response.set_cookie('OrderDetail',jsonstyle,172800)
                response.set_cookie('Order',order.id,172800)
                order.delete()
                return response 
    else:
        return redirect('/cart/')

def user_open_order(request):
    context = {
    'order':None,
    'details':None,
    'total':0,
    'sum':0,
    }
    if request.user.is_authenticated:
        open_order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        if open_order is not None:
            context['order'] = open_order
            context['details'] = open_order.orderdetail_set.all()
            # context ['sum'] =open_order.orderdetail_set.
            context['total'] = open_order.get_total_price()
    else:
        total_price = 0
        try :
            detail = request.COOKIES['OrderDetail']
            z = json.loads(detail)
            for det in z:
                # order_detail_list.append(det)
                id = z[det]['id']
                product = Product.objects.get(id=id)
                price_color = 0
                try:
                    x = product.color_set.get(color=z[det]['color'])
                    price_color = x.Ekhtelaf
                except:
                    pass
                price_size = 0
                try:
                    x = product.size_set.get(size=z[det]['size'])
                    price_size = x.Ekhtelaf
                except:
                    pass
                total_price_single = price_color + price_size + product.main_discount_cal(inti=True)
                total_price += total_price_single * z[det]['count']

            context['details'] = z
            context['total'] = total_price
        except:
            pass
        return render(request,'open_ano_order.html',context)


    return render(request,'user_open_order.html',context)

def remover_order_detail(request,product_id):
    # # order_detail = product_id
    # if product_id:
    #     order_detail = OrderDetail.objects.get(id=product_id)

    #     if order_detail:
    #         order_detail.delete()
    order = Order.objects.get(owner=request.user,is_paid=False)
    x = order.orderdetail_set.get(product_id = product_id)
    x.delete()
    return redirect('/cart')
 
def remove_from_cookie(request,id):
    x = request.COOKIES['OrderDetail']
    f = json.loads(x)
    del f[str(id)]
    m = json.dumps(f)
    response = redirect('/cart')
    response.delete_cookie('OrderDetail')
    response.set_cookie('OrderDetail',m,172800)
    return response

def order_payed(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except:
        return redirect('/info/')
    order = Order.objects.get(owner=request.user,is_paid=False)
    order.is_paid = True
    order.payment_date = timezone.now()
    order.save()
    payed_order = PayedOrder.objects.create(
        owner = request.user,payment_date= order.payment_date,
        city = profile.city , address= profile.address,username= request.user.username
    )
    for detail in order.orderdetail_set.all():
        PayedOrderDetail.objects.create(
            order = payed_order , product=detail.product ,price = detail.price,
            color = detail.color, size= detail.size , count=detail.count,
            
        )
    return HttpResponse('paid')
    



def addressView(request):
    context = {
        'form':InfoForm,
        'prof':Profile.objects.filter(user=request.user).last(),
        'total':0,
    }
    open_order = Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
    if open_order is not None:
        context['total'] = open_order.get_total_price()
    return render(request,'address.html',context)