from django.urls import path
from .views import TokenListView,TokenDetailView,TokenCreateView,TokenUpdateView,TokenDeleteView
from .import  views
from .models import Token

urlpatterns = [
	path('token_all/',TokenListView.as_view(), name='tokens'),
	path('form/create/',TokenCreateView.as_view(model=Token, success_url="/success/"), name='token-create'),
	path('order/<int:pk>/',TokenDetailView.as_view(), name='token-detail'),
    path('order/<int:pk>/update/',TokenUpdateView.as_view(), name='token-update'),
    path('order/<int:pk>/delete/',TokenDeleteView.as_view(), name='token-delete'),

]