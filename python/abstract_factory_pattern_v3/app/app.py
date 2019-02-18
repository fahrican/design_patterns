from python.abstract_factory_pattern_v3.factory.shoe_factory import ShoeFactory

if __name__ == '__main__':
    nike_shoe = ShoeFactory('nike')
    nike_sport = nike_shoe.get_sport_shoe()
    print(nike_sport.create_sport_shoe('Air Max'))
    adidas_shoe = ShoeFactory('adidas')
    adidas_hiking_shoe = adidas_shoe.get_hiking_shoe()
    print(adidas_hiking_shoe.create_hiking_shoe('XYZ'))
