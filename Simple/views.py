from django.shortcuts import render
import time


# Create your views here.
from Simple.tasks import *


def index(request):
    text = ""
    context={
        "text": text
    }
    return render(request, 'index.html')


def instant(request):
    text = "Main Thread Task Request"
    time.sleep(5)
    context = {"text": text}
    return render(request, 'index.html', context)


def seconds(request):
    text = "Background Task Request"
    debug_task.delay()
    work_for_5_seconds.delay()
    context = {"text": text}
    return render(request, 'index.html', context)
