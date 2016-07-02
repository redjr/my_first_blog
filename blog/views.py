from django.shortcuts import render
from django.utils import timezone
from . models import Post
# Create your views here.
# uma completa aqui: http://stackoverflow.com/questions/35377179/django-noreversematch-error-on-production
# outra completa aqui: http://stackoverflow.com/questions/31228794/noreversematch-error-finding-it-hard
# criando o método def chamado post_list,
# que aceita o pedido(request) e retorna um
# método render que será processado (para montar)
# nosso modelo blog/post_list.html
def post_list(request):
    #exibindo posts no blog, por ordem de publicação por date
    # published_date_lte fica dando erro: Cannot resolve keyword 'published_date' into field
    # porém, publish_date__lte tudo funciona corretamente
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request, 'blog/post_list.html', { 'posts' : posts })