from django.conf import settings
from django.db import models
from django.urls import reverse


class BookManager(models.Manager):

    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(is_active=True)


class Publisher(models.Model):
    """Model: สำนักพิมพ์"""
    publisher_title = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    class meta:
        verbose_name_plural = 'Publishers'

    def __str__(self):
        return f"{self.publisher_title}"


class Contributor(models.Model):
    """Model: ผู้แต่ง"""
    contributor_title = models.CharField(max_length=30, null=True, blank=True)

    class meta:
        verbose_name_plural = 'Contributors'

    def __str__(self):
        return f"{self.contributor_title}"


class Artist(models.Model):
    """Model: อาร์ทติสวาดภาพประกอบ"""
    artist_title = models.CharField(max_length=40, null=True, blank=True)

    class meta:
        verbose_name_plural = 'Artists'

    def __str__(self):
        return f"{self.artist_title}"


class BookLanguage(models.Model):
    """Model: ภาษาที่ตีพิมพ์"""
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
    """Model: ประเภทแนว"""
    book_category_choices = [('N/A', 'n/a'),
        ('Action', 'Action'), ('Drama', 'Drama'), ('Adventure', 'Adventure'), 
        ('Comedy', 'Comedy'), ('Magical', 'Magical'), ('Ecchi', 'Ecchi'), 
        ('Fantasy', 'Fantasy'), ('Gender Bender', 'Gender Bender'), ('Harem', 'Harem'), 
        ('Historical', 'Historical'), ('Horror', 'Horror'), ('Josei', 'Josei'), 
        ('Mature', 'Mature'), ('Mechanical', 'Mechanical'), ('Mystery', 'Mystery'), 
        ('Psychological', 'Psychological'), ('Romance', 'Romance'), ('School Life', 'School Life'), 
        ('Sci-fi', 'Sci-Fi'), ('Seinen', 'Seinen'), ('Shojou', 'Shojou'), 
        ('Shonen', 'Shonen'), ('Shoujou Ai', 'Shojou Ai'), ('Slice of Life', 'Slice of Life'), 
        ('Sport', 'Sport'), ('Tragedy', 'Tragedy'), ('Yaoi', 'Yaoi'), ('Yuri', 'Yuri'), 
        ('Isekai', 'Isekai'), 
    ]
    
    book_category_tag_label = models.CharField(max_length=200,null=True, blank=True)
    book_category_tag_1st = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_2nd = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_3rd = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_4th = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    book_category_tag_5th = models.CharField(max_length=25, choices=book_category_choices,
        null=True, blank=True, default='N/A')
    
    class meta:
        verbose_name_plural = 'BookCategories'

    def __str__(self):
        return f"""
            {self.book_category_tag_label},
            {self.book_category_tag_1st},
            {self.book_category_tag_2nd},
            {self.book_category_tag_3rd},
            {self.book_category_tag_4th},
            {self.book_category_tag_5th},
            """


class StockStatus(models.Model):
    """Model: สถานะใน stock""" 
    stock_status_choices = [
        ('IN STOCK', 'In stock'),
        ('OUT OF STOCK', 'Out of stock'),
    ]

    stock_status = models.CharField(max_length=15, choices=stock_status_choices,
                    null=True, blank=True, default='IN STOCK')

    def __str__(self):
        return f"{self.stock_status}"


class Book(models.Model):
    """Model: หนังสือ"""
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books_creator')
    book_title_eng = models.CharField(max_length=200, db_index=True, null=True)
    book_title_jp = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, blank=True)
    isbn = models.CharField(max_length=20, unique=True, db_index=True, null=True, blank=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True, blank=True)
    book_categories = models.ForeignKey(BookCategory, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    pages = models.CharField(max_length=4, null=True, blank=True)
    image = models.ImageField('/store_app/image', null=True, blank=True)
    volume_no = models.CharField(max_length=3, null=True, blank=True)
    stock_volume = models.IntegerField(null=True, blank=True)
    stock_status_now = models.ForeignKey(StockStatus, on_delete=models.CASCADE)
    is_in_stock = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    premium_price = models.DecimalField(max_digits=6, decimal_places=2,  
                        null=True, blank=True)
    normal_price = models.DecimalField(max_digits=6, decimal_places=2, 
                        null=True, blank=True)
    book_language = models.ForeignKey(BookLanguage, on_delete=models.CASCADE, null=True, blank=True)
    book_description = models.TextField(null=True, blank=True)
    objects = models.Manager()
    books = BookManager()

    class meta:
        verbose_name_plural = 'Books'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('store_app:book_detail', args=[self.id, self.slug])

    def __str__(self):
        return f"""
        {self.book_title_eng},
        {self.book_title_jp},
        {self.contributor},
        {self.artist},
        {self.volume_no},
        {self.book_categories}
        """


        
    

