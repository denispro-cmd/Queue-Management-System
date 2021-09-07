from django.shortcuts import render, redirect
from django.db import models
from .forms import TokenForm
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Token
from django.http import HttpResponse
from django.urls import reverse



class TokenListView(ListView):
		model = Token
		template_name = 'token/token.html'
		context_object_name = 'orders'
		

class TokenDetailView(DetailView):
		model = Token
		template_name = 'token/token-detail.html'



class TokenCreateView(CreateView):
	template_name = 'token/token-create.html'
	form_class = TokenForm
	queryset = Token.objects.all()



	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('tokens')


class TokenUpdateView(UserPassesTestMixin,UpdateView):
	template_name = 'token/token-update.html'
	form_class = TokenForm
	queryset = Token.objects.all()

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('tokens' )

	def test_func(self):
		order = self.get_object()
		if self.request.user == order.author:
			return True
		return False


class TokenDeleteView(UserPassesTestMixin,DeleteView):
	model = Token
	success_url = 'tokens'
	template_name = 'token/token-delete.html'


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		

	def test_func(self):
		order = self.get_object()
		if self.request.user == order.author:
			return True
		return False



