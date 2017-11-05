from django.shortcuts import render


def evaluation_list(request):
    return render(request, 'web/evaluationslist.html', {})
