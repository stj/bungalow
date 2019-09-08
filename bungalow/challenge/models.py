from django.db import models
from django.utils.translation import gettext_lazy as _


class Property(models.Model):
    """
    Model for properties rented out.

    For time saving no DB normalization has been done, no indexes are defined,
    nor are any details about who and when a record was created and changed.

    Model uses Django's implicit AutoField, consider an explicit UUID field.
    """
    HOME_TYPES = (
        ("Apartment", _("Apartment")),
        ("Condominium", _("Condominium")),
        ("Duplex", _("Duplex")),
        ("Miscellaneous", _("Miscellaneous")),
        ("MultiFamily2To4", _("MultiFamily2To4")),
        ("SingleFamily", _("SingleFamily")),
        ("VacantResidentialLand", _("VacantResidentialLand")),
    )

    area_unit = models.CharField(_("area unit"), max_length=4)
    bathrooms = models.FloatField(_("bathrooms"), null=True, blank=True)
    bedrooms = models.PositiveSmallIntegerField(_("bedrooms"))
    home_size = models.PositiveIntegerField(_("home size"), null=True, blank=True)
    home_type = models.CharField(_("home type"), choices=HOME_TYPES, max_length=25)
    last_sold_date = models.DateField(_("last_sold_date"), null=True, blank=True)
    last_sold_price = models.PositiveIntegerField(_("last_sold_price"), null=True, blank=True)
    link = models.CharField(_("link"), max_length=512)
    price = models.CharField(_("price"), max_length=10)
    property_size = models.PositiveSmallIntegerField(_("property size"), null=True, blank=True)
    rent_price = models.PositiveSmallIntegerField(_("rent price"), null=True, blank=True)
    rentzestimate_amount = models.PositiveSmallIntegerField(_("rent estimate amount"), null=True, blank=True)
    rentzestimate_last_updated = models.DateField(_("rent estimate last updated"), null=True, blank=True)
    tax_value = models.FloatField(_("tax value"))
    tax_year = models.PositiveSmallIntegerField(_("tax year"))
    year_built = models.PositiveSmallIntegerField(_("year built"), null=True, blank=True)
    zestimate_amount = models.PositiveIntegerField(_("estimate amount"), null=True, blank=True)
    zestimate_last_updated = models.DateField(_("rent estimate last updated"))
    zillow_id = models.PositiveIntegerField(_("zillow id"))
    address = models.CharField(_("address"), max_length=1024)
    city = models.CharField(_("city"), max_length=1024)
    state = models.CharField(_("state"), max_length=512)
    zipcode = models.CharField(_("ZIP / Postal code"), max_length=12)
