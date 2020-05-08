"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        # self.order_type = order_type
        # self.tax = 0

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5

        if self.species == "christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = 'domestic'




class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = 'international'


    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):

        if self.qty < 10:
            total_with_fee = super().get_total() + 3
            return total_with_fee
            
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Government melon order. Non-taxed"""

    order_type = 'government'
    tax = 0.0

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
