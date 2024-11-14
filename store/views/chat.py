# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Chat, ChatMessage

@login_required
def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.method == 'POST':
        message_content = request.POST.get('message')
        if message_content:
            ChatMessage.objects.create(
                chat=chat,
                user=request.user,
                message=message_content
            )
            return redirect('chat_view', chat_id=chat.id)

    messages = chat.messages.order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages, 'chat': chat})