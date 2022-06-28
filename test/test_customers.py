import unittest

from hotel.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    create_customer,
    update_customer,
)
from hotel.operations.interface import DataObject
from test.stub import DataInterfaceStub


class CustomerInterface(DataInterfaceStub):
    def create(self, data: DataObject) -> DataObject:
        data["id"] = 1
        return data

    def update(self, id: int, data: DataObject) -> DataObject:
        customer = {
            "id": id,
            "first_name": "Bill",
            "last_name": "Gates",
            "email_address": "bill@gates.com",
        }

        customer.update(data)

        return customer


class TestCustomers(unittest.TestCase):
    def test_create_customer(self):
        customer_data = CustomerCreateData(
            first_name="John", last_name="McAfee", email_address="john@mcafee.gov"
        )

        expected = customer_data.dict()
        expected["id"] = 1

        customer = create_customer(
            data=customer_data, customer_interface=CustomerInterface()
        )

        self.assertEqual(customer, expected)

    def test_update_customer_all_attributes(self):
        customer_data = CustomerUpdateData(
            first_name="John", last_name="McAfee", email_address="john@mcafee.gov"
        )

        expected = customer_data.dict()
        expected["id"] = 1

        customer = update_customer(
            customer_id=1, data=customer_data, customer_interface=CustomerInterface()
        )

        self.assertEqual(customer, expected)

    def test_update_customer_one_attribute(self):
        customer_data = CustomerUpdateData(first_name="John")

        expected = customer_data.dict()
        expected["id"] = 1
        expected["last_name"] = "Gates"
        expected["email_address"] = "bill@gates.com"

        customer = update_customer(
            customer_id=1, data=customer_data, customer_interface=CustomerInterface()
        )

        self.assertEqual(customer, expected)
