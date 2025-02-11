from django.db import models

# Company Information Model
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    country = models.CharField(max_length=10)  # Can be validated in a form later
    date_of_engagement = models.DateField()
    business_interests = models.TextField()
    contact_person = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    status = models.TextField(default="Pending Review")  # Default text prevents migration issues
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.country}"

# Zimbabwe Economic Data Model

class ZimbabweEconomicData(models.Model):
    date = models.DateField()
    central_bank_rate = models.DecimalField(max_digits=5, decimal_places=2)
    reserve_money = models.DecimalField(max_digits=15, decimal_places=2)
    broad_money_m3 = models.DecimalField(max_digits=15, decimal_places=2)
    usd_yoy_inflation = models.DecimalField(max_digits=5, decimal_places=2)
    zwg_mom_inflation = models.DecimalField(max_digits=5, decimal_places=2)
    usd_mom_inflation = models.DecimalField(max_digits=5, decimal_places=2)
    official_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    parallel_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    monthly_trade_balance = models.DecimalField(max_digits=15, decimal_places=2)
    gdp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # New GDP field

    def __str__(self):
        return f"Zimbabwe Economic Data ({self.date})"

# Rwanda Economic Data Model
class RwandaEconomicData(models.Model):
    date = models.DateField()
    rwanda_yoy_inflation = models.DecimalField(max_digits=5, decimal_places=2)
    official_exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    monthly_trade_balance = models.DecimalField(max_digits=15, decimal_places=2)
    gdp = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)  # New GDP field

    def __str__(self):
        return f"Rwanda Economic Data ({self.date})"

# diplomacy/models.py (append if not already present)

from django.db import models
from datetime import date

def current_year():
    return date.today().year

class Imihigo(models.Model):
    QUARTER_CHOICES = [
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4'),
    ]
    
    quarter = models.CharField(max_length=2, choices=QUARTER_CHOICES)
    year = models.IntegerField(default=current_year)  # New field with default current year for new records
    baseline_target = models.FloatField()  
    actual_result = models.FloatField()      
    comments = models.TextField(blank=True)
    
    @property
    def variance(self):
        if self.baseline_target:
            return ((self.baseline_target - self.actual_result) / self.baseline_target) * 100
        return None

    def __str__(self):
        return f"Imihigo: {self.get_quarter_display()} ({self.year})"

