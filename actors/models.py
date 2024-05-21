from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('FR', 'France'),
    ('DE', 'Germany'),
    ('JP', 'Japan'),
    ('CN', 'China'),
    ('IN', 'India'),
    ('BR', 'Brazil'),
    ('RU', 'Russia'),
    ('KR', 'South Korea'),
    ('IT', 'Italy'),
    ('ES', 'Spain'),
    ('CA', 'Canada'),
    ('AU', 'Australia'),
    ('MX', 'Mexico'),
    ('ID', 'Indonesia'),
    ('TR', 'Turkey'),
    ('NL', 'Netherlands'),
    ('SA', 'Saudi Arabia'),
    ('CH', 'Switzerland'),
    ('AR', 'Argentina'),
    ('SE', 'Sweden'),
    ('BE', 'Belgium'),
    ('AT', 'Austria'),
    ('NO', 'Norway'),
    ('PL', 'Poland'),
    ('TH', 'Thailand'),
    ('AE', 'United Arab Emirates'),
    ('SG', 'Singapore'),
    ('MY', 'Malaysia'),
    ('PH', 'Philippines'),
    ('EG', 'Egypt'),
    ('FI', 'Finland'),
    ('GR', 'Greece'),
    ('PT', 'Portugal'),
    ('CZ', 'Czech Republic'),
    ('IE', 'Ireland'),
    ('HU', 'Hungary'),
    
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True, default='BR')
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name