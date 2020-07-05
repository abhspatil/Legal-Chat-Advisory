from django.contrib import admin

# Register your models here.

from .models import Articles,ArticleDescription,References,Keywords,QueryData

admin.site.register(Articles)
admin.site.register(ArticleDescription)
admin.site.register(References)
admin.site.register(Keywords)
admin.site.register(QueryData)
