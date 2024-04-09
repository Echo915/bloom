from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from .models import Section, Note
from .forms import SectionCreateForm

# Create your views here.
class SectionView(ListView):
    model = Section
    form_class = SectionCreateForm
    template_name = "sections.html"
    success_url = reverse_lazy("sections") 
    paginate_by = 10

    # def form_valid(self, form):
    #     form.instance.creator = self.request.user
    #     return super().form_valid(form)
    
    # def get_queryset(self):
    #     user = self.request.user
    #     return Section.objects.filter(creator=user)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["section_list"] = self.object_list
    #     return context

def newSectionView(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        
        new_section = Section()
        new_section.title = title
        new_section.description = description
        new_section.creator = request.user 
        new_section.save()
        
        return JsonResponse({"title": title, "description": description})
        # else:
        #     return JsonResponse({"error": "Unable to create section"}, status=400)
    else:
        return JsonResponse({"error": "No data posted"})

class SectionDetailView(DetailView):
    model = Section
    template_name = "section_detail.html"

def NoteView(request):
    if request.method == "POST":
        if request.FILES:
            posted_file = request.FILES["file"]
            full_name = posted_file.name.split(".")
            file_name = full_name[0]
            file_ext = full_name[1]

            new_file = Note()
            new_file.title = file_name
            new_file.extension = file_ext
            new_file.creator = request.user
            new_file.section = Section.objects.get(id=request.POST.get("section_id"))
            new_file.file = posted_file
            new_file.save()
            return JsonResponse({"status": "success"})
        # else:
        #     return JsonResponse({"error": "Unable to create section"}, status=400)
    else:
        return JsonResponse({"error": "No data posted"}, status=400)

