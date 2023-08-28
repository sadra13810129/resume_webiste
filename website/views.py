from django.shortcuts import render


def index_view(request):
    context = {"biography" : ["My name is Sadra Salehi Kordabadi",
                              "I started my coding journey with cpp but then i became interested in web development so i tried to learn things that i need to know about it.",
                              "Currenly i am trying to learn Django for Backend development."
                              ]}
    return render(request,'website/index.html',context=context)

def resume_view(request):
    context = {"skills" : ["Web Development","Automation Testing", "UI/UX Design"],
               "languages" : ["Persian","English","French"],
               "education" : "Bachelor of Computer Engineering"
               }
    return render(request,'website/resume.html',context=context)

def project_view(request):
    context = {"project_link" : "https://github.com/sadra13810129/resume_webiste"}
    return render(request,'website/projects.html',context=context)

def contact_view(request):
    context = {"Email" : "sadra13810129@gmail.com", "Telegram" : "@OriginalPlaymaker29", "Phone_Number" : "0910-124-5263"}
    return render(request,'website/contact.html',context=context)