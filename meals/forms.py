from django import forms
from .widgets import CustomClearableFileInput
from .models import Meal, Category


class MealForm(forms.ModelForm):

    class Meta:
        model = Meal
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        slug = [(c.id, c.get_slug()) for c in categories]

        self.fields['category'].choices = slug
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
