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

def main():
    print("Welcome to the BnB booking system!")

    choice = int(input("Choose your action:\n1: Login\n2: Signup\n"))

    if choice == 1:
        # Login
        login_choice = int(input("Choose your role:\n1: Customer\n2: Owner\n"))

        phone_no = int(input("Enter your phone number: "))
        password = input("Enter your password: ")

        if login_choice == 1:
            # Customer login
            customer = session.query(Customer).filter_by(phoneNumber=phone_no, passWord=password).first()
            if customer:
                print("Customer login successful!")

                # Option to book a BnB
                book_choice = int(input("Choose an action:\n1: Book a BnB\n2: Log out\n"))

                if book_choice == 1:
                    # Booking a BnB
                    location = input("Enter your desired location: ")

                    matching_bnbs = session.query(Bnb).filter_by(location=location).all()

                    if not matching_bnbs:
                        print(f"No BnBs found in location: {location}")
                    else:
                        print("Matching BnBs:")
                        for idx, bnb in enumerate(matching_bnbs, start=1):
                            print(f"{idx}: {bnb.name}, Address: {bnb.address}, Price: {bnb.price}")

                        choice = int(input("Enter the number of the BnB you want to book: "))

                        if 1 <= choice <= len(matching_bnbs):
                            selected_bnb = matching_bnbs[choice - 1]
                            checkin = input("Enter Check-In Date in this format YYYY-MM-DD: ")
                            checkout = input("Enter Check-Out Date in this format YYYY-MM-DD: ")

                            try:
                                check_in = datetime.strptime(checkin, "%Y-%m-%d").date()
                                check_out = datetime.strptime(checkout, "%Y-%m-%d").date()
                            except ValueError:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                                return

                            new_booking = Booking(customer=customer, bnb=selected_bnb, check_in=check_in, check_out=check_out)
                            session.add(new_booking)
                            session.commit()
                            print("Booking successful!")

                        else:
                            print("Invalid BnB selection.")

                elif book_choice == 2:
                    print("Logging out.")

            else:
                print("Invalid login credentials for Customer.")

        elif login_choice == 2:
            # Owner login
            owner = session.query(Owner).filter_by(phoneNumber=phone_no, passWord=password).first()
            if owner:
                print("Owner login successful!")

                # Option to register a BnB
                register_choice = int(input("Choose an action:\n1: Register a BnB\n2: Log out\n"))

                if register_choice == 1:
                    # Registering a BnB
                    location = input("Enter the location of your BnB: ")
                    address = input("Enter the address of your BnB: ")
                    price = int(input("Enter the price per night: "))
                    name = input("Enter the name of your BnB: ")
                    status = input("Enter the status of your BnB: ")

                    new_bnb = Bnb(owner=owner, location=location, address=address, price=price, name=name, status=status)
                    session.add(new_bnb)
                    session.commit()
                    print("BnB registration successful!")

                elif register_choice == 2:
                    print("Logging out.")

            else:
                print("Invalid login credentials for Owner.")

        else:
            print("Invalid role choice for login.")

    elif choice == 2:
        # Signup
        signup_choice = int(input("Choose your role:\n1: Customer\n2: Owner\n"))

        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        phone_no = int(input("Enter phone number: "))
        password = input("Enter password, the password must be 8 characters: ")

        if signup_choice == 1:
            # Customer registration
            existing_customer = session.query(Customer).filter_by(phoneNumber=phone_no).first()
            if existing_customer:
                print("Customer already exists. Please log in.")
            else:
                new_customer = Customer(firstName=fname, lastName=lname, phoneNumber=phone_no, passWord=password)
                session.add(new_customer)
                session.commit()
                print("Customer registration successful!")

        elif signup_choice == 2:
            # Owner registration
            existing_owner = session.query(Owner).filter_by(phoneNumber=phone_no).first()
            if existing_owner:
                print("Owner already exists. Please log in.")
            else:
                new_owner = Owner(firstName=fname, lastName=lname, phoneNumber=phone_no, passWord=password)
                session.add(new_owner)
                session.commit()
                print("Owner registration successful!")

        else:
            print("Invalid role choice for signup.")

    else:
        print("Invalid action choice. Please choose 1 for Login or 2 for Signup.")

    session.close()

if __name__ == "__main__":
    main()