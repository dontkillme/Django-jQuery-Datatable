from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator

DATA = [ [str(x)] for x in range(1, 100) ]

def main_view(request):
  return render(request, "index.html")


def get_part_data(request):
  page = int(request.POST.get('start'))/int(request.POST.get('length'))
  pagination = Paginator(DATA, int(request.POST.get('length')))
  out = {"data": list(pagination.page(int(page)+1)),
         "draw": request.POST.get('draw'),
         "recordsTotal": len(DATA),
         "recordsFiltered": len(DATA),}
  return JsonResponse(out)
