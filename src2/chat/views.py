from django.shortcuts import render, redirect


def index(request):
    return render(request, "chat1/chat-home.html")

def chathome(request):
    # return redirect("/chat-app/index/")
    return render(request, "chat1/chat-index.html")

def room(request, room_name):
    return render(request, "chat1/chat-room.html", {"room_name": room_name})