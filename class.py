class Groundtransport(object): #Наземный транспорт name гусеничный транспорт
    def __init__(self, name, caterpillartransport):
        self.name = name
        self.caterpillartransport = caterpillartransport

class AirCushionTransport(object): #транспорт на воздушной подушке
    def __init__(self, air):
        self.air = air

Aircushion = AirCushionTransport('Машина на воздушной подушке - SR-N1')
car = Groundtransport('Машина на  гусеницах - Renault 12\n', Aircushion)

print("{}{}".format(car.name, car.caterpillartransport.air))

# Как-то так ?
# Или я все усложнил
# Надо было просто создать калссы с названиями?