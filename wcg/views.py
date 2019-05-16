# from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import generic

# from wcg.forms import OrderForm
from wcg.models import Order


#
# def index(request):
#     return render(request, 'wcg/default.html', {})
#
#
# def new_wordcloud(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=True)
#             return redirect('wcg')
#         else:
#             return render(request, 'wcg/form.html', {'form': form})
#     else:
#         form = OrderForm()
#         return render(request, 'wcg/form.html', {'form': form})


class IndexView(generic.ListView):
    template_name = 'wcg/index.html'
    context_object_name = 'latest_order_list'

    def get_queryset(self):
        return Order.objects.order_by('ordered_at')[:5]


class DetailView(generic.DetailView):
    model = Order
    template_name = 'wcg/detail.html'


def get_orders(request):
    orders = Order.objects.all().values('client', 'title', 'font', 'mask_image')
    orders_list = list(orders)
    return JsonResponse(orders_list, safe=False)
