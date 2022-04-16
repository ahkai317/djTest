from django.contrib import admin

# Register your models here.

# ======================================================================
# 0410 DRF前置補充
# from .models import ArticlePost

# admin.site.register(ArticlePost)
# ======================================================================

from .models import Article

admin.site.register(Article)
# admin.site.register(Articletest)