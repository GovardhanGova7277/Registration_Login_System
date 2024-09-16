from django.shortcuts import render, redirect
from .models import People
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import never_cache

# Create your views here.


def index(request):
    return render(request, "index.html")

# Using @never_cache means that every time a user requests that view, the server will generate a fresh response instead of potentially serving an outdated or incorrect cached version.

# The @never_cache decorator is used to prevent a Django view from being cached. This can be useful for views that generate dynamic content, such as views that display the current time or the results of a database query.
@never_cache
def register(request):
    # when the form is submitted
    print(request)
    if request.method == "POST":
        fn = request.POST["firstName"]
        ln = request.POST["secondName"]
        ph = request.POST["phoneNo"]
        em = request.POST["email"]
        pwd = request.POST["password"]
        rpwd = request.POST["rpassword"]
        gen = request.POST["gender"]
        hob = request.POST.getlist(
            "hobbies"
        )  # while retrieving multiple values from check box retrieve like this
        con = request.POST["country"]

        print(fn, ln, ph, em, pwd, rpwd, gen, hob, con)

        # to encrypt the password
        enc_pwd = make_password(pwd, salt="123")

        my_hob = ",".join(hob)

        if pwd != rpwd:
            messages.error(request, "Password Mismatch")
        else:
            try:
                ppl = People(
                    first_name=fn,
                    last_name=ln,
                    phone=ph,
                    email=em,
                    password=enc_pwd,
                    gender=gen,
                    hobbies=my_hob,
                    country=con,
                )
                ppl.save()

                messages.success(request, "User Registered")
            except Exception as ex:
                messages.error(request, ex)

        return render(request, "register.html")

    else:
        return render(request, "register.html")


@never_cache
def login(request):
    if request.method == "POST":
        entered_email = request.POST["email"]
        entered_pwd = request.POST["password"]

        # to encrypt the password
        enc_entered_pwd = make_password(entered_pwd, salt="123")

        if People.objects.filter(
            email=entered_email, password=enc_entered_pwd
        ).exists():
            messages.success(request, "Valid Login")

            ppl = People.objects.get(email=entered_email, password=enc_entered_pwd)
            pid = ppl.id

            # setting session object
            request.session["my_email"] = entered_email
            request.session["my_pid"] = pid

            return redirect(home)  # view function name
            # return redirect('home_page')  # URL NAME
        else:
            messages.error(request, "Invalid Login")

    return render(request, "login.html")


@never_cache
def home(request):
    if "my_email" in request.session:
        my_em = request.session["my_email"]
        context = {"my_em": my_em}
        return render(request, "home.html", context)
    else:
        return redirect("login_page")  # URL Name


@never_cache
def pwd(request):
    if "my_email" in request.session:
        my_em = request.session["my_email"]
        context = {"my_em": my_em}

        if request.method == "POST":
            em = request.POST["email"]
            op = request.POST["opwd"]
            np = request.POST["npwd"]

            enc_op = make_password(op, salt="123")
            enc_np = make_password(np, salt="123")

            if People.objects.filter(email=em, password=enc_op).exists():
                my_pid = request.session["my_pid"]

                p = People()
                p.id = my_pid
                p.password = enc_np
                p.save(update_fields=["password"])
                messages.success(request, "Password Updated")
            else:
                messages.error(request, "Your Information didnt match")

        return render(request, "pwd.html", context)
    else:
        return redirect("login_page")  # URL Name


@never_cache
def profile(request):
    if "my_email" in request.session:
        my_em = request.session["my_email"]
        user = People.objects.get(email=my_em)
        context = {"my_em": my_em, "user": user}
        return render(request, "profile.html", context)
    else:
        return redirect("login_page")  # URL Name


@never_cache
def logout(request):
    if "my_email" in request.session:
        del request.session["my_email"]
    return render(request, "logout.html")
