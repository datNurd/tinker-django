from django.shortcuts import render
from .forms import MerchantProfileForm, MerchantForm
# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        merchant_form = MerchantForm(data=request.POST)
        merchant_profile_form = MerchantProfileForm(data=request.POST)

        if merchant_form.is_valid() and merchant_profile_form.is_valid():
            user = merchant_form.save()
            user.set_password(user.password)
            user.save()
            profile = merchant_profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print merchant_form.errors, merchant_profile_form.errors
    else:
        merchant_form = MerchantForm()
        merchant_profile_form = MerchantProfileForm()
    return render(request,'merchant/register.html',{'merchant_form':merchant_form,'merchant_profile_form':merchant_profile_form,'registered':registered})
