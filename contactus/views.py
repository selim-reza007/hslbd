from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from .forms import MessageRequest
from .models import Message
from django.core.paginator import Paginator
from django.db import IntegrityError, DatabaseError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
#rendering the view of contactus from which customer can send message
def contactUsView(request):
    if request.method == "POST":
        form = MessageRequest(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'We have received your message. We will contact you soon.')
                return redirect('contactus:contactus')
            else:
                return render(request, 'contactus/contact-us.html', { 'form' : form })
        except IntegrityError:
            return HttpResponse("Integrity error occured")
        except DatabaseError:
            return HttpResponse("Database error occured")
    else:
        form = MessageRequest()
    return render(request, 'contactus/contact-us.html', { 'form' : form })

#listing all received message in dashboard view
@login_required(login_url='/admin/')
def requestedMsgView(request):
    try:
        data = Message.objects.all().order_by('-id')
        myPaginator = Paginator(data, 9)
        page_number = request.GET.get('page')
        page_obj = myPaginator.get_page(page_number)
    except IntegrityError:
        return HttpResponse("Integrity error occured")
    except DatabaseError:
        return HttpResponse("Database error occured")
    return render(request, 'contactus/dashboard/messages-list.html', { 'messagesData' : page_obj })

#displaying message info in dashboard
@login_required(login_url='/admin/')
def messageDetailsView(request, slug):
    datum = get_object_or_404(Message, id=slug)
    datum.messageRead = True
    try:
        datum.save()
        return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })
    except IntegrityError:
        return HttpResponse("Integrity error occured!")

#updating requested message status from false to true 
@login_required(login_url='/admin/')
def updateMsgStatus(request):
    if request.method == "POST":
        if 'msgId' in request.POST:
            try:
                datum = get_object_or_404(Message, id=request.POST.get('msgId'))
                datum.status = True
                datum.save()
                return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })
            except IntegrityError:
                return HttpResponse("Integrity error occured")
            except DatabaseError:
                return HttpResponse("Database error occured")
            
#delete message
@login_required(login_url='/admin/')
def deleteMsg(request, slug):
    if request.method == "POST":
        datum = get_object_or_404(Message, id=slug)
        try:
            datum.delete()
            messages.success(request, f"Message sent from {datum.email} has been deleted.")
        except IntegrityError:
            return HttpResponse("An error occurred while trying to delete the message.")
        return redirect('contactus:requested-msg')

#counting the number of unread messages
@login_required(login_url='/admin/')
def unreadMsgCount(request):
    try:
        data = Message.objects.filter(messageRead=False).count()
    except DatabaseError:
        return HttpResponse("Database error occured")
    return data