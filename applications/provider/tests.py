from django.core.exceptions import ValidationError
from django.test import TestCase

from applications.banks.models import Banks
from applications.provider.models import Provider


class TestCaseProviders(TestCase):
    def setUp(self):
        try:
            self.bank = Banks.objects.create(name_bank="Bancolombia")
            self.bank.full_clean()
            self.bank.save()
        except (AttributeError, ValueError, TypeError):
            self.fail()

    def test_only_with_mandatory_fields(self):

        try:
            query_provider = Provider.objects.create(
                name_provider="Katapult",
                nit_provider="901362343-4",
                name_contact_person="Carlos Velazquez",
                bank=self.bank,
            )
            query_provider.full_clean()
            query_provider.save()
        except ValidationError:
            self.fail()

        else:
            self.assertIsInstance(query_provider, Provider)
            self.assertIsInstance(query_provider.bank, Banks)
            self.assertEqual(query_provider.name_provider, "Katapult")
            self.assertEqual(query_provider.nit_provider, "901362343-4")
            self.assertEqual(query_provider.name_contact_person, "Carlos Velazquez")

    def test_incorrect_nit_pattern_provider(self):
        with self.assertRaises(ValidationError):
            query_provider = Provider.objects.create(
                name_provider="Katapult",
                nit_provider="9013623434",
                name_contact_person="Carlos Velazquez",
                bank=self.bank,
            )
            query_provider.full_clean()

    def test_with_all_fields_specified(self):
        try:
            provider = Provider.objects.create(
                name_provider="Katapult",
                nit_provider="901362343-4",
                name_contact_person="Carlos Velazquez",
                bank=self.bank,
                number_contact_person="3183848167",
                number_account_banking="002121583325",
                is_active=True,
            )
            provider.full_clean()
            provider.save()
        except ValidationError:
            self.fail()
        else:
            self.assertIsInstance(provider, Provider)
            self.assertIsInstance(provider.bank, Banks)
            self.assertEqual(provider.name_provider, "Katapult")
            self.assertEqual(provider.nit_provider, "901362343-4")
            self.assertEqual(provider.name_contact_person, "Carlos Velazquez")
            self.assertEqual(provider.number_contact_person, "3183848167")
            self.assertEqual(provider.number_account_banking, "002121583325")
            self.assertEqual(provider.is_active, True)

    def test_limint_max_length_in_nit(self):
        with self.assertRaises(ValidationError):
            _fake_nit = "901362343-4585"
            query_provider = Provider.objects.create(
                name_provider="Katapult",
                nit_provider=_fake_nit,
                name_contact_person="Carlos Velazquez",
                bank=self.bank,
            )
            query_provider.full_clean()

    def test_limint_max_length_in_contact_and_account(self):
        """
        number_contact_person
        number_account_banking
        """
        with self.assertRaises(ValidationError):
            _fake_max_length = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur condimentum aliquam arcu volutpat lobortis. Pellentesque sit amet lobortis elit, id sodales nulla. Nam id placerat sapien, et placerat metus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus."
            query_provider = Provider.objects.create(
                name_provider="Katapult",
                nit_provider="901362343-4",
                name_contact_person="Carlos Velazquez",
                bank=self.bank,
                number_contact_person=_fake_max_length,
                number_account_banking=_fake_max_length,
            )
            query_provider.full_clean()
