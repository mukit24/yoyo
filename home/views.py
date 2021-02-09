from django.shortcuts import render,redirect
from .models import Contributer_Profile,Volunteer_Profile
from .forms import ContributerProfileForm,VolunteerProfileForm
from post.models import Post
from event.models import Event

def home_view(request):
    vol_list = Volunteer_Profile.objects.all().order_by('-total_points')[:5]
    con_list = Contributer_Profile.objects.all().order_by('-total_money')[:5]
    post_list = Post.objects.all().order_by('-created_on')[:4]
    events = Event.objects.filter(is_present=True)[:4]
    # points = []
    # for x in vol_list:
    #     points.append(int(x.total_points))
    # points.sort(reverse=True)
    print(vol_list)
    context = {
        'vol_list':vol_list,
        'con_list':con_list,
        'post_list':post_list,
        'events':events,
    }
    return render(request,"home/home_view.html",context)

def intermediate_profile(request):
    context = {

    }
    return render(request,"home/im_profile.html",context)


def create_volunteer_profile(request,id):
    form = VolunteerProfileForm()
    if request.method == 'POST':
        form = VolunteerProfileForm(request.POST,request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            form.save_m2m()
            return redirect('home_view')
    context = {
        'form':form,
    }
    return render(request,"home/v_profile_create.html",context)


def create_contributer_profile(request,id):
    form = ContributerProfileForm()
    if request.method == 'POST':
        form = ContributerProfileForm(request.POST,request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            form.save_m2m()
            return redirect('home_view')
    context = {
        'form':form,
    }
    return render(request,"home/c_profile_create.html",context)


def profile(request,id):
    try:
        volunteer = Volunteer_Profile.objects.get(user=id)
        print(volunteer)
    except:
        volunteer = ''
    try:
        contributer = Contributer_Profile.objects.get(user=id)
    except:
        contributer = ''
    context = {
        'v_profile':volunteer,
        'c_profile':contributer,
    }
    return render(request,"home/profile.html",context)


def update_volunteer_profile(request,id):
    vol = Volunteer_Profile.objects.get(id=id)
    form = VolunteerProfileForm(instance=vol)
    if request.method == 'POST':
        form = VolunteerProfileForm(request.POST,request.FILES,instance=vol)
        if form.is_valid():
            form.save()
            return redirect('profile',request.user.id)
    context = {
        'form':form,
    }
    return render(request,"home/update_v_profile.html",context)


def update_contributer_profile(request,id):
    con = Contributer_Profile.objects.get(id=id)
    form = ContributerProfileForm(instance=con)
    if request.method == 'POST':
        form = ContributerProfileForm(request.POST,request.FILES,instance=con)
        if form.is_valid():
            form.save()
            return redirect('profile',request.user.id)
    context = {
        'form':form,
    }
    return render(request,"home/update_c_profile.html",context)


def profile_view(request,id):
    try:
        volunteer = Volunteer_Profile.objects.get(user=id)
        print(volunteer)
    except:
        volunteer = ''
    try:
        contributer = Contributer_Profile.objects.get(user=id)
    except:
        contributer = ''
    context = {
        'v_profile':volunteer,
        'c_profile':contributer,
    }
    return render(request,"home/profile_view.html",context)


def point_table(request):
    vol_list = Volunteer_Profile.objects.all().order_by('-total_points')
    context = {
        'vol_list':vol_list,
    }
    return render(request,"home/point_table.html",context)


def contributer_table(request):
    con_list = Contributer_Profile.objects.all().order_by('-total_money')
    context = {
        'con_list':con_list,
    }
    
    return render(request,"home/contributer.html",context)

def about(request):
    return render(request,"home/about.html",{})

