from django.db import models


# Create your models here.

class Publisher(models.Model):
    """A publisher that published the lightnovel."""

    publisher_title = models.CharField(max_length=20, help_text="The name of the publisher.", 
        null=True, blank=True)
    website = models.URLField(help_text="The publisher's website.",
        null=True, blank=True)
    email = models.EmailField(help_text="The publisher's email.",
        null=True, blank=True)

    class meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.publisher_title}"


class Contributor(models.Model):
    """A contributor that wrote the lightnovel."""

    contributor_title = models.CharField(max_length=20, help_text="The title of the author.",
        null=True, blank=True)

    class meta:
        verbose_name_plural = 'Contributors'

    def __str__(self):
        return f"{self.contributor_title}"


class Artist(models.Model):
    """The artist that illustrated the illustration of the lightnovel."""

    artist_title = models.CharField(max_length=40, help_text="The artist's title.",
        null=True, blank=True)

    class meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return f"{self.artist_title}"


class LanguagesLightnovel(models.Model):
    """for the language of the lightnovel selection."""

    languages_lightnovel_choices = [
        ("ENGLISH" ,"English"),
        ("JAPANESE", "Japanese"),
    ]

    language_lightnovel_select = models.CharField(max_length=10, choices=languages_lightnovel_choices,
        default='ENGLISH')

    class meta:
        verbose_name_plural = 'LanguageLightnovels'

    def __str__(self):
        return f"{self.language_lightnovel_select}"


class LightnovelCategory(models.Model):
    """for category of the ightnovel selection."""

    lightnovel_category_choices = [('N/A', 'n/a'),
        ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), 
        ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), 
        ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), 
        ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), 
        ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), 
        ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), 
        ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), 
        ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), 
        ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), 
        ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical'),
    ]

    lightnovel_1st_category = models.CharField(max_length=25, choices=lightnovel_category_choices,
        null=True, blank=True, default='N/A')
    lightnovel_2nd_category = models.CharField(max_length=25, choices=lightnovel_category_choices,
        null=True, blank=True)
    lightnovel_3rd_category = models.CharField(max_length=25, choices=lightnovel_category_choices,
        null=True, blank=True)
    lightnovel_4th_category = models.CharField(max_length=25, choices=lightnovel_category_choices, 
        null=True, blank=True)
    lightnovel_5th_category = models.CharField(max_length=25, choices=lightnovel_category_choices,
        null=True, blank=True)

    lightnovel_tag_label = models.CharField(max_length=255, help_text="For the lightnovel short detail.",
        null=True, blank=True)

    class meta:
        verbose_name_plural = 'Lightnovelcategories'

    def __str__(self):
        return f"""
        {self.lightnovel_tag_label}.title(),
        {self.lightnovel_1st_category}, 
        {self.lightnovel_2nd_category}, 
        {self.lightnovel_3rd_category}, 
        {self.lightnovel_4th_category}, 
        {self.lightnovel_5th_category},
        """


class StockStatus(models.Model):
    """An attribute that is status of the stock."""
   
    stock_status_choices = [
        ('IN STOCK', 'In stock'),
        ('OUT OF STOCK', 'Out of stock'),
    ]

    stock_status = models.CharField(max_length=15, choices=stock_status_choices,
                    null=True, blank=True, default='IN STOCK')

    def __str__(self):
        return f"{self.stock_status}"

class Lightnovel(models.Model):
    """A ligtnovel profile."""

    lightnovel_title_eng = models.CharField(max_length=200, help_text="The title of the book in english.", 
        db_index=True, null=True, blank=True)
    lightnovel_title_jp = models.CharField(max_length=200, help_text="The title of the book in japanese.",
        db_index=True, null=True, blank=True)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE,
        null=True, blank=True, help_text="The contributor of the lightnovel.")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,
        null=True, blank=True, help_text="The artist of the lightnovel.")
    isbn_number = models.CharField(max_length=20, unique=True, db_index=True,
        verbose_name="ISBN numbers of the book.", null=True, blank=True)
    year = models.CharField(max_length=4, help_text="The first year of lightnovel that was published.",
        null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
        null=True, blank=True)
    lightnovel_category = models.ForeignKey(LightnovelCategory, on_delete=models.CASCADE,
        null=True, blank=True)
    Lightnovel_description = models.TextField(help_text="For the lightnovel's description.", 
        null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    pages = models.CharField(max_length=4, help_text="The book's page.",
        null=True, blank=True)
    image = models.ImageField('/image', help_text="For the image.",
        null=True, blank=True)
    volume_no = models.CharField(max_length=3, help_text="The volume's number of the lightnovel.",
        null=True, blank=True)
    stock_volume = models.IntegerField(help_text="The stock of the lightnovel in the warehouse.",
        null=True, blank=True)
    stock_status_now = models.ForeignKey(StockStatus, help_text="The status of the stock.", on_delete=models.CASCADE)
    datetime_stock = models.DateTimeField()
    premium_price = models.DecimalField(max_digits=6, decimal_places=2, 
                        help_text="The premium price of the lightnovel.", 
                        null=True, blank=True)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, 
                        help_text="The normal price of the lightnovel.", 
                        null=True, blank=True)
    language_lightnovel = models.ForeignKey(LanguagesLightnovel, on_delete=models.CASCADE,
        help_text="The language of the lightnovel.")

    class meta:
        verbose_name_plural = 'Lightnovels'
        ordering = ['-datetime_stock']

    def __str__(self):
        return f"""
        {self.lightnovel_title_eng},
        {self.lightnovel_title_jp},
        {self.contributor},
        {self.artist},
        """
    



        
    

