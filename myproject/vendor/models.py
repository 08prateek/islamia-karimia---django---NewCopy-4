from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15, unique=True)
    address = models.TextField()  # New field
    gst_number = models.CharField(max_length=15, unique=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class Tender(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='tenders/', blank=True, null=True)
    document = models.FileField(upload_to='tender_documents/', blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TenderApplication(models.Model):
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)
    vendor_name = models.CharField(max_length=255)
    vendor_contact = models.CharField(max_length=15)
    vendor_email = models.EmailField()
    tender_title = models.CharField(max_length=200)

    class Meta:
        unique_together = ('vendor', 'tender')

    def __str__(self):
        return f"{self.vendor.name} applied for {self.tender.title}"
    