from flask_table import Table, Col

class Customer(Table):
    cNumber = Col('customerNumber')
    cName = Col('customerName')
    cPhone = Col('phone')
    cAddress = Col('addressLine1')
    cCity = Col('city')
    cCountry = Col('country')

    def __repr__(self):
        return "<Number: {}>".format(self.cNumber)