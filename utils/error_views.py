from django.http import JsonResponse

def handler404(request, exception):
    message = ('Route not found')
    response = JsonResponse(data={ 'error': message })
    response.status_code = 404
    return response
                                    
def handler500(request):
    message = ('Internal Server Error')
    response = JsonResponse(data={ 'error': message })
    response.status_code = 500
    return response
                                        
def handler403(request, exception=None):
    """ Handler to limit api callls by specific IP and avoid DDOS attacks"""
    message = ('sorry you are blocked')
    response = JsonResponse(data={ 'error': message })
    response.status_code = 429
    return response
