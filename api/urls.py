from django.urls import path
from .views import NoteLIstCreateAPIView, NoteDetailAPIView 

app_name = 'api'


urlpatterns = [
    path('notes/',NoteLIstCreateAPIView.as_view(), name='home'),
    path('notes/<uuid:product_id>/',NoteDetailAPIView.as_view(), name='note_detail'),

    
]
