# Define the Subject interface
class Subject:
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass

# Concrete Subject: Marketplace
class Marketplace(Subject):
    def __init__(self):
        self._observers = []
        self._products = {}

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def add_product(self, product, quantity):
        self._products[product] = quantity
        self.notify()

    def remove_product(self, product):
        if product in self._products:
            del self._products[product]
            self.notify()

    def update_quantity(self, product, quantity):
        if product in self._products:
            self._products[product] = quantity
            self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._products)

# Observer interface
class Observer:
    def update(self, products):
        pass

# Concrete Observer: Department of Purchasing (DPTO COMPRAS)
class PurchasingDepartment(Observer):
    def update(self, products):
        for product, quantity in products.items():
            if quantity < 100:
                print(f"DPTO COMPRAS: Refilling {product} in storage.")

# Concrete Observer: Marketing Department (DPTO MKT)
class MarketingDepartment(Observer):
    def update(self, products):
        # Marketing-related actions based on product updates
        pass

# Concrete Observer: Customer Service (SAC)
class CustomerService(Observer):
    def update(self, products):
        # Customer service actions based on product updates
        pass

# Simulation
if __name__ == "__main__":
    marketplace = Marketplace()
    purchasing = PurchasingDepartment()
    marketing = MarketingDepartment()
    customer_service = CustomerService()

    marketplace.attach(purchasing)
    marketplace.attach(marketing)
    marketplace.attach(customer_service)

    # Simulating updates in the marketplace
    marketplace.add_product("Shirt", 50)
    marketplace.add_product("Shoes", 20)

    marketplace.update_quantity("Shirt", 80)

    marketplace.remove_product("Shoes")
