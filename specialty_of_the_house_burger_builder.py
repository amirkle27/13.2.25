from typing import override

from burger_builder import BurgerBuilder

class SpecialtyOfTheHouseBurgerBuilder(BurgerBuilder):
    def __init__(self):
        super().__init__("Specialty of the House Burger")
    @override
    def prepare_bun(self):
        self.get_burger().prepare_bun("Brioche Bun")

    @override
    def prepare_vegg(self):
        self.get_burger().prepare_vegg("Tomatoes, Pickles, Lettuce, Onion, Truffles, Fruits of the season, Olives, Macadamia nuts")

    @override
    def prepare_main(self):
        self.get_burger().prepare_bun("Our special 500 Extra-tender 30-30-30 Veal-Fish-Goat Specialty of the House Super delicious burger")

    @override
    def prepare_graving(self, **kwargs):
        self.get_burger().prepare_graving(f"{kwargs.get("graving_type", "No Gravy")}")

    @override
    def prepare_side_dish(self, **kwargs):
        self.get_burger().prepare_side_dish(f"{kwargs.get("side_dish", "No Side Dish")}")

    @override
    def prepare_package(self):
        self.get_burger().prepare_package("Colourful Cheerful Paper Box")

    @override
    def prepare_price(self):
        self.get_burger().prepare_price("199.99")




