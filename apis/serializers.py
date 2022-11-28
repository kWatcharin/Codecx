from rest_framework import serializers

from store_app.models import Book


class BookSerializer(serializers.ModelSerializer):
    """ModelSerializer ของ Book Model."""
    
    class Meta:
        model = Book
        fields = [
            'id','book_title_eng', 'book_title_jp', 
            'contributor', 'artist', 'publisher',
            'isbn', 'year', 'volume_no', 'premium_price', 
            'normal_price'
        ]
