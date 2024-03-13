import pandas as pd

df = pd.read_csv("data/hotels.csv", dtype={"id":str})
df_cards = pd.read_csv("data/cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pd.read_csv("data/card-security.csv", dtype=str)


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name =  df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def available(self):
        """Check if the hotel is abailable."""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()

        if availability == 'yes':
            return True
        else:
            return False
            

    def book(self):
        """Book a hotel by changing its availability to no."""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("data/hotels.csv", index=False)


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation.
        Here are your booking details:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content
    

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self,  expiration, holder, cvc):
        card_data = {"number": self.number,
                     "expiration": expiration,
                     "holder": holder,
                     "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, entered_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()

        if password == entered_password:
            return True
        else:
            return False
        

class SpaReservationTicket(ReservationTicket):
    def generate(self):
        content = f"""
        Thank you for your reservation.
        Here are your SPA booking details:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content

print(df)
hotel_id = input("Enter the id oƒ the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():

    # card_number = input("Enter your credit card number: ")
    # card_exp_date = input("Enter expire date of your card (MM/YY): ")
    # card_holder = input("Enter card holder name: ")
    # card_cvv_code = input("Enter CVV of your card: ")

    credit_card = SecureCreditCard(number="12345")
    if credit_card.validate(expiration="12/26",holder="JOHN SMITH",cvc="123"):
        if credit_card.authenticate(entered_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
            
            while True:
                spa_package = input("Do you want to book a spa package? ")
                if spa_package == "yes":
                    spa_hotel = SpaReservationTicket(name, hotel)
                    print(spa_hotel.generate())
                    break

                elif spa_package == "no":
                    print("Thank you. Your Reservation completed.")
                    break

                else:
                    print("Invalid Selection. Type yes or no.")
        else:
            print("AuthFailed: There was a problem with your payment.")
    else:
        print("ValidatationFailed: Credit card validation failed.")
else:
    print("NotAvailable: Hotel is not free.")