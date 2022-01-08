from django.http import HttpResponse
from django.shortcuts import render
def hey(request):
    return render(request,'analyze2.html')
#def hii(request):
   # return HttpResponse(''' <h1>Hii...!!!!</h1> <a href='/'> <h2> Get Back Pragya </h2></a>''')
def index(request):

    return render(request,'index.html')
def analyze(request):
    djtext=(request.POST.get('text','default'))

    removepunc=(request.POST.get('removepunc','off'))
    fullcaps=(request.POST.get('fullcaps','off'))
    NewLine=(request.POST.get("NewLine","off"))
    print(removepunc)
    if removepunc=="on":

        punctuations='''!()-[]{};:'"\,<>./?@#$&*^%_'''
        analyzed=" "
        for char in djtext:
            if char not in punctuations:
               analyzed=analyzed+char
        params={'purpose':'Removed Punctuation','analyzed_text': analyzed }
        djtext=analyzed

       # return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=" "
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed

        #return render(request, 'analyze.html', params)
    if NewLine=="on":
        analyzed=" "
        for char in djtext:
            if char != '\n' and char !="\r":
                analyzed=analyzed+char
            else:
                print("No")
        print("pre",analyzed)
        params={'purpose':"NewLine Remover",'analyzed_text':analyzed}

        #return render(request, 'analyze.html', params)
    if(fullcaps!="on" and NewLine!="on" and removepunc!="on"):
               return render(request,"Error.html")





    return render(request,'analyze.html',params)







