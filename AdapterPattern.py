class EuropeanTemperature:

    def __init__(self, celsius):
        self.celsius = celsius

    def get_celsius(self):
        return self.celsius

    def __str__(self):
        return f"{self.celsius} °C"

class AmericanTemperature:

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def get_fahrenheit(self):
        return self.fahrenheit

    def __str__(self):
        return f"{self.fahrenheit} °F"

class TemperatureAdapter:

    def __init__(self, euro_temp, us_temp):
        self.euro_temp = euro_temp
        self.us_temp = us_temp

    def difference_celsius(self):
        us_c = (self.us_temp.get_fahrenheit() - 32) / 1.8
        return self.euro_temp.get_celsius() - us_c

    def difference_fahrenheit(self):
        euro_f = self.euro_temp.get_celsius() * 1.8 + 32
        return euro_f - self.us_temp.get_fahrenheit()

Dnipro=EuropeanTemperature(12)
Milan=EuropeanTemperature(18)

Michigan=AmericanTemperature(41)
Miami=AmericanTemperature(77)


print("Dnipro - ",Dnipro)
print("Michigan - ",Michigan)
temperature_difference=TemperatureAdapter(Dnipro, Michigan)
print("\tРізниця у °C: ",temperature_difference.difference_celsius())
print("\tРізниця у °F: ",temperature_difference.difference_fahrenheit())

print("Milan - ",Milan)
print("Miami - ",Miami)
temperature_difference=TemperatureAdapter(Milan, Miami)
print("\tРізниця у °C: ",temperature_difference.difference_celsius())
print("\tРізниця у °F: ",temperature_difference.difference_fahrenheit())


