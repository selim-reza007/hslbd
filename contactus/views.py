from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import MessageRequest
from .models import Message

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

#Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore libero rem ab maxime, quos quis, fugiat quidem temporibus provident non laboriosam amet ex repellendus cumque soluta tenetur veniam nostrum nulla alias a ducimus ut qui nihil repellat. Minima facere non recusandae, eius, laudantium corrupti iure molestias, quo esse ad quaerat?

def requestedMsgView(request):
    data = Message.objects.all()
    return render(request, 'contactus/dashboard/messages-list.html', { 'messages' : data })

def messageDetailsView(request):
    if request.method == "POST":
        if 'messageId' in request.POST:
            datum = Message.objects.get(id=request.POST.get('messageId'))
            return render(request, 'contactus/dashboard/message-body.html', { 'message' : datum })

