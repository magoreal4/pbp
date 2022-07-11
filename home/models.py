from __future__ import unicode_literals
from pydoc import classname

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page, Orderable
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from streams.blocks import ImageCaptionBlock

from wagtailsvg.models import Svg
from wagtailsvg.blocks import SvgChooserBlock
from wagtailsvg.edit_handlers import SvgChooserPanel

from base.fields import MonospaceField
from base.models import MetadataPageMixin

from services.models import ServicesPage

class HomePage(MetadataPageMixin, Page):

    subtitle = models.CharField(
        "Sub Titulo",
        max_length=50,
        blank=True,
        null=True,
        help_text="Subitulo o slogan",
        )
    description = MonospaceField(
        "Descripcion",
        blank=True,
        null=True,
        help_text="Descripción General",
        )
    slideTime = models.IntegerField(
        "Tiempo", 
        default=7000, 
        help_text="Tiempo en milisegundos"
        )

    effects_image = models.BooleanField(
        "Efectos Imagenes", 
        default=True, 
        help_text="Efecto imagen Aro"
        )
    repeat = models.BooleanField(
        "Repetición", 
        default=False, 
        help_text="Repite indefinidamente"
        )
    effects_text = models.BooleanField(
        "Efectos Texto", 
        default=True, 
        help_text="Efectos de texto"
        )
    # PROMOCION
    title_promo = models.CharField(
        "Titulo",
        max_length=20,
        default="Ahora",
        blank=True,
        null=True,
        help_text="Titulo Promocion, si queda vacio no se mostrará la Promoción"
    )
    precio_promo = models.IntegerField(
        "Precio",
        default="30",
        blank=True,
        null=True,
        help_text="Precio"
    )

    unidad_promo = models.CharField(
        "Unidad",
        max_length=10,
        default="persona",
        blank=True,
        null=True,
        help_text="Unidad (persona/grupo/equipo"
    )
    descripcion_promo = models.TextField(
        "Descripción",
        max_length=50,
        default="",
        blank=True,
        null=True,
        help_text="Descripcion Corta"
    )
     
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['servicios'] = ServicesPage.objects.first()
        return context

    # mixturecards = StreamField(
    #     [
    #         ("mixturecards", ImageCaptionBlock()),
    #     ],
    #     null=True,
    #     blank=True
    # )
        
    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        FieldPanel('description'),

        MultiFieldPanel([
            FieldPanel("title_promo"),
            FieldPanel("precio_promo"),
            FieldPanel("unidad_promo"),
            FieldPanel("descripcion_promo"),
            InlinePanel("promo_features", label="Caracteristicas"),
        ], heading="Promoción"),

        MultiFieldPanel([
            FieldPanel("slideTime"),
            FieldPanel("effects_image"),
            FieldPanel("effects_text"),
            FieldPanel("repeat"),
            InlinePanel("carousel_images", max_num=5, min_num=1, label="Imagenes Carrosel"),
        ], heading="Imagenes Carrusel"),

        # MultiFieldPanel([
        #     StreamFieldPanel("mixturecards"),
        # ], heading="Servicios xxx"),
    
    ]

class HomePageBanner(Orderable):
    page = ParentalKey(
        HomePage, 
        on_delete=models.CASCADE,
        related_name='carousel_images'
        )
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(
        max_length=30,
        blank=False, 
        null=True
        )
    description = MonospaceField(
        blank=True, 
        max_length=100
        )

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('title'),
        FieldPanel('description'),
    ]

class HomePagePromoFeatures(Orderable):
    page = ParentalKey(
        HomePage, 
        on_delete=models.CASCADE,
        related_name='promo_features'
        )

    caracteristicas = models.CharField(
        max_length=25, 
        blank=False, 
        null=True
        )
    
    panels = [
        FieldPanel('caracteristicas'),
    ]




    # Hero section of HomePage
    # image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Homepage image'
    # )
    # hero_text = models.CharField(
    #     null=True,
    #     blank=True,
    #     max_length=255,
    #     help_text='Write an introduction for the bakery'
    # )
    # hero_cta = models.CharField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Hero CTA',
    #     max_length=255,
    #     help_text='Text to display on Call to Action'
    # )
    # hero_cta_link = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     verbose_name='Hero CTA link',
    #     help_text='Choose a page to link to for the Call to Action'
    # )

    # # Body section of the HomePage
    # body = StreamField(
    #     BaseStreamBlock(), verbose_name="Home content block", blank=True
    # )

    # # Promo section of the HomePage
    # promo_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Promo image'
    # )
    # promo_title = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # promo_text = RichTextField(
    #     null=True,
    #     blank=True,
    #     help_text='Write some promotional copy'
    # )

    # # Featured sections on the HomePage
    # # You will see on templates/base/home_page.html that these are treated
    # # in different ways, and displayed in different areas of the page.
    # # Each list their children items that we access via the children function
    # # that we define on the individual Page models e.g. BlogIndexPage
    # featured_section_1_title = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # featured_section_1 = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='First featured section for the homepage. Will display up to '
    #     'three child items.',
    #     verbose_name='Featured section 1'
    # )

    # featured_section_2_title = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # featured_section_2 = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Second featured section for the homepage. Will display up to '
    #     'three child items.',
    #     verbose_name='Featured section 2'
    # )

    # featured_section_3_title = models.CharField(
    #     blank=True,
    #     max_length=255,
    #     help_text='Title to display above the promo copy'
    # )
    # featured_section_3 = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='Third featured section for the homepage. Will display up to '
    #     'six child items.',
    #     verbose_name='Featured section 3'
    # )

    # content_panels = Page.content_panels + [
    #     MultiFieldPanel([
    #         ImageChooserPanel('image'),
    #         FieldPanel('hero_text', classname="full"),
    #         MultiFieldPanel([
    #             FieldPanel('hero_cta'),
    #             PageChooserPanel('hero_cta_link'),
    #         ]),
    #     ], heading="Hero section"),
    #     MultiFieldPanel([
    #         ImageChooserPanel('promo_image'),
    #         FieldPanel('promo_title'),
    #         FieldPanel('promo_text'),
    #     ], heading="Promo section"),
    #     StreamFieldPanel('body'),
    #     MultiFieldPanel([
    #         MultiFieldPanel([
    #             FieldPanel('featured_section_1_title'),
    #             PageChooserPanel('featured_section_1'),
    #         ]),
    #         MultiFieldPanel([
    #             FieldPanel('featured_section_2_title'),
    #             PageChooserPanel('featured_section_2'),
    #         ]),
    #         MultiFieldPanel([
    #             FieldPanel('featured_section_3_title'),
    #             PageChooserPanel('featured_section_3'),
    #         ]),
    #     ], heading="Featured homepage sections", classname="collapsible")
    # ]

    # def __str__(self):
    #     return self.title
