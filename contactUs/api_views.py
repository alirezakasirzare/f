from rest_framework.permissions import IsAdminUser
from .serializers import ContactUsSerizalizers
from rest_framework.response import Response
from rest_framework import generics
from .models import ContactUs






class contactus_list(generics.ListAPIView):
    serializer_class = ContactUsSerizalizers
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return ContactUs.objects.all()


class add_contact(generics.CreateAPIView):
    serializer_class = ContactUsSerizalizers

    def post(self, request):
        data = ContactUsSerizalizers(data=request.data)
        if data.is_valid():
            vl = data.validated_data
            ContactUs.objects.create(firstName=vl['firstName'],lastName=vl['lastName'],email=vl['email'],contact_number=vl['contact_number'],company_name=vl['company_name'],subject=vl['subject'],message=vl['message'],status=False)
            return Response({'message': 'درخواست ثبت شد'})
        else:
            return Response(data.errors)