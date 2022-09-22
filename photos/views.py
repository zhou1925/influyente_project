from .models import Photo
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .validators import isValidExtension, isValidSize

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def uploadPhoto(request):
    """
    An user has limit of 10 photos if try to request with more
    photos and exceeds the limit just we accept the diference
    """
                                    
    user = request.user                                  
    photos = request.FILES.getlist('photos')

    user_photos = user.photos.count()
    limit_photos = 10
    print(user_photos)

    if user_photos >= limit_photos:                                   
        return Response({ 'message': 'You cant upload more {limit_photos} photos' }, status=status.HTTP_403_FORBIDDEN)
                                    
    total_photos = user_photos + len(photos)
                                    
    if total_photos <= limit_photos:
        for photo in photos:
            if isValidExtension(str(photo)) and isValidSize(photo.size):
                Photo.objects.create(user=user, photo=photo)
            else:
                return Response({ 'error': 'Please make sure images are .jpg or .png with less than 1mb' }, status=status.HTTP_400_BAD_REQUEST)
    elif total_photos > limit_photos and user_photos < limit_photos:
        for i in range(total_photos - limit_photos):
            if isValidExtension(str(photos[i])):
                Photo.objects.create(user=user, photo=photos[i])
            else:
                return Response({ 'error': 'Please upload only images files.' }, status=status.HTTP_400_BAD_REQUEST)
           # 8 - 4 = 2 -> 8+4=12 - 10 = 2
    return Response({})
