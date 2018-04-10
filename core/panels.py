from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel


class SearchEngineOptimisationPanel(MultiFieldPanel):
    heading = 'Search Engine Optimisation'
    children = [
        FieldPanel('slug'),
        FieldPanel('seo_title'),
        FieldPanel('search_description'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(
            heading=self.heading, children=self.children, *args, **kwargs
        )
