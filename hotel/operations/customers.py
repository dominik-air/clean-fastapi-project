from pydantic import BaseModel

from hotel.operations.interface import DataInterface, DataObject


class CustomerCreateData(BaseModel):
    first_name: str
    last_name: str
    email_address: str


class CustomerUpdateData(BaseModel):
    first_name: str | None
    last_name: str | None
    email_address: str | None


def get_all_customers(customer_interface: DataInterface) -> list[DataObject]:
    return customer_interface.get_all()


def get_customer(customer_id: int, customer_interface: DataInterface) -> DataObject:
    return customer_interface.get_by_id(customer_id)


def create_customer(
    data: CustomerCreateData, customer_interface: DataInterface
) -> DataObject:
    return customer_interface.create(data)


def update_customer(
    customer_id: int, data: CustomerUpdateData, customer_interface: DataInterface
) -> DataObject:
    return customer_interface.update(customer_id, data)


def delete_customer(customer_id: int, customer_interface: DataInterface) -> DataObject:
    return customer_interface.delete(customer_id)
