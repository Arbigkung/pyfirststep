def city_info(city, country, population=''):
    if population:
        info = city + ', ' + country + ' Pop: ' + str(population)
    else:
        info = city + ', ' + country
    
    return info
