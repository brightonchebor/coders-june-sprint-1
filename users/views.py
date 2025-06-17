from django.shortcuts import render

# Create your views from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import CheckInOut

@login_required
def check_in(request):
    today = timezone.now().date()
    user = request.user

    # Check if already checked in
    entry, created = CheckInOut.objects.get_or_create(user=user, date=today)

    if entry.check_in_time:
        message = "Already checked in!"
    else:
        entry.check_in_time = timezone.now()
        entry.save()
        message = "Checked in successfully."

    return render(request, 'checkin_status.html', {'message': message})

@login_required
def check_out(request):
    today = timezone.now().date()
    user = request.user

    try:
        entry = CheckInOut.objects.get(user=user, date=today)
        if entry.check_out_time:
            message = "Already checked out!"
        else:
            entry.check_out_time = timezone.now()
            entry.save()
            message = "Checked out successfully."
    except CheckInOut.DoesNotExist:
        message = "You must check in before checking out."

    return render(request, 'checkin_status.html', {'message': message})
here.
