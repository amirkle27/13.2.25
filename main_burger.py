from crispy_chicken_burger_builder import CrispyChickenBurgerBuilder
from beyond_burger_builder import BeyondBurgerBuilder
from specialty_of_the_house_burger_builder import SpecialtyOfTheHouseBurgerBuilder


from burger import Burger
from crispy_chicken_burger_builder import CrispyChickenBurgerBuilder

if __name__ == "__main__":



    crispy_chicken_burger: Burger = CrispyChickenBurgerBuilder().build_burger(
        graving_type="Honey Mustard", side_dish = "French Fries").get_burger()

    beyond_burger:Burger = BeyondBurgerBuilder().build_burger(
        graving_type="Thousand Islands Sauce, Extra Spycy", side_dish="Caesar Salad").get_burger()

    specialty_of_the_house_burger: Burger = SpecialtyOfTheHouseBurgerBuilder().build_burger(
        side_dish="Fried Tofu").get_burger()


    print(crispy_chicken_burger)
    print()
    print(beyond_burger)
    print()
    print(specialty_of_the_house_burger)



