from fastapi import APIRouter
from hotel.operations.customers import (
    CustomerCreateData,
    CustomerUpdateData,
    create_customer,
    get_all_customers,
    get_customer,
    update_customer,
)

router = APIRouter()


@router.get("/customers")
def api_get_all_customers():
    return get_all_customers()


@router.get("/customer/{customer_id}")
def api_get_room(customer_id: int):
    return get_customer(customer_id)


@router.post("/customer")
def api_create_customer(customer: CustomerCreateData):
    return create_customer(customer)


@router.post("/customer/{customer_id}")
def api_update_customer(customer_id: int, customer: CustomerUpdateData):
    return update_customer(customer_id, customer)
