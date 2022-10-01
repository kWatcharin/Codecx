from django.db import models


# Create your models here.

# Publishers Profile.
class Publishers(models.Model):
    """A publisher that published the lightnovel."""
    publisher_title = models.CharField(max_length=20, help_text="The name of the publisher.")
    website = models.URLField(help_text="The publisher's website.")
    email = models.EmailField(help_text="The publisher's email.")

    def __str__(self):
        return self.publisher_title


# Contributors Profile.
class Contributors(models.Model):
    """A contributor that wrote the lightnovel."""
    autor_title = models.CharField(max_length=20, help_text="The title's author.")

    def __str__(self):
        return self.autor_title

#
class Artists(models.Model):
    pass


# Genres Profile.
class LightNovelGenres(models.Model):
    """All genre of the lightnovel., แนวของ Lightnovel"""
    lightnovel_genre = [
        {'ACTION': 'Action'}, {'DRAMA': 'Drama'}, {'ADULT', 'Adult'}, {'ADVENTURE': 'Adventure'}, {'COMEDY': 'Comedy'}, {'DRAMA', 'Drama'},
        {'ECCHI': 'Ecchi'}, {'FANTASY': 'Fantasy'}, {'GENDER BENDER': 'Gender Bender'}, {'HAREM': 'Harem'}, {'HISTORICAL'},
        {'HORROR': 'Horror'}, {'JOSEI': 'Josei'}, {'MATURE': 'Mature'}, {'MACHA': 'Mecha'}, {'MYSTERY': 'Mystery'}, 
        {'PSYCHOLOGICAL': 'Psychological'}, {'ROMANCE': 'Romance'}, {'SCHOOL LIFE': 'School Life'}, {'SCI-FI': 'Sci-Fi'}, {'SEINEN': 'Seinen'},
        {'SHOJOU': 'Shojou'}, {'Shonen': 'Shonen'}, {'SHOJOU AI': 'Shojou Ai'}, {'SLICE OF LIFE': 'Slice of Life'}, 
        {'SPORT': 'Sport'}, {'TRAGEDY': 'Tragedy'}, {'YAOI': 'Yaoi'}, {'YURI': 'Yuri'}, {'HERROR': 'Horror'},
    ]

    lightnovel_title_eng = models.CharField()
    lightnovel_title_jp = models.CharField()
    lightnovel_genre_1st = models.CharField(max_length=20, choices=lightnovel_genre)
    lightnovel_genre_2nd = models.CharField(max_length=20, choices=lightnovel_genre)
    lightnovel_genre_3rd = models.CharField(max_length=20, choices=lightnovel_genre)
    lightnovel_genre_4th = models.CharField(max_length=20, choices=lightnovel_genre, 
                            null=True, black=True)
    lightnovel_genre_5th = models.CharField(max_length=20, choices=lightnovel_genre,
                            null=True, blank=True)
    


# Books Profile.
class LightNovels(models.Model):
    """A ligtnovel profile., รายละเอียดของไลท์โนเวล"""
    lightnovel_title_eng = models.CharField(max_length=200, help_text="The title of the book in english.", db_index=True)
    lightnovel_title_jp = models.CharField(max_length=200, help_text="The title of the book in japanese.", db_index=True)
    contributors = models.ForeignKey(Contributors, relate_name='contributor', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artists, relate_name='artist', on_delete=models.CASCADE)
    isbn_numbers = models.CharField(max_lenght=20, unique=True, db_index=True, verbose_name="ISBN numbers of the book.")
    years = models.CharField(max_length=5, help_text="The first years of lightnovel that was published.")
    publisher = models.ForeignKey(Publishers, relate_name='publisher', on_delete=models.CASCADE)
    ln_genre = models.ManyToManyField(through='LightNovelGenres')
    descriptions = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    prices = models.DecimalField(help_text="The prices of the book.")
    volumes = models.IntegerField(help_text="The book's volume.")
    pages = models.IntegerField(help_text="The book's page.")
    images = models.ImageField()


    def __str__(self):
        return self.ln_title_eng
    
    def __str__(self):
        return self.ln_title_jp
        
    

