from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increment
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    #using List comprehension
    sortedDict = [(k,v) for k, v in sorted(worddictionary.items(), key=operator.itemgetter(1), reverse = True)]

    print(fulltext)
    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedDict':sortedDict})