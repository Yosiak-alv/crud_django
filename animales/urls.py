from django.urls import path
from animales import views as v
#conectar con la otra urls
app_name = 'aplication'
urlpatterns = [
    path('',v.inicio , name='inicio'),
    path('detail_<int:id>/',v.detail,name='detail'),
    path('create/',v.create_animal,name='create'),
    path('edit_<int:id>/',v.edit_animal,name='edit'),
    path('delete_<int:id>/',v.delete_animal,name='delete')
]