from  burger import Burger
from abc import abstractmethod, ABC
from typing import final


class BurgerBuilder(ABC):
    def __init__(self,burger_name):
        self.__burger: Burger = None
        self.burger_name = burger_name

    def get_burger(self):
        return self.__burger

    @final
    def build_burger(self, **kwargs):
        self.__burger = Burger(burger_name=self.burger_name)  # 1
        self.prepare_bun()
        self.prepare_vegg()  # 2
        self.prepare_main()  # 3
        self.prepare_graving(**kwargs)  # 4
        self.prepare_side_dish(**kwargs)
        self.prepare_package()
        self.prepare_price()
        return self

    @abstractmethod
    def prepare_bun(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_vegg(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_main(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_graving(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def prepare_side_dish(self,**kwargs):
        raise NotImplementedError

    @abstractmethod
    def prepare_package(self):
        raise NotImplementedError

    @abstractmethod
    def prepare_price(self):
        raise NotImplementedError
