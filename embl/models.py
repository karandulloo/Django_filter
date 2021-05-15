from django.db import models

class Embl(models.Model):
    # id = models.IntegerField(primary_key=True)
    protein1 = models.CharField(max_length=100)
    protein2 = models.CharField(max_length=100)
    neighborhood = models.IntegerField(blank=True, null=True)
    fusion = models.IntegerField(blank=True, null=True)
    cooccurence = models.IntegerField(blank=True, null=True)
    coexpression = models.IntegerField(blank=True, null=True)
    experimental = models.IntegerField(blank=True, null=True)
    database = models.IntegerField(blank=True, null=True)
    textmining = models.IntegerField(blank=True, null=True)
    combined_score= models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = "MyData"