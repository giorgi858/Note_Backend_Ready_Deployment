from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer, UserSerializer
from .models import Note
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

class NoteLIstCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    
class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all().order_by('-id')
    serializer_class = NoteSerializer
    lookup_url_kwarg = 'product_id'
  


class CreateUserView(generics.CreateAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [AllowAny]