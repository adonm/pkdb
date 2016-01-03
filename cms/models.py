from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.http import HttpResponseRedirect

from wagtail.wagtailsearch import index
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel


class Content(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('rich_text', blocks.RichTextBlock()),
        ('raw', blocks.RawHTMLBlock()),
        ('include_content', blocks.CharBlock()),
        ('content_list', blocks.CharBlock()),
    ], null=True, blank=True)
    date = models.DateField("Content updated date", default=timezone.now)

    promote_panels = Page.promote_panels + [
        FieldPanel('date'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    search_fields = Page.search_fields + (
        index.SearchField('body'),
        index.FilterField('url_path'),
    )

    def serve(self, request):
        if "draft" in request.GET:
            return HttpResponseRedirect("/admin/pages/{}/view_draft/".format(self.pk))
        return super(Content, self).serve(request)

    class Meta:
        ordering = ("date",)
