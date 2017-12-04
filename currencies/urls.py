from django.conf.urls import url
from . import views

app_name = "currency"
urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="base"),
    url(r"^(?P<currency_code>[a-z]{3})/$", views.CurrencyDetailView.as_view(), name="detail"),
]