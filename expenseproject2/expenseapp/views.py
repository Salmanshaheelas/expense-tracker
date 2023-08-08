from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics
from .models import Category, Expense, Income
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer, CustomUserCreateSerializer
from djoser.views import UserViewSet as DjoserUserViewSet


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]  # Require authentication for all Category views


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CustomUserViewSet(DjoserUserViewSet):
    serializer_class = CustomUserCreateSerializer
