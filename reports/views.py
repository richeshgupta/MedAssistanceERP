from django.shortcuts import render

def report(request):
    if request.method == 'POST':
        duration = request.POST.get('time')
        print(duration)
    return render(request,'reports/report.html',{})

