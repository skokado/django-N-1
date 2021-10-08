import time
from typing import Dict, Any

from django.views.generic import TemplateView

from app.models import Post


class Home(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['records'] = Post.objects.count()
        return ctx


class BadView(TemplateView):
    template_name = 'show-posts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['view_name'] = 'Bad'
        start = time.time()
        posts = []
        for post in Post.objects.all():
            posts.append({
                'id': post.id,
                'title': post.title,
                # 全ての post レコードに対し、外部参照する category に対するクエリが発行される
                'category': {
                    'name': post.category.name
                }
            })
        ctx['posts'] = posts

        ctx['process_time'] = round((time.time() - start), 2)
        return ctx


class GoodView(TemplateView):
    template_name = 'show-posts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['view_name'] = 'Good'
        start = time.time()
        posts = []
        # 
        # 違いはここ(あらかじめ category テーブルをJOINしてデータを取得しておく)
        for post in Post.objects.all().select_related('category'):
            posts.append({
                'id': post.id,
                'title': post.title,
                'category': {
                    # 実行されるクエリは1回のみとなる
                    'name': post.category.name
                }
            })
        ctx['posts'] = posts

        ctx['process_time'] = round((time.time() - start), 2)
        return ctx
