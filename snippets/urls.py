from django.urls import path
from snippets.views import Snippets, snippet_list, tags

urlpatterns = [
    path('snippets', Snippets.as_view(), name='snippets'),
    path('snippets/<int:pk>', Snippets.as_view(), name='snippets'),
    path('snippets_list', snippet_list, name='snippets_list'),
    path('tags', tags, name='tags'),
    path('tags/<int:id>', tags, name='tags'),

]
