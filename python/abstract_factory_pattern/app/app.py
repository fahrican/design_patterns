from python.abstract_factory_pattern.brand.adidas_hiking_boot import AdidasHikingBoot
from python.abstract_factory_pattern.brand.adidas_sport_shoe import AdidasSportShoe
from python.abstract_factory_pattern.factory.adidas_shoe_factory import AdidasShoeFactory
from python.abstract_factory_pattern.factory.nike_shoe_factory import NikeShoeFactory


def main():
    for factory in (AdidasShoeFactory(), NikeShoeFactory()):
        hiking_boot = factory.create_hiking_boot()
        sport_shoe = factory.create_sport_shoe()
        hiking_boot.create_adidas_shoe()
        sport_shoe.create_nike_shoe()


if __name__ == '__main__':
    # print('Type a number for brand of shoe')
    # print('1) Adidas')
    # print('2) Nike')
    # print('Your choice: ', end='')
    # brand_of_shoe = int(input())
    # my_shoe = None
    # if brand_of_shoe in range(1, 3):
    #     print('Enter the type of shoe')
    #     print('*) hiking')
    #     print('*) sport')
    #     print('Your choice: ', end='')
    #     type_of_shoe = input().lower()
    #     if brand_of_shoe == 1:
    #         adidas_factory = AdidasShoeFactory()
    #         my_shoe = adidas_factory.create_shoe(type_of_shoe)
    #     else:
    #         nike_factory = NikeShoeFactory()
    #         my_shoe = nike_factory.create_shoe(type_of_shoe)
    # else:
    #     assert 0, 'Type a valid number!'
    #
    # print('Your shoe: ' + my_shoe.get_shoe_name())
    main()
