# Generated by Django 4.1.1 on 2022-10-05 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_title', models.CharField(help_text="The artist's title.", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contributor_title', models.CharField(help_text="The title's author.", max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LanguagesLightnovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_lightnovel', models.CharField(choices=[('ENGLISH', 'English'), ('JAPANESE', 'Japanese')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='LightnovelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lightnovel_1st_category', models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], default='N/A', max_length=25, null=True)),
                ('lightnovel_2nd_category', models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], max_length=25, null=True)),
                ('lightnovel_3rd_category', models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], max_length=25, null=True)),
                ('lightnovel_4th_category', models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], max_length=25, null=True)),
                ('lightnovel_5th_category', models.CharField(blank=True, choices=[('N/A', 'n/a'), ('ACTION', 'Action'), ('DRAMA', 'Drama'), ('ADVENTURE', 'Adventure'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('ECCHI', 'Ecchi'), ('FANTASY', 'Fantasy'), ('GENDER BENDER', 'Gender Bender'), ('HAREM', 'Harem'), ('HISTORICAL', 'Historical'), ('HORROR', 'Horror'), ('JOSEI', 'Josei'), ('MATURE', 'Mature'), ('MACHANICAL', 'Mechanical'), ('MYSTERY', 'Mystery'), ('PSYCHOLOGICAL', 'Psychological'), ('ROMANCE', 'Romance'), ('SCHOOL LIFE', 'School Life'), ('SCI-FI', 'Sci-Fi'), ('SEINEN', 'Seinen'), ('SHOJOU', 'Shojou'), ('Shonen', 'Shonen'), ('SHOJOU AI', 'Shojou Ai'), ('SLICE OF LIFE', 'Slice of Life'), ('SPORT', 'Sport'), ('TRAGEDY', 'Tragedy'), ('YAOI', 'Yaoi'), ('YURI', 'Yuri'), ('ISEKAI', 'Isekai'), ('MAGICAL', 'Magical')], max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publisher_title', models.CharField(help_text='The name of the publisher.', max_length=20)),
                ('website', models.URLField(help_text="The publisher's website.")),
                ('email', models.EmailField(help_text="The publisher's email.", max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_stock_status', models.CharField(choices=[('IN STOCK', 'in stock'), ('OUT OF STOCK', 'in stock')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Lightnovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lightnovel_title_eng', models.CharField(db_index=True, help_text='The title of the book in english.', max_length=200)),
                ('lightnovel_title_jp', models.CharField(db_index=True, help_text='The title of the book in japanese.', max_length=200)),
                ('isbn_number', models.CharField(db_index=True, max_length=20, unique=True, verbose_name='ISBN numbers of the book.')),
                ('year', models.CharField(help_text='The first years of lightnovel that was published.', max_length=5)),
                ('Lightnovel_description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('pages', models.IntegerField(help_text="The book's page.")),
                ('image', models.ImageField(upload_to='', verbose_name='/image')),
                ('stock_volume', models.IntegerField(help_text='The stock of the lightnovel.')),
                ('datetime_stock', models.DateTimeField()),
                ('premium_price', models.DecimalField(blank=True, decimal_places=2, help_text='The premium price of the lightnovel.', max_digits=6, null=True)),
                ('normal_price', models.DecimalField(blank=True, decimal_places=2, help_text='The normal price of the lightnovel.', max_digits=6, null=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.artist')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.contributor')),
                ('language_lightnovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.languageslightnovel')),
                ('lightnovel_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.lightnovelcategory')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_app.publisher')),
                ('stock_status_now', models.ForeignKey(help_text='The status of the stock.', on_delete=django.db.models.deletion.CASCADE, to='store_app.stockstatus')),
            ],
        ),
    ]