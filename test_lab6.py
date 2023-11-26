"""import datetime & pytest"""
import datetime
import pytest

from lab6 import Medicine
from lab6 import Pharmacy

@pytest.fixture(name='med_fixture')
def medicine():
    """
    This function if for reduce and simplify usage of Pharmacy class
    """
    med1 = Medicine(109, 10, 'paracetamol', True, datetime.date(2021, 6, 10))
    med2 = Medicine(567, 10, 'paralen', True, datetime.date(2024, 6, 10))
    med3 = Medicine(10, 10, 'ibuprofen', True, datetime.date(2025, 6, 10))
    med4 = Medicine(1090, 10, 'amol', False, datetime.date(2020, 6, 10))
    pharmacy = Pharmacy()
    pharmacy.add_medicine(med1)
    pharmacy.add_medicine(med2)
    pharmacy.add_medicine(med3)
    pharmacy.add_medicine(med4)
    yield pharmacy

def test_is_medicine_expired():
    """
    This function tests if medicine date isn\'t expired
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    assert med.is_expired() is False

def test_get_medicine_price():
    """
    This function tests if medicine price is corrctly initialized
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    assert med.get_price() == 109

def test_set_medicine_price():
    """
    This function tests if setted value of the price is correct
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    med.set_price(234234)
    assert med.get_price() == 234234

def test_get_medicine_name():
    """
    This function tests if medicine name is correctly initialized
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    assert med.get_name() == 'paracetamol'

def test_get_medicine_expiration_date():
    """
    This function tests if medicine expiration date corectly initialized
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    assert med.get_expiration_date() == datetime.date(2024, 6, 10)

def test_get_medicine_quantity():
    """
    This function tests if medicine quantity is correctly initialized
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    assert med.get_quantity() == 10

def test_get_medicine_if_prescription():
    """
    This function tests if medicine if prescription needed is correctly initialized
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    assert med.get_if_prescription() == 'Yes'

def test_pharmacy_add_medicine():
    """
    This function tests the add method  
    """
    med = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    pharmacy = Pharmacy()
    pharmacy.add_medicine(med)
    assert len(pharmacy.get_medicine()) == 1

def test_pharmacy_get_medicine(med_fixture):
    """
    This function tests the get of medicine list
    """
    assert len(med_fixture.get_medicine()) == 4

def test_pharmacy_del_medicine(med_fixture):
    """
    This function tests the delete medicine method 
    """
    med_fixture.del_medicine('paracetamol')
    assert len(med_fixture.get_medicine()) == 3

def test_pharmacy_get_medicine_lowest_price(med_fixture):
    """
    This function tests the getting og the list from lowest to highest price 
    """
    lowest = med_fixture.get_medicine_lowest_price()
    assert lowest[0].get_price() == 10

def test_pharmacy_set_discount(med_fixture):
    """
    This function tests setting of the discount 
    """
    med_fixture.set_discount(10)
    disc = med_fixture.get_medicine()
    assert disc[0].get_price() == 98.1

def test_pharmacy_del_discount(med_fixture):
    """
    This function tests delete of the discount 
    """
    med_fixture.set_discount(10)
    med_fixture.del_discount(10)
    disc = med_fixture.get_medicine()
    assert disc[0].get_price() == 109

def test_pharmacy_del_expired_medicine(med_fixture):
    """
    This function tests delete of the expired medicine
    """
    med_fixture.del_expired_medicine()
    assert len(med_fixture.get_medicine()) == 2
