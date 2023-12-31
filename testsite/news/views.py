from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView



class HomeNews(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    # extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

# переопределяем get_queryset мы получаем только нужный набор объектов
    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    # pk_url_kwarg = 'news_id'
    # template_name = 'news/news_detail.html'       #используется по умолчанию этот шаблон, но можно выбрать и другой

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    success_url = reverse_lazy('home')



# def index(request):
#     news = News.objects.all()
#     categories = Category.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {"news_item": news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)       # форма связана с данными
#         if form.is_valid():                # проверяет прошла ли форма валидацию, на основе валидаторов, связанных с классом
#             # print(form.cleaned_data)        # если форма прошла валидацию, то данные попадают в словарь cleaned_data
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect('home')
#     else:
#         form = NewsForm()                   # форма не связана с данными
#     return render(request, 'news/add_news.html', {'form': form})