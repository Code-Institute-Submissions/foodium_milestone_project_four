from django.shortcuts import render


def handler404(request, exception, template_name="errors/error_404.html"):
    '''
    404 Error Handler
    '''
    response = render, (template_name)
    response.status_code = 404
    return response
