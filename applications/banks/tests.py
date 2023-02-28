from django.core.exceptions import ValidationError
from django.test import TestCase

from applications.banks.models import Banks


class TestCaseBanks(TestCase):
    def setUp(self):
        try:
            self.bank = Banks.objects.create(name_bank="Bancolombia")
            self.bank.full_clean()
            self.bank.save()
        except (AttributeError, ValueError, TypeError):
            self.fail()

    def test_only_with_mandatory_fields(self):
        try:
            querybank = Banks.objects.create(name_bank="BBVA")
            querybank.full_clean()
            querybank.save()
        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(querybank, Banks)
            self.assertEqual(querybank.name_bank, "BBVA")

    def test_limint_max_length_in_name_bank(self):
        with self.assertRaises(ValidationError):
            _fake_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur condimentum aliquam arcu volutpat lobortis. Pellentesque sit amet lobortis elit, id sodales nulla. Nam id placerat sapien, et placerat metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
            entity_banking = Banks.objects.create(name_bank=_fake_name)
            entity_banking.full_clean()
