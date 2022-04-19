from django.contrib import admin

from .models import Faq, Answer

class CommentInline(admin.TabularInline):
    model = Answer
@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('category','author','subject','create_date','updated_at')
    inlines=[CommentInline]


