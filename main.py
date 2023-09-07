from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from customer import Base, Customer
from owner import Owner
from bnb import Bnb
from booking import Booking
from datetime import datetime

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

def Customer_login(login_choice):
    if login_choice == 1:
        phone_no = int(input("Enter your phone number: "))
        password = input("Enter your password: ")
        customer = session.query(Customer).filter_by(phoneNumber=phone_no, passWord=password).first()
         
        if customer:
            print(f"Welcome Back {customer.firstName} {customer.lastName}")
            booking(customer)
        else:
            print("Invalid login credentials for Customer.")





def Customer_account_creation(creation_choice):
    if creation_choice == 1:
        fname=input("Enter your First Name: ")
        lname=input("Enter your Sir Name: ")
        phoneNo=int(input("Enter your Phone Number: "))
        passWord=input("Enter your password: ")

        # check if Customer exists

        existing_customer=session.query(Customer).filter_by(phoneNumber=phoneNo).first()

        if existing_customer:
            print("User already exists")
        else :
            customer = Customer(firstName=fname, lastName=lname, phoneNumber=phoneNo, passWord=passWord)
            session.add(customer)
            session.commit()
            print("Customer registration successful!")
            booking(customer)



def booking(customer):
    booking_choice=int(input("Do you want to make booking ? \n 1: Yes \n 2: No \n"))

    if booking_choice == 1:
        location=input("Enter desired destination ? ")

        matching_location=session.query(Bnb).filter_by(location=location).all()

        making_bookings(matching_location,location,customer)
    elif booking_choice == 2:
        print("Logging  Out")
    else:
        print("Enter valid choice")



def making_bookings(matching_location,location, customer):
    if not matching_location:
            print(f"No bns found in this location {location}")
    else:
        print(f"Here are the Bnbs in {location}")
        for idx, bnb in enumerate(matching_location, start=1):
            print(f"{idx}, Name: {bnb.name} Address: {bnb.address}, Price: {bnb.price}, ")

        choice=int(input("Enter the number for the Bnb of your choocing: "))

        if 1 <= choice <= len(matching_location):
            selected=matching_location[choice-1]
            checkin = input("Enter Check-In Date in this format YYYY-MM-DD: ")
            checkout = input("Enter Check-Out Date in this format YYYY-MM-DD: ")

            try:
                check_in = datetime.strptime(checkin, "%Y-%m-%d").date()
                check_out = datetime.strptime(checkout, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

            new_booking = Booking(customer=customer, bnb=selected, check_in=check_in, check_out=check_out)
            session.add(new_booking)
            session.commit()
            print("Booking successful!")


            selected.status="booked"
            session.commit()
        else:
            print("You have entered invalid bnb selection")




def Owner_login(login_choice):
    if login_choice == 2:
        phone_no = int(input("Enter your phone number: "))
        password = input("Enter your password: ")
        owner = session.query(Owner).filter_by(phoneNumber=phone_no, passWord=password).first()


        if owner:
            print(f"Welcome back {owner.firstName} {owner.lastName}")
            
            register_bnb(owner)
        else :
            print("Invalid credentials !!")




def Owner_register(creation_choice):
    
    if creation_choice == 2:
        fname=input("Enter your First Name: ")
        lname=input("Enter your Sir Name: ")
        phoneNo=int(input("Enter your Phone Number: "))
        passWord=input("Enter your password: ")

        existing_owner=session.query(Owner).filter_by(phoneNumber=phoneNo).first()

        if existing_owner:
            print("User already exists")

        else:
            owner=Owner(firstName=fname, lastName=lname, phoneNumber=phoneNo, passWord=passWord)
            session.add(owner)
            session.commit()
            print("Owner registration successful!")
            register_bnb(owner)





def register_bnb(owner):
    choice=int(input("Do you want to register a Bnb \n 1: Yes \n 2: No \n"))
    if choice == 1:
        location = input("Enter the location of your BnB: ")
        address = input("Enter the address of your BnB: ")
        price = int(input("Enter the price per night: "))
        name = input("Enter the name of your BnB: ")
        status = input("Enter the status of your BnB: ")

        new_bnb = Bnb(owner=owner, location=location, address=address, price=price, name=name, status=status)
        session.add(new_bnb)
        session.commit()
        print("BnB registration successful!")
    else:
        print("Logging Out")


def main():
    print("Welcome to Bnb booking system!")

    choice = int(input("Choose your action:\n1: Sign in\n2: Sign up\n"))

    if choice == 1:
        login_choice = int(input("Choose your role:\n1: Customer\n2: Owner\n"))
        Customer_login(login_choice)
        Owner_login(login_choice)
    elif choice == 2:
        creation_choice=int(input("Choose your role: \n1: Customer \n 2: Owner \n"))
        Customer_account_creation(creation_choice)
        Owner_register(creation_choice)


if __name__ == "__main__":
    main()