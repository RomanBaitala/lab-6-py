"""
datatime import
"""
import datetime


class Medicine:
    """
    class medicine
    """

    def __init__(self, price=0, quantity=0, name='', is_prescription_needed=True,
                expiration_date=datetime.date.today()):
        """
        Class constructor
        :param price: price of medicine (float)
        :param quantity: number of medicine that we have (int)
        :param name: medicine name (str)
        :param is_prescription_needed:  (boolean)
        :param expiration_date: when medicine expires (datetime)
        """
        self._price = price
        self._quantity = quantity
        self._name = name
        self._expiration_date = expiration_date
        self._is_prescription_needed = is_prescription_needed

    def is_expired(self):
        """
        The func is checking if medicine is expired
        :return: boolean
        """
        today_day = datetime.date.today()
        return self._expiration_date < today_day

    def get_price(self):
        """
        The func returns price
        :return:
        """
        return self._price

    def set_price(self, new_price):
        """
        The func sets new value for price
        :param new_price: new value for price
        :return:
        """
        self._price = new_price
        return 'Your new prise was set'

    def get_name(self):
        """
        The func returns medicine name
        :return:
        """
        return self._name

    def get_expiration_date(self):
        """
        The func returns medicine expiration date
        :return:
        """
        return self._expiration_date

    def get_quantity(self):
        """
        The func returns medicine quantity
        :return:
        """
        return self._quantity

    def get_if_prescription(self):
        """
        The func returns if prescription needed
        :return:
        """
        if self._is_prescription_needed:
            return "Yes"
        return "No"

    def __str__(self):
        """
        The func returns object in str format
        :return:
        """
        return (f"| Name = {self.get_name()} | Price = {self.get_price()} | "
                f"Expiration date = {self.get_expiration_date()} | "
                f"Quantity = {self.get_quantity()} | Prescription = {self.get_if_prescription()} |")


class Pharmacy:
    """
    class pharmacy
    """

    def __init__(self):
        """
        Class constructor
        """
        self.medicines = []

    def add_medicine(self, medicine):
        """
        The func adds medicine to medicine list
        :param medicine: medicine object
        :return:
        """
        self.medicines.append(medicine)
        return print(f"The medicine \"{medicine.get_name()}\" was successfully added")

    def get_medicine(self):
        """
        The func returns all medicines in str format
        :return:
        """
        for med in self.medicines:
            print('=================================================')
            print(med)
            print('=================================================')
        return 'String list of medicine'

    def del_medicine(self, name):
        """
        Func for medicine delete
        :param name: name of medicine to delete
        :return:
        """
        for i in self.medicines:
            if name == i.get_name():
                self.medicines.remove(i)
        return f"The medicine {name} was successfully deleted!"

    def get_medicine_lowes_price(self):
        """
        The func returns list of medicine from lowes price to highest
        :return:
        """
        sorted_list = sorted(self.medicines, key=lambda medicine: medicine.get_price())

        if len(self.medicines) == len(sorted_list):
            for el in sorted_list:
                print('=================================================')
                print(el)
                print('=================================================')
            return 'Cheapest med list'
        return 'Something went wrong'

    def set_discount(self, discount):
        """
        The func for setting discount
        :param discount: discount value
        :return:
        """
        for med in self.medicines:
            med.set_price(med.get_price() - med.get_price() * discount / 100)
            print('=================================================')
            print(med)
            print('=================================================')
        return "discount was set"

    def del_discount(self, old_discount):
        """
        The func for removing discount
        :param old_discount: the value of old discount
        :return:
        """
        for med in self.medicines:
            med.set_price(med.get_price() + med.get_price() / 90 * old_discount)
            print('=================================================')
            print(med)
            print('=================================================')
        return "Discount was canceled"

    def del_expired_medicine(self):
        """
        The func deletes medicines which has expired
        :return:
        """
        for med in self.medicines:
            if med.expiration_date():
                self.medicines.remove(med)


if __name__ == "__main__":
    paracetamol = Medicine(109, 10, 'paracetamol', True, datetime.date(2024, 6, 10))
    ibuprofen = Medicine(50, 100, 'ibuprofen', False, datetime.date(2024, 6, 11))
    inulin = Medicine(70, 100, 'inulin', False, datetime.date(2022, 6, 11))
    inulin1 = Medicine(4545, 100, 'inulin', False, datetime.date(2022, 6, 11))
    inulin2 = Medicine(745, 100, 'inulin', False, datetime.date(2022, 6, 11))
    inulin3 = Medicine(750, 100, 'inulin', False, datetime.date(2022, 6, 11))
    inulin4 = Medicine(740, 100, 'inulin', False, datetime.date(2022, 6, 11))

    pharmacy = Pharmacy()
    pharmacy.add_medicine(paracetamol)
    pharmacy.add_medicine(ibuprofen)
    pharmacy.add_medicine(inulin)
    pharmacy.add_medicine(inulin1)
    pharmacy.add_medicine(inulin2)
    pharmacy.add_medicine(inulin3)
    pharmacy.add_medicine(inulin4)

    pharmacy.del_medicine('ibuprofen')

    print(pharmacy.set_discount(10))
    print(pharmacy.del_discount(10))

    print(pharmacy.get_medicine())

    print(pharmacy.get_medicine_lowes_price())
