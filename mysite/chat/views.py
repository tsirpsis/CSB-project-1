from django.shortcuts import get_object_or_404, render
from .models import Thread, Message

def index(request):
    all_threads = Thread.objects.all()
    return render(request, "chat/index.html", {"threads": all_threads})

def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'chat/thread.html', {'thread': thread})
