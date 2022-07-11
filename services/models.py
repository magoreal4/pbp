from __future__ import unicode_literals

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import (
    FieldPanel, 
    InlinePanel, 
    StreamFieldPanel,
    MultiFieldPanel
)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from streams.blocks import BaseStreamBlock
from wagtail.core.fields import RichTextField
from base.fields import MonospaceField

class ServicesPage(Page):

    subtitle = models.CharField(
        max_length = 50,
        help_text='Titulo de la pagina',
        blank=True,
        null=True
        )

    introduction = MonospaceField(
        help_text='Descripcion de los servicios',
        blank=True,
        null=True
        )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('introduction', classname="full"),
        InlinePanel('n_servicios', heading='Nuestros Servicios')
    ]

    parent_page_types = ['home.HomePage']

class Services(Orderable):
    page = ParentalKey(
        ServicesPage, 
        on_delete=models.CASCADE,
        related_name='n_servicios'
        )
    
    title = models.CharField(
        max_length=25, 
        blank=False, 
        null=True
        )

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    description = RichTextField(
        blank=True, 
        )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('image'),
        FieldPanel('description', classname="full"),
    ]


    # Speficies that only BlogPage objects can live under this index page
    

    # Defines a method to access the children of the page (e.g. BlogPage
    # objects). On the demo site we use this on the HomePage
    # def children(self):
    #     return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # https://docs.wagtail.org/en/stable/getting_started/tutorial.html#overriding-context
    # def get_context(self, request):
    #     context = super(BlogIndexPage, self).get_context(request)
    #     context['posts'] = BlogPage.objects.descendant_of(
    #         self).live().order_by(
    #         '-date_published')
    #     return context

    # # This defines a Custom view that utilizes Tags. This view will return all
    # # related BlogPages for a given Tag or redirect back to the BlogIndexPage.
    # # More information on RoutablePages is at
    # # https://docs.wagtail.org/en/stable/reference/contrib/routablepage.html
    # @route(r'^tags/$', name='tag_archive')
    # @route(r'^tags/([\w-]+)/$', name='tag_archive')
    # def tag_archive(self, request, tag=None):

    #     try:
    #         tag = Tag.objects.get(slug=tag)
    #     except Tag.DoesNotExist:
    #         if tag:
    #             msg = 'There are no blog posts tagged with "{}"'.format(tag)
    #             messages.add_message(request, messages.INFO, msg)
    #         return redirect(self.url)

    #     posts = self.get_posts(tag=tag)
    #     context = {
    #         'tag': tag,
    #         'posts': posts
    #     }
    #     return render(request, 'blog/blog_index_page.html', context)

    # def serve_preview(self, request, mode_name):
    #     # Needed for previews to work
    #     return self.serve(request)

    # # Returns the child BlogPage objects for this BlogPageIndex.
    # # If a tag is used then it will filter the posts by tag.
    # def get_posts(self, tag=None):
    #     posts = BlogPage.objects.live().descendant_of(self)
    #     if tag:
    #         posts = posts.filter(tags=tag)
    #     return posts

    # # Returns the list of Tags for all child posts of this BlogPage.
    # def get_child_tags(self):
    #     tags = []
    #     for post in self.get_posts():
    #         # Not tags.append() because we don't want a list of lists
    #         tags += post.get_tags
    #     tags = sorted(set(tags))
    #     return tags
# class ServicePage(Page):

#     subtitle = models.TextField(
#         help_text='Tipo de Servicio',
#         blank=True)

#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+',
#         help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
#     )
#     body = StreamField(
#         BaseStreamBlock(), verbose_name="Page body", blank=True
#     )

#     content_panels = Page.content_panels + [
#         FieldPanel('subtitle', classname="full"),
#         ImageChooserPanel('image'),
#         StreamFieldPanel('body'),
#     ]

#     # Specifies parent to BlogPage as being BlogIndexPages
#     parent_page_types = ['ServiceIndexPage']

#     # Specifies what content types can exist as children of BlogPage.
#     # Empty list means that no child content types are allowed.
#     subpage_types = []
