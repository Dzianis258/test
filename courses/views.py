from .models import Course, Lesson
from django.views.generic import ListView, DetailView, CreateView


class HomePage(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['id']

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(HomePage, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта'
        return ctx


class CourseDetailPage(DetailView):
    model = Course
    template_name = 'courses/course-detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailPage, self).get_context_data(**kwargs)
        ctx['title'] = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['lessons'] = Lesson.objects.filter(course=ctx['title']).order_by('number')
        # print(ctx['lessons'].query) если нужно узнать какой запрос к базе
        return ctx


class LessonDetailPage(DetailView):
    model = Course
    template_name = 'courses/lesson_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(LessonDetailPage, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        lesson = list(Lesson.objects.filter(course=course).filter(slug=self.kwargs['lesson_slug']).values())
        ctx['title'] = lesson[0]['title']
        ctx['desc'] = lesson[0]['description']
        ctx['video'] = lesson[0]['video_url'].split('=')[1]
        return ctx


class CourseAddPage(CreateView):
    model = Course
    template_name = 'courses/add-course.html'
    fields = ['slug', 'title', 'description', 'img']

    def form_valid(self, form): #встроенная функция, которая срабатывает перед сохранением данных в БД
        if not Course.objects.filter(slug=form.instance.slug):
            return super().form_valid(form)
        else:
            form.add_error(error="Такое название URL уже есть в базе данных придумайте другое", field='slug')
            return super().form_invalid(form)

    def get_context_data(self, *, object_list=None, **kwards):
        ctx = super(CourseAddPage, self).get_context_data(**kwards)
        ctx['title'] = 'Добавить курс'
        return ctx