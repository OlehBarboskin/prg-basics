class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self,distance):
        self.calculate_fare(distance)
        print (f'{self.fare}')


def main():
    # your program
   uber = TaxiRide(2)
   uber.print_receipt(5)

if __name__ == "__main__":
    main()
