from django.shortcuts import render

# Create your views here.
# def error(request, exception):
#     # context = {}
#     return render(request,'error/notpage.html', status=404)
def error_handler_404(request, exception):
   context = {}
   return render(request,'error/notpage.html', context, status=404)

def error_500(request):
   context = {}
   return render(request,'error/notpage_505.html', context, status=505)