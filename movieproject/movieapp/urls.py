# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.index,name='index')   
# ]


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Detail View part1
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.index,name='index'),
#     path('movie/<int:movie_id>/',views.detail,name='detail')
# ]


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Name space in django
from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add/' ,views.add_movie,name='add_movie'),
    # Update part2
    path('update/<int:id>/',views.update,name='update'),
    #Delete
    path('delete/<int:id>/',views.delete,name='delete')]