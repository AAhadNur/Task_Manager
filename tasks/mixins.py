from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


class OwnerRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.created_by != self.request.user:
            raise Http404("You are not allowed to edit this task.")
        return super().dispatch(request, *args, **kwargs)
