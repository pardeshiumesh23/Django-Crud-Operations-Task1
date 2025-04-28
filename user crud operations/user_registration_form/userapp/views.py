from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm

def user_list(request):
    users = UserProfile.objects.all()
    return render(request, 'userapp/user_list.html', {'users': users})

def user_create(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm()
    return render(request, 'userapp/user_form.html', {'form': form})

def user_update(request, pk):
    user = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'userapp/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(UserProfile, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'userapp/user_confirm_delete.html', {'user': user})