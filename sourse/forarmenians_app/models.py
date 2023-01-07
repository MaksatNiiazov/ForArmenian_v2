from datetime import datetime
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

User = settings.AUTH_USER_MODEL


# Default Ad


class AdCountry(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.country}'


class AdState(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.state}'


class AdAddress(models.Model):
    country = models.ForeignKey(AdCountry, on_delete=models.CASCADE)
    state = models.ForeignKey(AdState, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.country} {self.state} {self.address}'


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    address = models.ForeignKey(AdAddress, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}'


class AdPhoto(models.Model):
    photo = models.ImageField(upload_to='static/img/ads_photos', null=False)
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f'{self.ad_id}'


# Job


class JobAd(Ad):
    work_graphic = models.CharField(max_length=300)
    education = models.CharField(max_length=200)
    frequency_of_payment = models.CharField(max_length=50, default='per month')
    salary_from = models.PositiveSmallIntegerField(default=1)
    salary_to = models.PositiveSmallIntegerField(default=1)
    currency = models.CharField(max_length=20, default='USD')


class JobKeySkills(models.Model):
    job_ad = models.ForeignKey(JobAd, on_delete=models.CASCADE, related_name='key_skills')
    skill = models.CharField(max_length=50)


class JobWorkExperience(models.Model):
    job_ad = models.ForeignKey(JobAd, on_delete=models.CASCADE, related_name='work_experiences')
    work_place = models.CharField(max_length=300)
    month = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000)],
                                     help_text="How many months did you work?")
    experience = models.TextField()


class JobLanguageSkill(models.Model):
    job_ad = models.ForeignKey(JobAd, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=50)
    level = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.language}/{self.level}'


class JobVacancy(JobAd):
    responsibilities = models.TextField()
    requirements = models.TextField()


class JobResume(JobAd):
    resume_photo = models.ImageField(upload_to='static/img/resume/', blank=True)


# Vehicle


class VehicleBrand(models.Model):
    brand = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand}'


class VehicleModel(models.Model):
    brand = models.ForeignKey(VehicleBrand, on_delete=models.CASCADE, related_name='models')
    model = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand} {self.model}'


class VehicleCarcaseType(models.Model):
    carcase_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.carcase_type}'


class VehicleDriveUnit(models.Model):
    drive_unit = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.drive_unit}'


class VehicleMotorType(models.Model):
    motor_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.motor_type}'


class VehicleYear(models.Model):
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)],
                                       help_text="Use the following format: <YYYY>")

    def __str__(self):
        return f'{self.year}'


class VehicleAd(Ad):
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE, related_name='ads')
    carcase_type = models.ForeignKey(VehicleCarcaseType, on_delete=models.CASCADE)
    drive_unit = models.ForeignKey(VehicleDriveUnit, on_delete=models.CASCADE)
    motor_type = models.ForeignKey(VehicleMotorType, on_delete=models.CASCADE)
    year = models.ForeignKey(VehicleYear, on_delete=models.PROTECT)
    engine_volume = models.IntegerField()
    mileage = models.CharField(max_length=100)
    power = models.DecimalField(decimal_places=1, max_digits=5)
    rent = models.BooleanField(default=False)


# Property


class PropertyCategory(models.Model):
    title = models.CharField(max_length=100)


class PropertyRentalPeriod(models.Model):
    rental_period = models.CharField(max_length=15)


class PropertyPurpose(models.Model):
    property_purpose = models.CharField(max_length=30)


class PropertyAdd(models.Model):
    ad_id = models.ForeignKey(Ad, on_delete=models.CASCADE)
    category = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100)
    property_purpose = models.ForeignKey(PropertyPurpose, models.CASCADE)
    badrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    square = models.PositiveIntegerField()
    rental_period = models.ForeignKey(PropertyRentalPeriod, on_delete=models.CASCADE, blank=True)


# Market


class Sticker(models.Model):
    sticker = models.CharField(max_length=20)


class MarketCategory(models.Model):
    category = models.CharField(max_length=50)


class MarketAd(Ad):
    sticker = models.ForeignKey(Sticker, on_delete=models.PROTECT, related_name='ads')
    is_new = models.BooleanField(default=True)
    category = models.ForeignKey(MarketCategory, on_delete=models.CASCADE, related_name='ads')
    time_to_develop = models.CharField(max_length=50)


class MarketRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    market_ad = models.ForeignKey(MarketAd, on_delete=models.CASCADE, related_name='ratings')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


# Service


class ServiceCategory(models.Model):
    category = models.CharField(max_length=50)


class ServiceAd(Ad):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='ads')


# Useful resources


class UsefulResources(Ad):
    pass


# Entertainments


class EntertainmentType(models.Model):
    type = models.CharField(max_length=50)


class EntertainmentAd(Ad):
    type = models.ForeignKey(EntertainmentType, on_delete=models.PROTECT, related_name='entertainment_ads')
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)


class EntertainmentRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entertainment_ratings')
    entertainment_ad = models.ForeignKey(EntertainmentAd, on_delete=models.CASCADE,
                                         related_name='entertainment_ratings')
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])


# News


class News(models.Model):
    created_date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='static/img/news_photos')
    news_source = models.CharField(max_length=100)
    link = models.URLField(max_length=300)


class NewsCategory(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='categories')
    category = models.CharField(max_length=30)


# ABC

class ABCCategory(models.Model):
    category = models.CharField(max_length=50)


class ABC(Ad):
    category = models.ForeignKey(ABCCategory, on_delete=models.CASCADE, related_name='abcs')
