from rest_framework.response import Response
from rest_framework.decorators import api_view
from oauth2_provider.models import AccessToken, RefreshToken

from doctors.serializers import UserSerializer
from .models import PatientProfile


@api_view(['POST'])
def user_register_view(request):
    serializer = UserSerializer(data=request.data)

    data = {}

    if serializer.is_valid():
        user = serializer.save()
        PatientProfile.objects.create(user=user)

        data['response'] = 'Account for Patient has been created'
        data['username'] = user.username
        data['email'] = user.email

        token = AccessToken.objects.get(user=user)
        refresh_token = RefreshToken.objects.get(user=user)
        data['token'] = token.token
        data['refresh_token'] = refresh_token.token
        data['expires'] = token.expires
    
    else:
        data = serializer.errors
    
    return Response(data)


