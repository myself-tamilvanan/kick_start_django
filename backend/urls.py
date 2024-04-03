from django.urls import path
from .views import home, todos, StudentsView

urlpatterns = [
  path("", home, name="home"),
  path("todos/", todos, name="Todos"),
  path("students/", StudentsView.as_view()),
  path("students/<int:id>/", StudentsView.as_view()),
  path("students/<int:id>/update", StudentsView.as_view()),
]