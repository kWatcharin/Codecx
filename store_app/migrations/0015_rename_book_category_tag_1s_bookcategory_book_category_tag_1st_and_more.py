# Generated by Django 4.1.1 on 2022-10-18 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0014_rename_book_category_tag_bookcategory_book_category_tag_1s_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookcategory',
            old_name='book_category_tag_1s',
            new_name='book_category_tag_1st',
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='book_category_tag_2st',
            field=models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], default='N/A', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='book_category_tag_3st',
            field=models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], default='N/A', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='book_category_tag_4st',
            field=models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], default='N/A', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='bookcategory',
            name='book_category_tag_5st',
            field=models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], default='N/A', max_length=25, null=True),
        ),
    ]