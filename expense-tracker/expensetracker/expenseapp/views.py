import calendar
from datetime import timezone

from django.db.models import Sum
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Category, Expense, Income
from .serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer, CustomUserCreateSerializer
from djoser.views import UserViewSet as DjoserUserViewSet
from django.template.loader import render_to_string
from django.core.mail import send_mail


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all Category views


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


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
    # permission_classes = [IsAuthenticated]


class CustomUserViewSet(DjoserUserViewSet):
    serializer_class = CustomUserCreateSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_summary(request):
    user = request.user

    total_expenses = Expense.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0
    total_incomes = Income.objects.filter(user=user).aggregate(Sum('amount'))['amount__sum'] or 0

    available_balance = total_incomes - total_expenses

    data = {
        'total_expenses': total_expenses,
        'total_incomes': total_incomes,
        'available_balance': available_balance,
    }

    return Response(data)

    # Calculate monthly summaries for a user


def calculate_monthly_summary(user, year, month):
    expenses = Expense.objects.filter(user=user, date__year=year, date__month=month)
    incomes = Income.objects.filter(user=user, date__year=year, date__month=month)

    total_expenses = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_incomes = incomes.aggregate(Sum('amount'))['amount__sum'] or 0
    available_balance = total_incomes - total_expenses

    return {
        'user': user,
        'year': year,
        'month': month,
        'total_expenses': total_expenses,
        'total_incomes': total_incomes,
        'available_balance': available_balance,
    }


def generate_email_content(summary):
    context = {
        'summary': summary,
    }
    return render_to_string('account_summary_email_template.html', context)


def send_account_summary_email(user, year, month):
    subject = f"Monthly Account Summary - {year}/{month}"
    summary = calculate_monthly_summary(user, year, month)
    email_content = generate_email_content(summary)

    send_mail(
        subject,
        '',
        'salmanshaheelas@gmail.com',
        [user.email],
        html_message=email_content,
    )

