from django.db import models

from django.utils.translation import gettext_lazy as _


class BusinessEntitiesModel(models.Model):
    class BusinessEntitiesEnum(models.TextChoices):
        TOV = "TOV", _("TOV")
        FOP = "FOP", _("FOP")

    class GenderEnum(models.TextChoices):
        MALE = "M", _("який")
        FEMALE = "F", _("яка")

    business_entity = models.CharField(
        max_length=3,
        choices=BusinessEntitiesEnum.choices,
        default=BusinessEntitiesEnum.FOP
    )
    code_edrpou = models.CharField(_("Code EDRPOU"), max_length=10, blank=True, unique=True, null=True)
    fop_name = models.CharField(_("FOP Name"), max_length=200, blank=True, null=True)
    tov_name = models.CharField(_("TOV Name"), max_length=200, blank=True, null=True)
    full_tov_name = models.CharField(_("Full TOV Name"), max_length=200, blank=True, null=True)
    director_name = models.CharField(_("Name of Director"), max_length=200, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=200, blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone = models.CharField(_("Phone"), max_length=200, blank=True, null=True)
    gender = models.CharField(_("Gender"), max_length=5, choices=GenderEnum.choices, default=GenderEnum.MALE)
    iban = models.CharField(_("IBAN"), max_length=200, blank=True, null=True)
    bank_name = models.CharField(_("Bank Name"), max_length=200, blank=True, null=True)
    mfo = models.CharField(_("MFO"), blank=True, null=True)

    vehicles = models.ManyToManyField(
        'VehicleModel',
        verbose_name=_("Vehicles"),
        blank=True,
        related_name='business_entities'
    )
    contract = models.ManyToManyField(
        'ContractModel',
        verbose_name=_("Contract Documents"),
        blank=True,
        related_name='business_entities'
    )


class VehicleModel(models.Model):
    number = models.CharField(_("Vehicle Number"), max_length=200, blank=True, null=True)
    brand = models.CharField(_("Brand"), max_length=200, blank=True, null=True)
    model = models.CharField(_("Model"), max_length=200, blank=True, null=True)
    year = models.CharField(_("Year"), blank=True, null=True)


class ContractModel(models.Model):

    class ContractEnum(models.TextChoices):
        ATP = "ATP", _("ATP")
        OFFICE = "OFFICE", _("OFFICE")

    contract_choice = models.CharField(_("Contract Choice"), choices=ContractEnum.choices, default=ContractEnum.ATP)
    start_date = models.DateField(_("Start Date"), blank=True, null=True)
    end_date = models.DateField(_("End Date"), blank=True, null=True)
    customer_code_edrpou = models.CharField(_("Code EDRPOU"), blank=True, null=True)
