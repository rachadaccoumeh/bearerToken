from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app.models import Location, Hospital
from app.serializers import LocationSerializer, HospitalSerializer


# Create your views here.
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAuthenticated]


class HospitalViewSet(viewsets.ModelViewSet):
    # user = User.objects.create_user(username="test", password="test")
    # token = Token.objects.create(user=user)
    # print(token.key)
    # pdb.set_trace()
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def location_add(request):
    try:
        if request.method == 'POST':
            loc = None
            try:
                loc = Location.objects.get(city=request.data['city'])
            except:
                loc = Location.objects.create(city=request.data['city'],
                                              zip='nader'
                                              )

        return JsonResponse({'message': 'location is created successfully!'}, status=status.HTTP_201_CREATED)
    except:
        return JsonResponse({'message': 'Error!'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def hospital_add(request):
    try:
        if request.method == 'POST':
            try:
                loc = Location.objects.get(city=request.data['city'])
            except:
                loc = Location.objects.create(city=request.data['city'], zip='test')
            hospital = Hospital.objects.create(name=request.data['name'], phone=request.data['phone'], location=loc)

        return JsonResponse({'message': 'hospital is created successfully!'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return JsonResponse({'message': 'Error! ' + str(e)}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([permissions.IsAuthenticated])
def location_delete(request, pk):
    try:
        location = Location.objects.get(pk=pk)
        location.delete()
        return JsonResponse({'message': 'The location was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)
    except Location.DoesNotExist:
        return JsonResponse({'message': 'The location does not exist'}, status=status.HTTP_404_NOT_FOUND)
