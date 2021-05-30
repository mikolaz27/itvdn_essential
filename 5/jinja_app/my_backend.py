from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django.template.loader import get_template

from django.template.backends.django import Engine


class MyBackend(BaseEngine):
    app_dirname = 'example_1'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super().__init__(params)

        self.engine = Engine(**options)

    def get_template(self, template_name):
        try:
            return Template(get_template(template_name))
        except TemplateDoesNotExist as exc:
            raise TemplateDoesNotExist(exc.args, backend=self)


class Template:

    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['my_template'] = 'this is custom'
        print(context)
        return self.template.render(context)
