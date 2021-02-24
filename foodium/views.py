from django.shortcuts import render


def handler404(request, exception):
    '''
    404 Error Handler
    '''
    return render(request, 'errors/error_404.html')

# def handler404(request, exception):
#     context = {}
#     response = render(request, "errors/404.html", context=context)
#     response.status_code = 404
#     return response
