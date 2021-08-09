from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.db import transaction
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from django.utils.translation import gettext_lazy as _

from main.forms import PostCommentForm
from main.models import Post, Category, Post_Comment


class MainIndex(View):
    def get(self, request, pk=None):
        cat = None
        query = Post.objects.order_by('-id')
        if pk is not None:
            query = query.filter(category_id=pk)
            cat = Category.objects.get(id=pk)

        paginator = Paginator(query.all(), 8)
        page = paginator.get_page(request.GET.get('page'))

        return render(request, 'main/index.html', {
            'object_list': page.object_list,
            'page_obj': page,
            'cat': cat
        })


class MainCatAjax(View):
    def get(self, request, pk):
        return HttpResponse("pk= {}".format(pk))


class UploadPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'comment', 'fields', ]
    template_name = 'layouts/form.html'
    success_url = reverse_lazy('main:upload')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Yuklash")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, _("Muvafaqiyatli qo'shildi."))
        return super().form_valid(form)


class Postlike(View):
    def get(self, request, post_id, action):
        if action not in ['like', 'dislike']:
            raise Http404

        def _redirect():
            return redirect(request.GET.get('return', 'main:index'))

        with transaction.atomic():
            try:
                post = Post.objects.select_for_update().get(id=post_id)
            except:
                return _redirect()

            if action == 'like':
                post.like += 1
            else:
                post.dislike += 1

            post.save()
        return _redirect()


class PostCommentView(ListView):
    model = Post_Comment
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().filter(post_id=self.kwargs['post_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['post_id'])
        context['form'] = PostCommentForm

        return context

    def post(self, request, post_id):
        if not request.user.is_authenticated:
            return redirect('main:comments', post_id=self.kwargs['post_id'])

        form = PostCommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            comment: Post_Comment = form.save(commit=False)
            comment.post_id = self.kwargs['post_id']
            comment.user = self.request.user
            comment.save()

            return redirect('main:comments', post_id=comment.post_id)

        return self.get(request)







