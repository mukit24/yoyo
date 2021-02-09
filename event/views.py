from django.shortcuts import render,redirect,HttpResponse
from .models import Event,Contributer
from django.db.models import Q
from django.utils import timezone
from datetime import datetime,timedelta
from home.models import Contributer_Profile
from .forms import CreateEventForm
from django.contrib.auth.decorators import login_required 
# Create your views here.
def event_view(request):
    present_events = Event.objects.filter(is_present=True)
    previous_events = Event.objects.filter(is_present=False)
    
    # start_date = datetime.strptime('10/23/2020','%m/%d/%Y')
    # end_date = datetime.strptime('12/31/2020','%m/%d/%Y')
    # weekly = Contributer.objects.filter(created_on__date__range=[start_date.date(), end_date.date()])
    # # weekly = Contributer.objects.filter(created_on__date = end_date.date())
    # for i in weekly:
    #     print(i.created_on)

    context = {
        'events':present_events,
        'past':previous_events,
    }
    return render(request,'event/event_view.html',context)


def event_details(request,id):
    # print(datetime.datetime.now())
    # print(timezone.now())
    event = Event.objects.get(pk=id)
    cont = Contributer.objects.filter(event_no=event).order_by('-created_on')
    # print(cont)
    context = {
        'event':event,
        'contributers':cont,
    }
    return render(request,'event/event_details.html',context)

@login_required
def add_money(request,id):
    amount = int(request.POST['amount'])
    event = Event.objects.get(pk=id)
    try:
        temp = request.user.contributer
    except:
        return HttpResponse('<h1>Sorry You Dont Have A Contributer Profile</h1><h2>Please Create A Contributer Profile From Your Profile Section</h2>')
    if amount:
        contributer = Contributer(
            contributer=request.user.contributer,
            event_no= event,
            amount=amount,
            created_on=datetime.now(),
        )
        contributer.save()
        cont = Contributer_Profile.objects.get(id=request.user.contributer.id)
        cont.total_money = cont.total_money + amount
        cont.save()
        event.present_amount = event.present_amount + amount
        event.save()
        return redirect('event_details', id=id)


def create_event(request):
    form = CreateEventForm(request.POST or None)
    if form.is_valid():
        new_event = form.save(commit=False)
        new_event.volunteer = request.user.volunteer
        new_event.save()
        form.save_m2m()
        return redirect('event_details',new_event.id)
    context = {
        'form':form,
    }
    return render(request,"event/create_event.html",context)
