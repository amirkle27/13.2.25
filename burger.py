class Burger:
    def __init__(self,burger_name):
        self.order = []
        self.burger_name = burger_name

    def prepare_bun(self, bun):
        self.order.append(bun)

    def prepare_vegg(self, vegg):
        self.order.append(vegg)

    def prepare_main(self, main):
        self.order.append(main)

    def prepare_graving(self, graving):
        self.order.append(graving)

    def prepare_side_dish(self,side_dish):
        self.order.append(side_dish)

    def prepare_package(self,package):
        self.order.append(package)

    def prepare_price(self, price):
        self.order.append(price)

    def __str__(self):
        return f"{self.burger_name}:\nBurger Order: " + ", ".join(self.order)


# return f"{BurgerBuilder.get_burger(BurgerBuilder()):\n}Burger Order: " + ", ".join(self.order)