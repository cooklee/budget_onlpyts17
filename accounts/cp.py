from datetime import datetime


def data(request):
    return {
        'data': datetime.now().time()
    }
