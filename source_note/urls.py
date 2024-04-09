from django.urls import path

from .views import SectionView, newSectionView, SectionDetailView, NoteView

urlpatterns = [
    path("", SectionView.as_view(), name="sections"),
    path("section_data", newSectionView, name="section_data"),
    path("section/<int:pk>", SectionDetailView.as_view(), name="section_detail"),
    path("section/note/", NoteView, name="note_add")
    # path("section/<int:pk>/notes", NoteView.as_view(), name="section_notes"), 
]
