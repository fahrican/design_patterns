from design_patterns.decorater_pattern.model.audi import Audi
from design_patterns.decorater_pattern.model.radio import Radio
from design_patterns.decorater_pattern.model.leather_seats import LeatherSeats

if __name__ == '__main__':
    my_audi = Audi()
    my_audi = LeatherSeats(my_audi)
    my_audi = Radio(my_audi)
    print(my_audi.get_equipment())
    print(my_audi.get_price())
