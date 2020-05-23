from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from mail_sender import settings

# Create your views here.

def index(request):
    return render(request,"mail/index.html")
"""
def testmail(request):
    to_list = []

    to_email = request.POST.get("to[]")
    to_list.append(to_email)
    from_email = settings.EMAIL_HOST_USER
    subject = request.POST.get("subject")
    message = request.POST.get("message")

    send_mail(subject, message, from_email, to_list)
    return render(request,"mail/success.html")
"""

def testmail(request):
    to_list = []
    to_email = request.POST.getlist('to')
    length = len(to_email)
    for i in range(length):
        to_list.append(to_email[i])

    subject = request.POST.get('subject')
    message = request.POST.get('message')
    from_email = settings.EMAIL_HOST_USER
    context = {
        "to_email": to_email,
        "from_email": from_email,
        "subject": subject,
        "message": message
    }

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, to_list)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')

    return render(request,"mail/success.html",context)
