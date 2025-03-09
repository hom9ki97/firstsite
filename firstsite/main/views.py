from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

from .models import Topic, Lessons


@login_required
def profile(request):
    return render(request, 'main/profile.html')


class FSLogout(LogoutView):
    pass


class FSLoginView(LoginView):
    template_name = 'main/login.html'


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


def index(request):
    return render(request, 'main/index.html')


def topic_page(request, page):
    topics = Topic.objects.prefetch_related('lessons').all()
    context = {'topics': topics}
    return render(request, 'main/topic.html', context)


def lesson_page(request, lesson_id):
    lesson = get_object_or_404(Lessons, id=lesson_id)
    homeworks = lesson.homeworks.all()
    context = {
        'lesson': lesson,
        'homeworks': homeworks,
    }
    return render(request, 'main/lesson.html', context)
