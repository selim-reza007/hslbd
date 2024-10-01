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
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'We have received your message. We will contact you soon.')
                return redirect('contactus:contactus')
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
        else:
            return render(request, 'contactus/contact-us.html', { 'form' : form })
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
        return render(request, 'contactus/dashboard/messages-list.html', { 'messagesData' : page_obj })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

#displaying message info in dashboard
@login_required(login_url='/admin/')
def messageDetailsView(request, id):
    datum = get_object_or_404(Message, id=id)
    datum.messageRead = True
    try:
        datum.save()
        return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })
    except IntegrityError:
        return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

#updating requested message status from false to true 
@login_required(login_url='/admin/')
def updateMsgStatus(request):
    if request.method == "POST":
        if 'msgId' in request.POST:
            datum = get_object_or_404(Message, id=request.POST.get('msgId'))
            datum.status = True
            try:
                datum.save()
                return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })
            except IntegrityError:
                return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
            except DatabaseError:
                return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })
            
#delete message
@login_required(login_url='/admin/')
def deleteMsg(request, id):
    if request.method == "POST":
        datum = get_object_or_404(Message, id=id)
        try:
            datum.delete()
            messages.success(request, f"Message sent from {datum.email} has been deleted.")
            return redirect('contactus:requested-msg')
        except IntegrityError:
            return render(request, 'Error.html', { 'errorMsg' : 'Integrity error occured!' })
        except DatabaseError:
            return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })

#counting the number of unread messages
@login_required(login_url='/admin/')
def unreadMsgCount(request):
    try:
        data = Message.objects.filter(messageRead=False).count()
        return data
    except DatabaseError:
        return render(request, 'Error.html', { 'errorMsg' : 'Database error occured!' })