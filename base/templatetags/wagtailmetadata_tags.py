from django import template

from base.templatetags import meta_tags

register = template.Library()


@register.simple_tag(takes_context=True)
def meta_tags(context, model=None):
    request = context.get('request', None)
    if not model:
        model = context.get('self', None)

    return meta_tags.meta_tags(request, model)
