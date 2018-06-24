from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .MachineLearning import logistic_regression


# Create your views here.
class AppView(LoginRequiredMixin, View):

	def get(self, request):
		return render(request, "apps.html", {})

class PredictionView(LoginRequiredMixin, View):

	def get(self, request):
		return render(request, "prediction.html", {})


class TrainingView(LoginRequiredMixin, View):

	def get(self, request):
		return render(request, "training.html", {})

@login_required
def predict(request):
	if request.method == 'POST':

		loan_amount = request.POST['loan']
		interest_rate = request.POST['irate']
		emp_length = request.POST['emp_length']
		annual_inc = request.POST['annual_income'] 
		dti = request.POST['dti'] 
		delinq_2yrs = request.POST['del_2yrs'] 
		revol_util = request.POST['revol_util']
		total_acc = request.POST['total_acc'] 
		longest_credit_length = request.POST['longest_cr_length']

		prediction = logistic_regression(loan_amount, interest_rate, emp_length, annual_inc, dti, delinq_2yrs, revol_util, total_acc, longest_credit_length)

		return HttpResponse(prediction)

@login_required
def train(request):
	pass
		