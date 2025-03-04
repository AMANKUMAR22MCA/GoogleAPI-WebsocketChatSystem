from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Message


def user_selection(request):
    if request.method == "POST":
        username = request.POST.get("username")
        # Use a fixed password or pre-set users
        user = authenticate(username=username, password="password123")
        if user:
            login(request, user)
            return redirect('chat_room')
    return render(request, 'user_selection.html')


@login_required
def chat_room(request):
    messages = Message.objects.filter(
        room_name="chat_room").order_by("timestamp")
    return render(request, 'chat.html', {'messages': messages})
