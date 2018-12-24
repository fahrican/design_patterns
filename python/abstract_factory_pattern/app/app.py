from design_patterns.abstract_factory_pattern.factory import adidas_shoe_factory, nike_shoe_factory

if __name__ == '__main__':
    print('Type a number for brand of shoe')
    print('1) Adidas')
    print('2) Nike')
    print('Your choice: ', end='')
    brand_of_shoe = int(input())
    my_shoe = None
    if brand_of_shoe in range(1, 3):
        print('Enter the type of shoe')
        print('*) hiking')
        print('*) sport')
        print('Your choice: ', end='')
        type_of_shoe = input().lower()
        if brand_of_shoe == 1:
            adidas_factory = adidas_shoe_factory.AdidasShoeFactory()
            my_shoe = adidas_factory.create_shoe(type_of_shoe)
        else:
            nike_factory = nike_shoe_factory.NikeShoeFactory()
            my_shoe = nike_factory.create_shoe(type_of_shoe)
    else:
        assert 0, 'Type a valid number!'

    print('Your shoe: ' + my_shoe.get_shoe_name())
