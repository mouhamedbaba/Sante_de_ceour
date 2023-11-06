from django.db import models

class NotificationPayTech(models.Model):
    TYPE_EVENT_CHOICES = [
        ('sale_complete', 'Paiement réussi'),
        ('sale_canceled', 'Annulation de paiement'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('Carte Bancaire', 'Carte Bancaire'),
        ('PayPal', 'PayPal'),
        ('Orange Money', 'Orange Money'),
        ('Joni Joni', 'Joni Joni'),
        ('Wari', 'Wari'),
        ('Poste Cash', 'Poste Cash'),
    ]
    CURRENCY_CHOICES = [
        ('XOF', 'XOF'),
        ('EUR', 'EUR'),
        ('USD', 'USD'),
        ('CAD', 'CAD'),
        ('GBP', 'GBP'),
        ('MAD', 'MAD'),
    ]
    ENV_CHOICES = [
        ('test', 'Test'),
        ('prod', 'Production'),
    ]

    type_event = models.CharField(max_length=20)
    client_phone = models.CharField(max_length=20, null = True , blank=True)
    payment_method = models.CharField(max_length=20, null = True , blank=True)
    item_name = models.CharField(max_length=255)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    ref_command = models.CharField(max_length=255)
    command_name = models.CharField(max_length=255)
    currency = models.CharField(max_length=3, null = True , blank=True)
    env = models.CharField(max_length=10)
    custom_field = models.TextField( null = True , blank=True)
    token = models.CharField(max_length=100)

    def __str__(self):
        return f"Notification PayTech - Référence de commande : {self.ref_command}"
