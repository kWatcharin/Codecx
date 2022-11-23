from rest_framework import serializers

from store_app.models import Book, Contributor


class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'book_title_eng', 'book_title_jp', 'contributor', 'artist', 'publisher',
            'isbn', 'year', 'volume_no', 'premium_price', 'normal_price'
        ]


class ContributorSerializers(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'