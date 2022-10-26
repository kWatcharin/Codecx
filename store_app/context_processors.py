from store_app.models import Book, Publisher, BookCategory


# The functions for retrieving the particular of the database for using all the templates in this project.
def publishers(request):
    """The function for retrieve the Publisher model for all the templates."""
    return {
        'publishers': Publisher.objects.all()
    }


def books(request):
    """The function for retrieve the Book model for all the templates."""
    return {
        'books': Book.objects.all()
    }