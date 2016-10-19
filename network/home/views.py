# !coding=utf-8
from django.shortcuts import render, render_to_response
from django.http import Http404

def index(request):

    from article.models import Column, Article

    about_column = Column.objects.filter(slug='about').first()
    column_text = ''
    if about_column is not None:
        column_text = about_column.intro

    top_six_news = Article.objects.filter(column__slug='news', published=True).order_by('pub_date')[0:6]
    return render(request, 'index.html', {'courseintro': column_text, 'news': top_six_news})


def static_page(request, col, art=None):
    from article.models import Column

    column = Column.objects.filter(slug=col).first()
    if column is None: raise Http404()
    article = column.article_set.filter(slug=art).first() if art is not None else column.article_set.first()
    if article is None: raise Http404()
    articles = column.article_set.all()

    return render(request, 'static-page.html', {
        'column': column,
        'article': article,
        'articles': articles
    })

