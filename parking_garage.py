class Parking_Garage:
    '''
    Creates a parking garage representation object that tracks tickets, parking spaces,
    and tickets paid or unpaid. 
    '''
    def __init__(self, tickets=[x for x in range(1,101)], parkingSpaces=[x for x in range(1,101)], currentTicket={}):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket    

    def takeTicket(self):
        # takes first ticket from tickets list
        ticket_number = self.tickets.pop(0)
        print(f'Your ticket number is {ticket_number}')
        
        # removes last spot from parkingSpaces list
        self.parkingSpaces.pop()
        
        # adds the ticket number with value 'Unpaid' to the currentTicket dictionary
        self.currentTicket[ticket_number] = 'Unpaid'

        return ticket_number
    
    def payForParking(self, ticket):
        payment = (input('Please provide your ticket number '))
        # ensures an int is entered
        try:
            payment_int = int(payment)
        except:
            print("Please enter the whole number value ")
            payForParking(self)
        
        if payment_int != "" and payment_int in self.currentTicket:
            self.currentTicket[payment_int] = 'Paid'
            print('Your ticket has been paid. Please leave in 15 min. Or else...')
        else:
            while payment not in self.currentTicket:
                payment = input("Please enter a valid ticket number or 'Abort' ")
                if payment.lower() == 'abort':
                    print('Process terminated')
                    break
                elif payment in self.currentTicket:
                    payment = int(payment)
    
    def leaveGarage(self, ticket):
        # simulates leaving the garage
        if self.currentTicket[ticket] == 'Paid':
            print('Thank You, have a nice day!')
            open_space = self.parkingSpaces[-1] + 1
            self.parkingSpaces.append(open_space)
            new_ticket = self.tickets[-1] + 1
            self.tickets.append(new_ticket)

        elif self.currentTicket[ticket] != 'Paid':
            pay_now = input('Would like you like to pay now? Enter Y or N ')
            if pay_now.lower() == 'y':
                self.payForParking(ticket)
                self.leaveGarage(ticket)
            elif pay_now.lower() != 'y':
                while pay_now.lower() != 'y':
                    pay_now = input('You must pay to leave :) Pay now? Please enter Y or "Abort" to terminate process ')
                    if pay_now.lower() == 'abort':
                        break 

        
new_garage = Parking_Garage()
ticket = new_garage.takeTicket()
new_garage.payForParking(ticket)
new_garage.leaveGarage(ticket)

# print(new_garage.tickets) 
# print(new_garage.parkingSpaces)
# print(new_garage.currentTicket)

1
