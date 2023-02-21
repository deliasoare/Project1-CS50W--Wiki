from django.shortcuts import render,redirect
from django import forms
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import default_storage
from . import util
from markdown2 import Markdown
from django import forms
from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def entry(request, title):
    if util.get_entry(title):
        EntryPage=util.get_entry(title)
        markdowner = Markdown()
        return render(request, "encyclopedia/entry.html", {
            "entry" : markdowner.convert(EntryPage),
            "entryTitle":title
        })
    else:
        return render(request, "encyclopedia/error.html")

def search(request):
    if request.method == "POST":
        title = request.POST["q"]
        for entry in util.list_entries():
            if entry.upper() == title.upper():
                EntryPage=util.get_entry(entry)
                markdowner = Markdown()
                return render(request, "encyclopedia/entry.html", {
                    "entry" : markdowner.convert(EntryPage),
                    "entryTitle":title
                })
            else:
                SubstringEntries = []
                for entry in util.list_entries():
                    if title.upper() in entry.upper():
                        SubstringEntries.append(entry)
        return render(request, "encyclopedia/search.html", {
            "entries" : SubstringEntries,
            "title" : title
        })

def newpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newpage.html")
    else:
        title= request.POST["title"]
        content=request.POST["content"]
        if util.get_entry(title) == None:
            util.save_entry(title,content)
            EntryPage=util.get_entry(title)
            markdowner = Markdown()
            return render(request, "encyclopedia/entry.html", {
                "entry" : markdowner.convert(EntryPage),
                "entryTitle":title
            })
        else:
            return render(request, "encyclopedia/newpage.html", {
                "title":title,
                "exists" : True
            })

def editpage(request, entryTitle):
    if request.method == "GET":
        entryPage = util.get_entry(entryTitle)
        return render(request, "encyclopedia/editEntry.html", {
            "entryTitle" : entryTitle,
            "entry" : entryPage
        })
    else:
        entry = request.POST["content"]
        util.save_entry(entryTitle, entry)
        return render(request, "encyclopedia/entry.html", {
            "entryTitle" : entryTitle,
            "entry": entry
        })

def random(request):
    entries = util.list_entries()
    page = choice(entries)
    entry = util.get_entry(page)
    return render(request, "encyclopedia/entry.html", {
        "entryTitle" : page,
        "entry" : entry
    })

















