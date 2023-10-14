from django.shortcuts import render

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Классический пломбир',
        'description': 'Настоящее мороженое, для истинных ценителей вкуса. '
                       'Если на столе появляется пломбир — это не надолго.',
    },
    {
        'id': 1,
        'title': 'Мороженое с кузнечиками',
        'description': 'В колумбийском стиле: мороженое '
                       'с добавлением настоящих карамелизованных кузнечиков.',
    },
    {
        'id': 2,
        'title': 'Мороженое со вкусом сыра чеддер',
        'description': 'Вкус настоящего сыра в вафельном стаканчике.',
    },
    {
        'id': 3,
        'title': 'Мороженое с варёной сгущёнкой',
        'description': 'Безумно сладкое и такое родное, прямо из детства.',
    }
]

ice_cream_id_dict = {ice_cream['id']: ice_cream
                     for ice_cream in ice_cream_catalog}


def ice_cream_list(request):
    context = {'ice_cream_list': ice_cream_catalog}
    return render(request, 'ice_cream/list.html', context)


def ice_cream_detail(request, pk):
    context = {'ice_cream': ice_cream_id_dict[pk]}
    return render(request, 'ice_cream/detail.html', context)
