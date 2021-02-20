from django.shortcuts import render


def handler404(request, exception):
    '''
    404 Error Handler
    '''
    return render(request, 'errors/error_404.html')
