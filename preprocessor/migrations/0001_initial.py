# Generated by Django 3.2.7 on 2022-01-09 23:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSV',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('average_length', models.IntegerField(default=0)),
                ('first_review', models.DateField(null=True)),
                ('last_review', models.DateField(null=True)),
                ('total_reviews', models.IntegerField(default=0)),
                ('origin', models.CharField(default='', max_length=100)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('uploaded_by', models.CharField(default='', max_length=100)),
                ('average_rating', models.FloatField(default=0)),
                ('review_id_col', models.CharField(blank=True, max_length=100, null=True)),
                ('date_col', models.CharField(blank=True, max_length=100, null=True)),
                ('rating_col', models.CharField(blank=True, max_length=100, null=True)),
                ('text_col', models.CharField(blank=True, max_length=100, null=True)),
                ('country_col', models.CharField(blank=True, max_length=100, null=True)),
                ('city_col', models.CharField(blank=True, max_length=100, null=True)),
                ('user_col', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]