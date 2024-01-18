class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0
        self.total_amount = 0
        self.gift_wrap = False

class Cart:
    def __init__(self):
        self.products = [
            Product("Product A", 20),
            Product("Product B", 40),
            Product("Product C", 50)
        ]
        self.subtotal = 0
        self.discount_amount = 0
        self.shipping_fee = 0
        self.gift_wrap_fee = 0
        self.total = 0

    def discount_rules(self):
        total_quantity = sum(p.quantity for p in self.products)
        cart_total = sum(p.total_amount for p in self.products)

        if cart_total > 200:
            self.discount_amount = min(self.discount_amount + 10, cart_total)

        for product in self.products:
            if product.quantity > 10:
                product_discount = 0.05 * product.total_amount
                self.discount_amount = max(self.discount_amount, product_discount)

        if total_quantity > 20:
            self.discount_amount = max(self.discount_amount, 0.1 * cart_total)

        if total_quantity > 30 and (p.quantity > 15 for p in self.products):
            tiered_discount = sum((p.quantity - 15) * p.price * 0.5 for p in self.products if p.quantity > 15)
            self.discount_amount = max(self.discount_amount, tiered_discount)

    def calc_fees(self):
        total_quantity = sum(p.quantity for p in self.products)

        print(f"Total quantity : {total_quantity}")
        self.gift_wrap_fee = sum(p.quantity for p in self.products if p.gift_wrap)
        self.shipping_fee = (total_quantity // 10) * 5

    def generate_invoice(self):
        print("\n\t------Invoice------")
        for p in self.products:
            print(f"\n\t{p.name} : Quantity : {p.quantity} = ${p.total_amount}")

        print(f"\n\tSubtotal: ${self.subtotal}")
        print(f"\n\tDiscount Applied: ${self.discount_amount}")

        print(f"\n\tGift Wrap Fee: ${self.gift_wrap_fee}")
        print(f"\n\tShipping Fee: ${self.shipping_fee}")

        self.total = self.subtotal - self.discount_amount + self.gift_wrap_fee + self.shipping_fee
        print(f"\n\tTotal: ${self.total}")

    def handle_input(self):
        for p in self.products:
            p.quantity = int(input(f"Enter quantity of {p.name}: "))
            p.total_amount = p.quantity * p.price

            gift_wrap = input(f"Is {p.name} wrapped as a gift? (yes/no): ").lower()
            if gift_wrap == 'yes':
                p.gift_wrap = True

            print("\n")

            self.subtotal += p.total_amount

        self.discount_rules()
        self.calc_fees()
        self.generate_invoice()



c = Cart()
c.handle_input()
