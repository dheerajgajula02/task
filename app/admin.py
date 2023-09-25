from django.contrib import admin
from .models import User, Author, Book

admin.site.register(User)
admin.site.register(Author)
admin.site.register(Book)




from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.contrib.admin.widgets import AutocompleteSelectMultiple

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_authors')
    formfield_overrides = {
        models.ForeignKey('Author', on_delete=models.CASCADE): {
            'form_class': ModelChoiceField,
            'queryset': Author.objects.all(),
        },
        models.ArrayField(models.ForeignKey('Author', on_delete=models.CASCADE), blank=True, null=True): {
            'form_class': ModelMultipleChoiceField,
            'queryset': Author.objects.all(),
            'widget': AutocompleteSelectMultiple('Author', field_name='name'),
        }
    }

