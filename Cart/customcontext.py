from .models import Order,OrderDetail


def ChackUser(request):
    if not request.user:
        if not request.COOKIES['Order']:
            pass