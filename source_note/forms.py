from django.forms import ModelForm, Textarea, TextInput

from .models import Section

form_control = "w-full px-3 py-2 border-1 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 focus:ring focus:bg-blue-100"
class SectionCreateForm(ModelForm):
    class Meta:
        model = Section
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                "class": f"{form_control}",
                "placeholder": "Enter section name"
            }),
            "description": Textarea(attrs={
                "class": f"{form_control}",
                "placeholder": "Enter a brief section info",
            }),
        }
