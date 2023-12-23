# I have created this file - Rohit
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def navigator(request):
    return render(request, 'navigator.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')


    # Code for removing punctuations fron entered text
    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        #Logic for removing punctuations from entered text
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        # Creating dictonary key value pair for passing in analyze.html or any
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}

        # Analyze the text
        #return render(request, 'analyze.html', params)
        djtext = analyzed

        # Code for converting lowercase to upper case
    if(fullcaps == "on"):
        analyzed = ""

        # Logic for capitalize the lowercase letter in entered text
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

        # Code for to remove the new line in entered text
    if(newlineremover == "on"):
        analyzed = ""

        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed new lines', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

        # Code for to remove space in entered text
    if(spaceremover == "on"):
        analyzed = ""

        for char in djtext:
            if char != " ":
                analyzed = analyzed + char

        params = {'purpose': 'Removed spaces', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

        # Code for to remove extra space in entered text
    if(extraspaceremover == "on"):
        analyzed = ""

        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed

    # Code for Character Count
    if(charcount == "on"):
        #print(djtext)
        count1 = 0
        for char in djtext:
            count1 = count1 + 1

        params = {'purpose': 'Character Count', 'analyzed_text': analyzed, 'text_count': count1}
        #djtext = analyzed

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

