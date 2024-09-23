from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import MessageRequest
from .models import Message
from django.core.paginator import Paginator

# Create your views here.
def contactUsView(request):
    if request.method == "POST":
        form = MessageRequest(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'We have received your message. We will contact you soon.')
            return redirect('contactus:contactus')
        else:
            return render(request, 'contactus/contact-us.html', { 'form' : form })
    else:
        form = MessageRequest()
        return render(request, 'contactus/contact-us.html', { 'form' : form })

def requestedMsgView(request):
    data = Message.objects.all().order_by('-id')
    myPaginator = Paginator(data, 9)
    page_number = request.GET.get('page')
    page_obj = myPaginator.get_page(page_number)

    # return render(request, 'contactus/dashboard/messages-list.html', { 'messages' : data })
    return render(request, 'contactus/dashboard/messages-list.html', { 'messages' : page_obj })

def messageDetailsView(request, slug):
    datum = Message.objects.get(id=slug)
    datum.messageRead = True
    datum.save()
    return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })

def updateMsgStatus(request):
    if request.method == "POST":
        if 'msgId' in request.POST:
            datum = Message.objects.get(id=request.POST.get('msgId'))
            datum.status = True
            datum.save()
            return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })

def deleteMsg(request, slug):
    if request.method == "POST":
        datum = Message.objects.get(id=slug)
        datum.delete()
        return redirect('contactus:requested-msg')

def unreadMsgCount(request):
    data = Message.objects.filter(messageRead=False).count()
    return data



