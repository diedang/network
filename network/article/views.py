from django.shortcuts import render

# Create your views here.
from article.models import Article, Column


def index(request):
    columns = Column.objects.all()
    return render(request, 'news/index.html',{'columns': columns})

# def single_page(request, col, art):
#     if col not in ['Introduction']:
#         pass
#
#     the_art = None
#
#     if art is None:
#         the_col = Column.objects.filter(slug=col).first()
#         the_art = the_col.articlesets.first()
#     else:
#         the_art = Article.objects.filter(slug=art).first()
#
#     related_articles = the_col.articlesets.all()
#
#     return render(request, 'single-page.html', {'article': the_art})
#
#
#
#     pass

def list_column(request, col, page=1):
    column = Column.objects.get(slug=col)
    return render(request, 'news/column.html',{'column': column})

def show_article(request, col, art):
    article = Article.objects.filter(slug=art)
    return render(request, 'news/article.html',{'article': article})



