from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('boards', views.BoardViewSet, 'boards')
router.register('tasks', views.TaskViewSet, 'tasks')
router.register('comments', views.CommentViewSet, 'comments')

urlpatterns = router.urls
