from rest_framework.response import Response
from rest_framework.decorators import api_view
from oauth2_provider.models import AccessToken, RefreshToken
from rest_framework import status


from .serializers import UserSerializer
from .models import DoctorProfile


@api_view(['POST'])
def user_register_view(request):
    serializer = UserSerializer(data=request.data)

    data = {}

    if serializer.is_valid():
        user = serializer.save()
        DoctorProfile.objects.create(user=user)

        data['response'] = 'Account for Doctor has been created'
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



@api_view(['POST'])
def logout_user(request):
    try:
        token = request.headers.get('Authorization', '')[7:]
        access_token = AccessToken.objects.get(token=token)
        user = access_token.user
        access_token.delete()
        refresh_token = RefreshToken.objects.get(user=user)
        refresh_token.delete()
        
        return Response({'Message': 'You are successfully logged out'}, status=status.HTTP_200_OK)
    except AccessToken.DoesNotExist:
        return Response({'Message': 'Failed'}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'Message': e})
    

