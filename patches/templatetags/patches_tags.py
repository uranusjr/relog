from django.template import Library


register = Library()


@register.inclusion_tag('includes/paginator.html', takes_context=True)
def pagination(context, page, page_param_key='page'):
    """Generate paging widget for page object."""
    get_params = context['request'].GET.copy()
    if page_param_key in get_params:
        del get_params[page_param_key]
    query_string = get_params.urlencode()
    return {
        'page': page,
        'page_param_key': page_param_key,
        'query_string': query_string
    }
