from fastapi import APIRouter
from hotel.db.db_interface import DBInterface
from hotel.db.models import DBCustomer
from hotel.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    create_customer,
    delete_customer,
    get_all_customers,
    get_customer,
    update_customer,
)

router = APIRouter()


@router.get("/customers")
def api_get_all_customers():
    customer_interface = DBInterface(db_class=DBCustomer)
    return get_all_customers(customer_interface)


@router.get("/customer/{customer_id}")
def api_get_room(customer_id: int):
    customer_interface = DBInterface(db_class=DBCustomer)
    return get_customer(customer_id, customer_interface)


@router.post("/customer")
def api_create_customer(customer: CustomerCreateData):
    customer_interface = DBInterface(db_class=DBCustomer)
    return create_customer(customer, customer_interface)


@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    customer_interface = DBInterface(db_class=DBCustomer)
    return update_customer(customer_id, customer, customer_interface)


@router.delete("/customer/{customer_id}")
def api_delete_customer(customer_id: int):
    customer_interface = DBInterface(db_class=DBCustomer)
    return delete_customer(customer_id, customer_interface)
