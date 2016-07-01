from django.shortcuts import render

# Create your views here.
# criando o método def chamado post_list,
# que aceita o pedido(request) e retorna um
# método render que será processado (para montar)
# nosso modelo blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})