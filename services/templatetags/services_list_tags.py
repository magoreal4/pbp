from django import template

from wagtail.core.models import Page, Site

from services.models import ServicesPage


register = template.Library()
# https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/

@register.inclusion_tag('tags/service_list.html', takes_context=False)
def serviceslist():
    servicios = ServicesPage.objects.first()
    url = '/servicios/'
    if servicios:
        return {
            'list': servicios.n_servicios.all,
            }


# @register.inclusion_tag('base/include/footer_text.html', takes_context=True)
# def get_footer_text(context):
#     footer_text = ""
#     if FooterText.objects.first() is not None:
#         footer_text = FooterText.objects.first().body

#     return {
#         'footer_text': footer_text,
#     }
