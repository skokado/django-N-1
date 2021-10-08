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
                category_id=random.choice(range(1, len(CATEGORY_CHOICES) + 1))
            )
            for _ in tqdm(range(n))
        ]
        models.Post.objects.bulk_create(posts)
        print(f'Generated {n} post records')
