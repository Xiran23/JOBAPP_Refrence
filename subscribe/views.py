from django.shortcuts import redirect, render
from django.urls import reverse

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe

def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty =" "
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe_form.save()
            # print("Valid form")
            # print(subscribe_form.cleaned_data)
            # email =subscribe_form.cleaned_data['email']
            # first_name =subscribe_form.cleaned_data['first_name']
            # last_name =subscribe_form.cleaned_data['last_name']
            # subscribe = Subscribe(first_name = first_name,last_name = last_name,email= email)
            # subscribe.save()
            return redirect(reverse('thank_you'))

        # email = request.POST['email']
        # first_name = request.POST['firstname']
        # last_name = request.POST["lastname"]
        # print("post request:", email)
        # if email == "":
        #     email_error_empty = "no email entered"

        # subscribe = Subscribe(first_name = first_name,last_name = last_name,email= email)
        # subscribe.save()
    context = {"email_error_empty":email_error_empty,"form":subscribe_form}
    return render(request,'subscribe/subscribe.html',context)

# Create your views here.


def thank_you(request):
    context={}
    return render(request,'subscribe/thank_you.html',context)
