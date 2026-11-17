from django.shortcuts import get_object_or_404, render, redirect
from .models import Thread, Message
from django.utils import timezone

def index(request):
    if request.method == "POST":
        header = request.POST["header"]
        content = request.POST["content"]

        Thread.objects.create(header=header, content=content, pub_date=timezone.now())
        return redirect("/chat/")

    all_threads = Thread.objects.all()
    return render(request, "chat/index.html", {"threads": all_threads})

def thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == "POST":
        content = request.POST["content"]

        Message.objects.create(thread=thread, message=content)
        return redirect(f"/chat/{thread_id}/")

    return render(request, "chat/thread.html", {"thread": thread})
