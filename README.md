参考 https://selfs-ryo.com/detail/django_nplusone

Python: 3.9
Django: 3.2.8

```shell
$ git clone https://github.com/skokado/django-Nplus1.git
$ cd django-N-1.git
$ pipenv install
$ pipevn shell
$ python3 manage.py migrate
$ # ランダムデータを登録
$ python3 manage.py gendata

$ # アプリケーション起動
$ python3 manage.py runserver
# => http://localhost:8000/
```
