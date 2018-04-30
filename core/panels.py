from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


class SearchEngineOptimisationPanel(MultiFieldPanel):
    heading = 'Search Engine Optimisation'
    children = [
        FieldPanel('seo_title'),
        FieldPanel('search_description'),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(children=self.children, heading=self.heading)
