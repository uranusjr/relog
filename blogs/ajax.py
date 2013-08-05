from docutils.core import publish_parts
from django.http import HttpResponse


def render_post_raw_content(request):
    raw = request.POST['content']
    compiled = publish_parts(raw, writer_name='html')['html_body']
    return HttpResponse(compiled)
