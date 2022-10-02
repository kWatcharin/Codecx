from django.db import models


# Create your models here.

# Publishers's Profile Class.
class Publishers(models.Model):
    """A publisher that published the lightnovel."""

    publisher_title = models.CharField(max_length=20, help_text="The name of the publisher.")
    website = models.URLField(help_text="The publisher's website.")
    email = models.EmailField(help_text="The publisher's email.")

    def __str__(self):
        return self.publisher_title


# Contributors's Profile Class.
class Contributors(models.Model):
    """A contributor that wrote the lightnovel."""

    contributor_title = models.CharField(max_length=20, help_text="The title's author.")

    def __str__(self):
        return self.autor_title

# Artist's Profile Class.
class Artists(models.Model):
    """An Artist's attributes."""

    artist_title = models.CharField(max_length=20, help_text="The artist's title.")

    def __str__(self):
        return self.artist_title


# Book's languages Profile Class.
class LanguagesLightnovel(models.Model):
    """Attribute's language of lightnovels."""

    languages_lightnovel_choices = [
        {"ENGLISH" :"English"},
        {"JAPANESE": "Japanese"},
    ]

    language_lightnovel = models.CharField(max_length=10, choices=languages_lightnovel_choices)

    def __str__(self):
       return self.language_lightnovel


# Genres Profile.
class LightnovelCategories(models.Model):
    """All attrbutes's categories of the lightnovel."""

    lightnovel_category_choices = [
        {'ACTION': 'Action'}, {'DRAMA': 'Drama'}, {'ADVENTURE': 'Adventure'}, 
        {'COMEDY': 'Comedy'}, {'DRAMA', 'Drama'}, {'ECCHI': 'Ecchi'}, 
        {'FANTASY': 'Fantasy'}, {'GENDER BENDER': 'Gender Bender'}, {'HAREM': 'Harem'}, 
        {'HISTORICAL': 'Historical'}, {'HORROR': 'Horror'}, {'JOSEI': 'Josei'}, 
        {'MATURE': 'Mature'}, {'MACHANICAL': 'Mechanical'}, {'MYSTERY': 'Mystery'}, 
        {'PSYCHOLOGICAL': 'Psychological'}, {'ROMANCE': 'Romance'}, {'SCHOOL LIFE': 'School Life'}, 
        {'SCI-FI': 'Sci-Fi'}, {'SEINEN': 'Seinen'}, {'SHOJOU': 'Shojou'}, 
        {'Shonen': 'Shonen'}, {'SHOJOU AI': 'Shojou Ai'}, 
        {'SLICE OF LIFE': 'Slice of Life'}, {'SPORT': 'Sport'}, {'TRAGEDY': 'Tragedy'}, 
        {'YAOI': 'Yaoi'}, {'YURI': 'Yuri'}, {'ISEKAI': 'Isekai'}, {'MAGICAL': 'Magical'},
    ]
    
    lightnovel_1st_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)
    lightnovel_2nd_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)
    lightnovel_3rd_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)
    lightnovel_4th_category = models.CharField(max_length=20, choices=lightnovel_category_choices, 
                                null=True, black=True)
    lightnovel_5th_category = models.CharField(max_length=20, choices=lightnovel_category_choices,
                                null=True, blank=True)


# Books's Profile.
class Lightnovel(models.Model):
    """A ligtnovel profile."""

    lightnovel_title_eng = models.CharField(max_length=200, help_text="The title of the book in english.", db_index=True)
    lightnovel_title_jp = models.CharField(max_length=200, help_text="The title of the book in japanese.", db_index=True)
    contributor = models.ForeignKey(Contributors, relate_name='contributor', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artists, relate_name='artist', on_delete=models.CASCADE)
    isbn_numbers = models.CharField(max_lenght=20, unique=True, db_index=True, verbose_name="ISBN numbers of the book.")
    years = models.CharField(max_length=5, help_text="The first years of lightnovel that was published.")
    publisher = models.ForeignKey(Publishers, relate_name='publisher', on_delete=models.CASCADE)
    lightnovel_category = models.ManyToManyField(LightnovelCategories)
    Lightnovel_description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    pages = models.IntegerField(help_text="The book's page.")
    images = models.ImageField()
    stock_volume = models.IntegerField()
    in_stock = models.BooleanField()
    stocking_price = models.DecimalField()
    selling_price = models.DecimalField()
    language_lightnovel = models.ForeignKey(LanguagesLightnovel, on_delete=models.CASCADE)

    class meta:
        verbose_name_plural = 'lightnovels'

    def __str__(self):
        return self.lightnovel_title_eng
    
    def __str__(self):
        return self.lightnovel_title_jp


# Order's profile.
class OrderList(models.Model):
    all_lightnovels = models.ForeignKey(Lightnovel, max_length=200, 
                    null=True, blank=True, on_delete=models.CASCADE)
    all_stock_volume = models.ForeignKey(Lightnovel, max_length=4,
                    null=True, blank=True, on_delete=models.CASCADE)
    all_order_price = models.ForeignKey(Lightnovel, max_length=False,
                    null=True, blank=True, on_delete=models.CASCADE) 
    time_created = models.DateTimeField(auto_add_now=True)

    def __str__(self):
        return self.lightnovels.lightnovel_title_eng

    def __str__(self):
        return self.lightnovels.lightnovel_title_jp





        
    

