from django.contrib import admin
from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
	path('add/', views.ExpenseCreateView.as_view(), name = "add_expense"),
	path('details/<int:pk>', views.ExpenseDetailView.as_view(), name = "expense_detail"),
	path('list/', views.ExpenseListView.as_view(), name = "expense_list"),
	path('delete/<int:pk>', views.ExpenseDeleteView.as_view(), name = "expense_delete"),
	path('special/', views.filter_by_date, name= "filter_by_date"),
]