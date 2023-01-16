from django.views.generic import DetailView
from django.shortcuts import render
import json
from client.models import Complex, Client, Site, SiteData
from django.http import JsonResponse, Http404, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
 
def index(request):
    complex  = Complex.objects.filter(
        site = Site.objects.get_current(),
        is_published = True,
        private = True
    ).first()
    if complex is not None:
        return render(
            request, 'base.html', {'object': complex}
        )
    else:
        return HttpResponseNotFound('Not Found')


class ComplexDetailView(DetailView):
    model = Complex
    template_name = 'base.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True, private=False)

@csrf_exempt
def contact(request):
    if request.POST:
        complex = Complex.objects.filter(pk=request.POST.get('complex_pk', 1)).first()
        Client.objects.create(
            name=request.POST.get('name', 'Запрос на рассылку'),
            email=request.POST.get('email', 'default@gmail.ru'),
            phone=request.POST.get('tel', '+00000000000'),
            complx=complex,
            site=Site.objects.get_current()
        ).save()
        message = f"\nНовый контакт {complex}\n\nИмя: {request.POST['name']}\nПочта: {request.POST['email']}\nТелефон: {request.POST['tel']}\nЖК: {complex}"
        send_mail(
            subject=f'Новый контакт {str(complex).upper()}', 
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=settings.RECIPIENT_ADDRESS,
        )
            
        return JsonResponse({'status': 'data recived'})
    else:
        return JsonResponse({'status': 'data did not saved'})