from django.views.generic import DetailView
from django.shortcuts import render
from client import serializers
from rest_framework import generics
from client.models import Complex, Client, Site, SiteData
from django.http import HttpResponseNotFound
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
 
def index(request):
    st = SiteData.objects.filter(site=Site.objects.get_current()).first()
    if st is not None:
        complex  = Complex.objects.filter(
            site = st,
            is_published = True,
            private = True
        ).first()
        if complex is not None:
            return render(
                request, 'base.html', {'object': complex}
        )

    return HttpResponseNotFound('Not Found')


class ComplexDetailView(DetailView):
    model = Complex
    template_name = 'base.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True, private=False)


class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.ClientSerializer
    queryset = Client.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
       
        try:
            serializer.is_valid(raise_exception=True)
            contact = serializer.save()
            message = f"\nНовый контакт {contact.complex}\n\nИмя: {contact.name}\nПочта: {contact.email}\nТелефон: {contact.phone}\nЖК: {contact.complex}"
            send_mail(
                subject=f'Новый контакт {str(complex).upper()}', 
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=settings.RECIPIENT_ADDRESS,
            )
        except Exception as e:
            print(e)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)