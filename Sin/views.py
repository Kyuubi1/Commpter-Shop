from django.shortcuts import render, redirect
from django.views import View
from .forms import Login, Signup, UpdateAccount, ServiceRegister, ServiceAssign, Carts, Pay, ReportForm
from django.contrib.auth import authenticate, login
from .models import Account, Product, Service, FixService, Cart, Report
from django.views.generic import FormView


class ClassIndex(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, 'Sin/index.html', {'product': product})


class ClassLogin(View):

    def get(self, request):
        lg = Login()
        return render(request, 'Sin/Login.html', {'login': lg})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user_login = authenticate(username=username, password=password)

        if user_login is None:
            lg = Login()
            context = {'login': lg, 'flag': True}
            return render(request, 'Sin/Login.html', context)
        login(request, user_login)
        return redirect('Sin:home')


class Logout(View):
    def get(self):
        return redirect('Sin:index')


class SignupView(FormView):
    template_name = 'Sin/sign-up.html'
    form_class = Signup

    def form_valid(self, form):
        user = Account()
        user.username = form.cleaned_data.get('username')
        user.set_password(form.cleaned_data.get('password'))
        user.email = form.cleaned_data.get('email')
        user.phone = form.cleaned_data.get('phone')
        user.sex = form.cleaned_data.get('sex')
        user.save()
        user.refresh_from_db()
        lg = Login()
        return render(self.request, 'Sin/Login.html', {'login': lg})


class InforUser(View):
        def get(self, request):
            user = request.user
            return render(request, 'Sin/infor.html', {'user': user, 'acc': user})


class AccountUpdate(View):
    def get(self, request):
        acc = request.user
        user = UpdateAccount()
        return render(request, 'Sin/update.html', {'user': user, 'acc': acc})

    def post(self, request):
        acc = request.user
        user = Account.objects.get(id=request.user.id)
        user.set_password(request.POST['password'])
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.phone = request.POST['phone']
        user.address = request.POST['address']
        user.save()
        return render(request, 'Sin/infor.html', {'user': user, 'acc': acc})


class ServiceView(View):
    def get(self, request):
        acc = request.user
        return render(request, 'Sin/service.html', {'acc': acc})


class HomeView(View):
    def get(self, request):
        user = request.user
        product = Product.objects.all()
        return render(request, 'Sin/shop.html', {'acc': user, 'product': product})


class DetailProduct(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        cart = Carts()
        acc = request.user
        list_product = Product.objects.all().order_by('category')
        return render(request, 'Sin/detail_product.html', {'product': product, 'lists': list_product, 'acc': acc, 'cart': cart})

    def post(self, request, product_id):
        form = Carts(request.POST)
        number = form.data['number']
        print(number)
        cart = Cart()
        cart.number = number
        cart.product = Product.objects.get(id=product_id)
        cart.user = request.user
        cart.save()
        return redirect('Sin:home')


class RegisterService(FormView):
    template_name = 'Sin/register_service.html'
    form_class = ServiceRegister

    def form_valid(self, form):
        service = Service()
        service.customer_name = form.cleaned_data.get('customer_name')
        service.phone = form.cleaned_data.get('phone')
        service.address = form.cleaned_data.get('address')
        service.save()
        service.refresh_from_db()
        return redirect('Sin:success_register')


class SuccessRegister(View):
    def get(self, request):
        acc = request.user
        return render(request, 'Sin/complete_register.html', {'acc': acc})


class ServiceAssignee(View):
    def get(self, request):
        acc = request.user
        employee = Account.objects.filter(is_staff=True)
        fix = Service.objects.all()
        product = Product.objects.all()
        return render(request, 'Sin/assignee.html', {'acc': acc, 'employee': employee, 'fix': fix, 'product': product})

    def post(self, request):
        acc = request.user
        form = ServiceAssign(request.POST)
        employee = form.data['employee']
        product = form.data['product']
        fix = form.data['customer']
        error = form.data['error']
        is_guarantee = form.data['choice']
        em = Account.objects.get(username=employee)
        pro = Product.objects.get(name=product)
        fi = Service.objects.get(customer_name=fix)
        fix_service = FixService()
        fix_service.product = pro
        fix_service.employee = em
        fix_service.fix = fi
        fix_service.is_guarantee = is_guarantee
        fix_service.error = error
        fix_service.save()
        return redirect('Sin:home')


class Infor:
    def __init__(self, cart, cost):
        self.cart = cart
        self.cost = cost


class BoxProduct(View):
    def get(self, request):
        acc = request.user
        cart = Cart.objects.filter(user=acc)
        cart_infor = []
        costs = []
        for item in cart:
            cost = item.product.cost * item.number
            costs.append(cost)
            carts = Infor(item, cost)
            cart_infor.append(carts)
        s = 0
        for ct in costs:
            s = s+ct
        return render(request, 'Sin/cart.html', {'acc': acc, 'carts': cart_infor, 'total': s})


class DeleteProduct(View):
    def post(self, request, cart_id):
        car = Cart.objects.filter(id=cart_id)
        print(car)
        return redirect('Sin:home')


class AssigneeDetail(View):
    def get(self, request):
        acc = request.user
        detail = FixService.objects.filter(employee=request.user)
        return render(request, 'Sin/fixed_form_assignee.html', {'detail': detail, 'acc': acc})


class ReportView(View):
    def get(self, request):
        acc = request.user
        data_fix = FixService.objects.filter(employee=request.user)
        employee = Account.objects.filter(is_staff=True)
        return render(request, 'Sin/report.html', {'data_fix': data_fix, 'acc': acc, 'employee': employee})

    def post(self, request):
        form = ReportForm(request.POST)
        fixed = form.data['fixed']
        assignee = form.data['assignee']
        type_report = form.data['choice']
        is_fixed = form.data['choose']
        em = Account.objects.get(username=assignee)
        fi = FixService.objects.get(error=fixed)
        rp = Report()
        rp.fixed = fi
        rp.assignee = em
        rp.is_fixed = is_fixed
        rp.type_report = type_report
        rp.save()

        return redirect('Sin:assignee_detail')



