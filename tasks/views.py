import ast

from django.shortcuts import render

from tasks.models import Type, Tasks


def main_page(request):
    return render(request, template_name='main_page.html', context={
        'title': 'Главная страница',
        'types': Type.objects.all()
    })


def tasks_view(request, type_id):
    tasks = Tasks.objects.filter(type_id=type_id)
    context = {
        'title': 'Задачи',
        'tasks': tasks,
        'current_type': type_id,
        'types': Type.objects.all(),
    }
    if request.POST:
        print(request.POST.get('answers', '{}'))
        answers = ast.literal_eval(request.POST.get('answers', '{"test": "test"}'))
        for task_id, task_answer_user in request.POST.items():
            if task_id != 'csrfmiddlewaretoken' and task_id != 'answers' and task_answer_user:
                task = Tasks.objects.get(pk=task_id)
                if task.answer == int(task_answer_user):
                    answers[int(task_id)] = True
                else:
                    answers[int(task_id)] = False
        if answers:
            context['answers'] = answers
        print(answers)
    return render(request, 'tasks.html', context)
