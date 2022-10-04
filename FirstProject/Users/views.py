from django.shortcuts import render,redirect
from django.contrib import messages
from Users.forms import UserForm,UserUpdateForm,UpdateProfileForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.You can please LogIn.')
            user_form.save()
            return redirect('login')
    else:
        user_form = UserForm()
    context = {'user_form' : user_form}
    return render(request,'Users/register.html',context)


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {'u_form' : u_form,'p_form' : p_form}
    return render(request,'Users/profile.html',context)

 