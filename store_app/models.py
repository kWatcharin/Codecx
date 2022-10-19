from django.db import models
from django.urls import reverse

class Publisher(models.Model):
    """The model for the publisher that published the book(lightnovel)."""

    publisher_title = models.CharField(max_length=30, help_text="The publisher's name.", 
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
    """The model for the contributor that wrote the book(lightnovel)."""

    contributor_title = models.CharField(max_length=30, help_text="The contributor's name.",
        null=True, blank=True)

    class meta:
        verbose_name_plural = 'Contributors'

    def __str__(self):
        return f"{self.contributor_title}"


class Artist(models.Model):
    """The artist that illustrated the illustration of the lightnovel."""

    artist_title = models.CharField(max_length=40, help_text="The artist's name.",
        null=True, blank=True)

    class meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return f"{self.artist_title}"


class BookLanguage(models.Model):
    """The language for the book."""

    book_language_choices = [
        ("ENGLISH" ,"English"),
        ("JAPANESE", "Japanese"),
    ]

    book_language_select = models.CharField(max_length=10, choices=book_language_choices)

    class meta:
        verbose_name_plural = 'BookLanguages'

    def __str__(self):
        return f"{self.book_language_select}"


class BookCategory(models.Model):
    """The model for the book's category."""

    book_category_choices = [('N/A', 'n/a'),
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
    
    book_category_tag_label = models.CharField(max_length=200, help_text="The book(lightnovel)'s tage label.",
        null=True, blank=True)

    book_category_tag_1st = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_2st = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_3st = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_4st = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_5st = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    
    class meta:
        verbose_name_plural = 'BookCategories'

    def __str__(self):
        return f"""
            {self.book_category_tag_label},
            {self.book_category_tag_1st},
            {self.book_category_tag_2st},
            {self.book_category_tag_3st},
            {self.book_category_tag_4st},
            {self.book_category_tag_5st},
            """


class StockStatus(models.Model):
    """The model for stock status checker."""
   
    stock_status_choices = [
        ('IN STOCK', 'In stock'),
        ('OUT OF STOCK', 'Out of stock'),
    ]

    stock_status = models.CharField(max_length=15, choices=stock_status_choices,
                    null=True, blank=True, default='IN STOCK')

    def __str__(self):
        return f"{self.stock_status}"

class Book(models.Model):
    """The model for the book(lightnovel) details."""

    book_title_eng = models.CharField(max_length=200, help_text="The book's name in English.", 
        db_index=True, null=True, blank=True)
    book_title_jp = models.CharField(max_length=200, help_text="The book's name in Japanese(Romaji).",
        db_index=True, null=True, blank=True)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE,
        null=True, blank=True, help_text="The contributor of the book(lightnovel).")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,
        null=True, blank=True, help_text="The artist of the book(lightnovel).")
    isbn = models.CharField(max_length=20, unique=True, db_index=True,
        verbose_name="ISBN numbers of the book.", null=True, blank=True)
    year = models.CharField(max_length=4, help_text="The first year of (book)lightnovel that was published.",
        null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
        null=True, blank=True)
    book_categories = models.ForeignKey(BookCategory, on_delete=models.CASCADE,
        null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    pages = models.CharField(max_length=4, help_text="The book(lightnovel)'s page.",
        null=True, blank=True)
    image = models.ImageField('/store_app/image', help_text="For the book(lightnovel)'s image.",
        null=True, blank=True)
    volume_no = models.CharField(max_length=3, help_text="The volume's number of the (book)lightnovel.",
        null=True, blank=True)
    stock_volume = models.IntegerField(help_text="The stock of the (book)lightnovel in the warehouse.",
        null=True, blank=True)
    stock_status_now = models.ForeignKey(StockStatus, help_text="The status of the stock.", on_delete=models.CASCADE)
    datetime_create = models.DateTimeField()
    premium_price = models.DecimalField(max_digits=6, decimal_places=2, 
                        help_text="The premium price of the (book)lightnovel.", 
                        null=True, blank=True)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, 
                        help_text="The normal price of the (book)lightnovel.", 
                        null=True, blank=True)
    book_language = models.ForeignKey(BookLanguage, on_delete=models.CASCADE,
        help_text="The book(lightnovel)'s language", null=True, blank=True)

    class meta:
        verbose_name_plural = 'Books'
        ordering = ['-datetime_stock']

    def get_absolute_url(self):
        return reverse('book_detail', kwargs=[str(self.slug)])

    def __str__(self):
        return f"""
        {self.book_title_eng},
        {self.book_title_jp},
        {self.contributor},
        {self.artist},
        {self.volume_no},
        {self.book_categories}
        """
    



        
    

