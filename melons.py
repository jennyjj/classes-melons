"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An over-arching melon class"""

    def __init__(self,
                 species,
                 qty,
                 shipped=False,
                 country_code='USA',
                 order_type="domestic",
                 tax=0.08):

        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = shipped
        self.order_type = order_type
        self.tax = tax

    def mark_shipped(self):
        """Marks the melon shipped."""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price = 7.50
        else:
            base_price = 5


        if self.order_type == "international" and self.qty < 10:
            total = ((1 + self.tax) * self.qty * base_price) + 3
        elif self.order_type == "government":
            total = self.qty * base_price
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize domestic melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize international melon order attributes."""

        super(InternationalMelonOrder, self).__init__(
            species, qty, tax=.17, order_type="international")
        
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government order"""


    def __init__(self, species, qty, passed_inspection=False):
        """Initialize domestic melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty, order_type="government")

        self.passed_inspection = passed_inspection

    def mark_inspection(self):
        """Marks the melon passed inspection."""
            
        self.passed_inspection = True

