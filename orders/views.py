from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
	DetailView, 
	CreateView, 
	UpdateView,
	DeleteView)
from .models import Order


def home(request):
	context = {
	'orders': Order.objects.all()
	}
	return render(request, 'orders/home.html', context)


def search_orders(request):
	if 'q' in request.GET:
		query = request.GET['q']
		results= Order.objects.filter(priority__icontains=query)
	else:
		results = []

	return render(request, 'orders/search_results.html', {'results': results})


class OrderListView(ListView):
	model = Order
	template_name = 'orders/home.html'
	context_object_name= 'orders'
	ordering = ['priority']

class OrderDetailView(DetailView):
	model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
	model = Order
	fields= ['product_name', 'priority']

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Order
	fields= ['product_name', 'priority']

	def form_valid(self, form):
		form.instance.creator = self.request.user
		return super().form_valid(form)


	def test_func(self):
		order = self.get_object()
		if self.request.user == order.creator:
			return True
		return False

class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Order
	success_url = '/'

	def test_func(self):
		order = self.get_object()
		if self.request.user == order.creator:
			return True
		return False


	
