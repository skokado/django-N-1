import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from tqdm import tqdm

from app import models

faker = Faker()
DEFAULT_POSTS_RECORDS = 1000

CATEGORY_CHOICES = (
    'プログラミング',
    'デザイン',
    'マネジメント',
    'ビジネス',
    'その他',
)


TAGS = (
    models.Tag.objects.create(name='Python'),
    models.Tag.objects.create(name='Ruby'),
    models.Tag.objects.create(name='Go'),
    models.Tag.objects.create(name='Kotlin'),
)

# TAGS = (
#     'Python',
#     'Ruby',
#     'Go',
#     'Kotlin',
# )


class Command(BaseCommand):
    help = 'Generate random datas using faker'

    def add_arguments(self, parser):
        parser.add_argument('--n', nargs='+', type=int, default=DEFAULT_POSTS_RECORDS)

    def handle(self, *args, **options):
        n: int = options['n']

        # カテゴリ登録
        categories = []
        for category in CATEGORY_CHOICES:
            categories.append(models.Category(
                name=category
            ))
        models.Category.objects.bulk_create(categories, ignore_conflicts=True)

        posts = [
            models.Post(
                title=faker.text(),
                content=' '.join(faker.texts()),
                category_id=random.choice(range(1, len(CATEGORY_CHOICES) + 1)),
            )
            for _ in tqdm(range(n))
        ]
        models.Post.objects.bulk_create(posts)
        posts = models.Post.objects.all()
        # 3個のタグを登録する
        for post in posts:
            tags = random.sample(TAGS, 3)
            post.tags.add(*tags)
            
        print(f'Generated {n} post records')
