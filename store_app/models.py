from django.db import models


# Create your models here.

# Publishers's Profile Class.
class Publisher(models.Model):
    """A publisher that published the lightnovel."""

    publisher_title = models.CharField(max_length=20, help_text="The name of the publisher.")
    website = models.URLField(help_text="The publisher's website.")
    email = models.EmailField(help_text="The publisher's email.")

    class meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.publisher_title


# Contributors's Profile Class.
class Contributor(models.Model):
    """A contributor that wrote the lightnovel."""

    contributor_title = models.CharField(max_length=20, help_text="The title's author.")

    class meta:
        verbose_name_plural = 'Contributors'

    def __str__(self):
        return self.autor_title


# Artist's Profile Class.
class Artist(models.Model):
    """An Artist's attributes."""

    artist_title = models.CharField(max_length=20, help_text="The artist's title.")

    class meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.artist_title


# Book's languages Profile Class.
class LanguagesLightnovel(models.Model):
    """Attribute's language of lightnovels."""

    languages_lightnovel_choices = [
        ("ENGLISH" ,"English"),
        ("JAPANESE", "Japanese"),
    ]

    language_lightnovel = models.CharField(max_length=10, choices=languages_lightnovel_choices)

    def __str__(self):
       return self.language_lightnovel


# Genres Profile.
class LightnovelCategory(models.Model):
    """All attrbutes for category of the lightnovel."""

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
    
    lightnovel_1st_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True, default='N/A')
    lightnovel_2nd_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)
    lightnovel_3rd_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)
    lightnovel_4th_category = models.CharField(max_length=20, choices=lightnovel_category_choices, 
                                null=True, black=True)
    lightnovel_5th_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)

    class meta:
        verbose_name_plural = 'Lightnovelcategories'


# Stock Status's Profile.
class StockStatus(models.Model):
    """An attribute that is status of the stock."""
   
    stock_status_choices = [
        ('IN STOCK', 'in stock'),
        ('OUT OF STOCK', 'in stock'),
        ]

    in_stock_status = models.CharField(max_length=15, choices=stock_status_choices)


# Books's Profile.
class Lightnovel(models.Model):
    """A ligtnovel profile."""

    lightnovel_title_eng = models.CharField(max_length=200, help_text="The title of the book in english.", db_index=True)
    lightnovel_title_jp = models.CharField(max_length=200, help_text="The title of the book in japanese.", db_index=True)
    contributor = models.ForeignKey(Contributor, relate_name='contributor', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, relate_name='artist', on_delete=models.CASCADE)
    isbn_number = models.CharField(max_lenght=20, unique=True, db_index=True, verbose_name="ISBN numbers of the book.")
    year = models.CharField(max_length=5, help_text="The first years of lightnovel that was published.")
    publisher = models.ForeignKey(Publisher, relate_name='publisher', on_delete=models.CASCADE)
    lightnovel_category = models.ForeignKey(LightnovelCategory)
    Lightnovel_description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    pages = models.IntegerField(help_text="The book's page.")
    image = models.ImageField('/image')
    stock_volume = models.IntegerField(help_text="The stock of the lightnovel.")
    stock_status_now = models.ForeignKey(StockStatus, help_text="The status of the stock.", on_delete=models.CASCADE)
    datetime_stock = models.DateTimeField(auto_add_now=True)
    premium_price = models.DecimalField(help_text="The premium price of the lightnovel.", null=True, black=True)
    normal_price = models.DecimalField(help_text="The normal price of the lightnovel.", null=True, blank=True)
    language_lightnovel = models.ForeignKey(LanguagesLightnovel, on_delete=models.CASCADE)

    class meta:
        verbose_name_plural = 'Lightnovels'
        ordering = ['-datetime_stock']

    def __str__(self):
        return self.lightnovel_title_eng
    
    def __str__(self):
        return self.lightnovel_title_jp




        
    

