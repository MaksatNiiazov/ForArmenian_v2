from django.views.generic import TemplateView, ListView, DetailView, CreateView
from forarmenians_app.forms import *
from forarmenians_app.models import *


class MainPageView(TemplateView):
    template_name = "mainPage/index.html"


# ABC


class ABCView(TemplateView):
    template_name = "abc/abc.html"


class ABSDetailView(TemplateView):
    template_name = "abc/abc-single.html"


# Café


class CafeView(TemplateView):
    template_name = "cafe/cafe.html"


class CafeDetailView(TemplateView):
    template_name = "cafe/cafe-single.html"


# Entertainments


class EntertainmentsView(ListView):
    model = EntertainmentAd
    template_name = "entertainments/entertainments.html"


class EntertainmentsDetailView(DetailView):
    model = EntertainmentAd
    template_name = "entertainments/entertainments-single.html"


# Events


class EventsView(TemplateView):
    template_name = "events/events.html"


class EventsDetailView(TemplateView):
    template_name = "events/events-single.html"


# Job


class JobView(TemplateView):
    template_name = "job/job.html"


class JobCatalogResumeView(ListView):
    model = JobResume
    template_name = "job/job-catalog-resume.html"


class JobResumeDetailView(DetailView):
    model = JobResume
    template_name = "job/job-single-resume.html"


class JobCatalogVacancyView(ListView):
    model = JobVacancy
    template_name = "job/job-catalog-vacancy.html"


class JobVacancyDetailView(DetailView):
    model = JobVacancy
    template_name = "job/job-single-vacancy.html"


class JobVacancyCreateView(CreateView):
    model = JobVacancy
    form_class = JobVacancyForm
    template_name = 'job/submit-job.html'


# Market


class MarketView(TemplateView):
    template_name = "market/market.html"


# News


class NewsView(ListView):
    model = News
    template_name = "news/news.html"


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news-single.html"


# Profile


class ProfileView(TemplateView):
    template_name = "profile/profile.html"


class ProfileADCView(TemplateView):
    template_name = "profile/profile-ads.html"


class ProfileWalletView(TemplateView):
    template_name = "profile/profile-wallet.html"


# Property


class PropertyView(TemplateView):
    template_name = "property/property.html"


class PropertyCatalogView(TemplateView):
    template_name = "property/property-catalog.html"


class PropertyDetailView(TemplateView):
    template_name = "property/property-single.html"


# Service


class ServicesView(TemplateView):
    template_name = "services/services.html"


class ServiceDetailView(TemplateView):
    template_name = "services/services-single.html"


class UsefulView(TemplateView):
    template_name = "useful/useful.html"


class UsefulDetailView(TemplateView):
    template_name = "useful/useful-single.html"


# Vehicle


class ChooceCategoriesView(TemplateView):
    template_name = "vehicle/choose-categories.html"


class VehicleView(TemplateView):
    template_name = "vehicle/vehicle.html"


class VehicleCatalogView(ListView):
    model = VehicleAd
    queryset = VehicleAd.objects.filter(rent=False)
    template_name = "vehicle/vehicle-catalog.html"


class VehicleCatalogRentView(ListView):

    model = VehicleAd
    queryset = VehicleAd.objects.filter(rent=True)
    template_name = "vehicle/vehicle-catalog.html"


class VehicleDetailView(DetailView):
    model = VehicleAd
    template_name = "vehicle/vehicle-single.html"


class VehicleCreateView(CreateView):
    form_class = VehicleForm
    template_name = "vehicle/submit-auto.html"

