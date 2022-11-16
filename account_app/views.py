from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from account_app.models import UserAccount
from account_app.forms import RegistrationForm
from account_app.tokens import account_activation_token


@login_required
def dashboard(request):
    return render(request, 'account_app/user/dashboard.html')


def account_register(request):

    if request.user.is_authenticated:
        return redirect('account_app:dashboard')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            user.is_active = False
            user.save()
            
            #set-up email
            current_site = get_current_site(request)
            subject = 'Activeate your Account'
            message = render_to_string(
                'account_app/registration/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
            user.email_user(subject=subject, message=message)
            
            return HttpResponse('Registered successfully and activation sent!')

    else:
        register_form = RegistrationForm()

    context = {'form': register_form}
    return render(request, 'account_app/registration/register.html', context)


def account_activate(request, uidb64, token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserAccount.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('account_app:dashboard')
    else:
        return redirect(request, 'account/registraion/activation_invalid.html')









    
