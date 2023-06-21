from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком записей
def my_notes_list(request):
    return HttpResponse('Список записей')


def group_notes(request, pk):
    return HttpResponse('Группы записей')

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def my_notes_detail(request, pk):
    return HttpResponse(f'Запись номер {pk}')
