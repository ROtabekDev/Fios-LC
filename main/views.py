from django.shortcuts import render

from .models import Contact, Appeal


def home_page(request):
    return render(request, "home page.html", )


def about_page(request):
    return render(request, "about.html", )


def courses_page(request):
    return render(request, "courses.html", )


def contact_page(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        text = request.POST['text']
        contact = Contact(name=name, phone=phone, text=text)
        contact.save()

        return render(request, "contact.html", {'name': name,
                                                'phone': phone,
                                                'text': text})
    return render(request, "contact.html")


def appeal_page(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']
        appeal = Appeal(
            firstname=firstname, lastname=lastname, phone=phone, email=email, text=text
        )
        appeal.save()

        return render(request, "appeal.html", {'firstname': firstname,
                                               'lastname': lastname,
                                               'phone': phone,
                                               'email': email,
                                               'text': text})
    return render(request, "appeal.html",)
