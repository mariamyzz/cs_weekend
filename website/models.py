from django.db import models


class Session(models.Model):
    weekend_num = models.IntegerField("weekend number",
                                      help_text="Number of a weekend that the session refers to.",
                                      )
    num = models.IntegerField("session number", unique=True)
    date = models.DateField(auto_now_add=False)
    what_was_done = models.TextField(help_text="Description of what was done on the session")

    # Timestamps
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Session #{}".format(self.num)


class Page(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(default=None)

    # Timestamps
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Announcement(Page):
    pass


class About(Page):
    comment = models.CharField()
    class Meta:
        verbose_name_plural = "about"


class Supplementary(Page):

    class Meta:
        verbose_name_plural = "supplementaries"


class Compendia(Page):

    class Meta:
        verbose_name_plural = "compendia"
