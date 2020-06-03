from django.contrib import admin
from .models import Article ##models에 작성한 model 등록

# Register your models here.

admin.site.register(Article) ## admin==관리자페이지

# --> models.py에서 작성한 'Article'이라는 class를 admin site에 등록
