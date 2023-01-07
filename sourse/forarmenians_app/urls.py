from django.urls import path
from forarmenians_app.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('abc/', ABCView.as_view(), name='abc'),
    path('abs/detail/', ABSDetailView.as_view(), name='abs-detail'),
    path('cafe/', CafeView.as_view(), name='cafe'),
    path('cafe/detail/', CafeDetailView.as_view(), name='cafe-detail'),
    path('entertainments/', EntertainmentsView.as_view(), name='entertainments'),
    path('entertainments/detail/', EntertainmentsDetailView.as_view(), name='entertainments-detail'),
    path('events/', EventsView.as_view(), name='events'),
    path('events/detail/', EventsDetailView.as_view(), name='events-detail'),
    path('job/', JobView.as_view(), name='job'),
    path('job-catalog/vacancy/', JobCatalogVacancyView.as_view(), name='job-catalog-vacancy'),
    path('job-catalog/resume/', JobCatalogResumeView.as_view(), name='job-catalog'),
    path('job/vacancy/<int:pk>/', JobCatalogVacancyDetailView.as_view(), name='job-detail-vacancy'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job-detail'),

    path('market/', MarketView.as_view(), name='market'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/detail/', NewsDetailView.as_view(), name='news-detail'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile-ads/', ProfileADCView.as_view(), name='profile-ads'),
    path('profile-wallet/', ProfileWalletView.as_view(), name='profile-wallet'),
    path('property/', PropertyView.as_view(), name='property'),
    path('property-catalog/', PropertyCatalogView.as_view(), name='property-catalog'),
    path('property/detail/', PropertyDetailView.as_view(), name='property-detail'),
    path('services', ServicesView.as_view(), name='services'),
    path('services/detail/', ServiceDetailView.as_view(), name='services-detail'),
    path('useful', UsefulView.as_view(), name='useful'),
    path('useful/detail/', UsefulDetailView.as_view(), name='useful-detail'),
    path('choose-categories/', ChooceCategoriesView.as_view(), name='choose-categories'),
    path('vehicle/', VehicleView.as_view(), name='vehicle'),
    path('vehicle-catalog/', VehicleCatalogView.as_view(), name='vehicle-catalog'),
    path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('vehicle/create/', VehicleCreateView.as_view(), name='vehicle-create')
]

