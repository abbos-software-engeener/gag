from django.urls import path
from .views import MainIndex, UploadPost, Postlike, PostCommentView

app_name = 'main'

urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('‘cat/<int:pk>/’', MainIndex.as_view(), name='cat'),
    path('upload/', UploadPost.as_view(), name='upload'),
    path('post/<str:action>/<int:post_id>/', Postlike.as_view(), name="like"),
    path('comment/<int:post_id>/', PostCommentView.as_view(), name='comments')



]
