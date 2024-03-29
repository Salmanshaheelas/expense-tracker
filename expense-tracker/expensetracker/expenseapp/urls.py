from django.urls import path, include
from djoser.urls import authtoken
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from .views import CategoryViewSet, ExpenseViewSet, IncomeViewSet, CustomUserViewSet, ExpenseListCreateView, \
    ExpenseRetrieveUpdateDestroyView, CategoryListCreateView, CategoryRetrieveUpdateDestroyView, user_summary

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'incomes', IncomeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('',TemplateView.as_view(template_name='index.html')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/', CustomUserViewSet.as_view({'post': 'create'}), name='user-register'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseRetrieveUpdateDestroyView.as_view(), name='expense-retrieve-update-destroy'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='category-retrieve-update-destroy'),
    path('user-summary/', user_summary, name='user-summary'),
]
