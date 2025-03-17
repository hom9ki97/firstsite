from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Topic, Lessons, CodeExample, HomeWork, Language
from .forms import CodeExampleForm, LessonsForm, HomeWorkForm, TopicForm


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


def topic_page(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    topics = Topic.objects.filter(language=language).prefetch_related('lessons')
    context = {'topics': topics,
               'language': language,
               'language_id': language_id}
    print(language)
    return render(request, 'main/topic.html', context)


def lesson_page(request, lesson_id):
    lesson = get_object_or_404(Lessons, id=lesson_id)
    homeworks = lesson.homeworks.all()
    code_examples = lesson.code_examples.all()
    for example in code_examples:
        try:
            with example.code_file.open('r') as f:
                example.code_content = f.read()
        except Exception as e:
            example.code_content = f"Ошибка при чтении файла: {str(e)}"
    context = {
        'lesson': lesson,
        'homeworks': homeworks,
        'code_examples': code_examples,
        'add_hw': add_hw
    }
    return render(request, 'main/lesson.html', context)


def home_work_page(request, home_work_id):
    hw = get_object_or_404(HomeWork, id=home_work_id)
    lesson = hw.lesson
    code_examples = hw.code_examples.all()
    for example in code_examples:
        try:
            with example.code_file.open('r') as f:
                example.code_content = f.read()
        except Exception as e:
            example.code_content = f"Ошибка при чтении файла: {str(e)}"
    context = {
        'homework': hw,
        'lesson': lesson,
        'code_examples': code_examples,
    }
    return render(request, 'main/homework.html', context)


def upload_code(request):
    if request.method == 'POST':
        form = CodeExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main:lesson', lesson_id=form.cleaned_data['lesson'].id)
    else:
        form = CodeExampleForm()
    return render(request, 'main/upload_code.html', {'form': form})


def upload_code_hw(request):
    if request.method == 'POST':
        form = CodeExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('main:home_work_page', home_work_id=form.cleaned_data['homework'].id)
    else:
        form = CodeExampleForm()
        return render(request, 'main/upload_code.html', {'form': form})


def add_topic(request, language_id):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save()
            language_id = topic.language.id
            return redirect('main:topic', language_id)
    else:
        form = TopicForm()
    return render(request, 'main/add_topic.html', {'form': form})


def lesson_add(request):
    if request.method == 'POST':
        form = LessonsForm(request.POST)
        if form.is_valid():
            lesson = form.save()
            topic = lesson.topic
            print(request.POST.get('topic'))
            language_id = topic.language.id
            return redirect('main:topic', language_id)
    else:
        form = LessonsForm()
    return render(request, 'main/add_lesson.html', {'form': form})


def add_hw(request, lesson_id):
    if request.method == 'POST':
        form = HomeWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:lesson', lesson_id=lesson_id)
    else:
        form = HomeWorkForm()
    return render(request, 'main/add_hw.html', {'form': form})


def del_exemple_code(request, code_example_id):
    code_example = get_object_or_404(CodeExample, id=code_example_id)
    if code_example.lesson:
        print(code_example.lesson, code_example_id)
        code_example.delete()

        return redirect('main:lesson', code_example.lesson.id)
    elif code_example.homework:
        print(code_example.homework, code_example_id)
        code_example.delete()

        return redirect('main:lesson', code_example.homework.id)


def del_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    topic.delete()
    return redirect('main:topic', topic.language.id)


def del_lesson(request, lesson_id):
    lesson = get_object_or_404(Lessons, id=lesson_id)
    lesson.delete()
    return redirect('main:topic', lesson.topic.language.id)
