from django import template
from django.shortcuts import render_to_response

register = template.Library()


@register.filter
def get_excerpt(page):
    result = render_to_response('cms/include_content.html', context={
        "self": page,
        "embed": True})
    return result.content


@register.inclusion_tag('cms/include_content.html', takes_context=True)
def include_content(context, value):
    from cms.models import Content
    try:
        page = Content.objects.get(slug=value)
    except Exception as e:
        page = None
        context.update({"error": "{}: {}".format(value, e)})
    context.update({"self": page})
    return context
