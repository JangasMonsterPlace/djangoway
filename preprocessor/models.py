from django.db import models
from uuid import uuid4


class CSV(models.Model):
    """
    CSV model
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    # Required for frontend
    average_length = models.IntegerField(default=0)
    first_review = models.DateField(null=True)
    last_review = models.DateField(null=True)
    total_reviews = models.IntegerField(default=0)
    origin = models.CharField(max_length=100, default="")
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=100, default="")
    average_rating = models.FloatField(default=0)

    # required for backend
    review_id_col = models.CharField(max_length=100, blank=True, null=True)
    date_col = models.CharField(max_length=100, blank=True, null=True)
    rating_col = models.CharField(max_length=100, blank=True, null=True)
    text_col = models.CharField(max_length=100, blank=True, null=True)
    country_col = models.CharField(max_length=100, blank=True, null=True)
    city_col = models.CharField(max_length=100, blank=True, null=True)
    user_col = models.CharField(max_length=100, blank=True, null=True)

