from django.db import models

class AboutApplication(models.Model):
    title = models.CharField(max_length=200, default="About Application")
    content = models.TextField(help_text="Enter details about the developer and the application functionality.")
    image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Optional: Upload an image of the developer.")

    def __str__(self):
        return self.title

class ContactDetails(models.Model):
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn profile URL")
    github = models.URLField(blank=True, null=True, help_text="GitHub profile URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter profile URL")
    email = models.EmailField(blank=True, null=True, help_text="Contact email address")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Contact phone number")

    def __str__(self):
        return "Contact Details"

