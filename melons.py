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

        base_price = 5
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
