#Write a program for presale tickets.Each buyer can buy up to 4 tickets.
# No more than 20 tickets can be sold total. Prompt the user for the desired
# number of tickets and then display the number of remaining tickets after their purchase.
# Repeat until all tickets have been sold. Then display the total number of buyers.

#creating function
def main(remaining_tickets):
    ticket_buyers = int(input(f'How many tickets would you like to buy? (Up t0 4)'))

    #if statement for limit on ticket purchases
    if ticket_buyers <= 4 and ticket_buyers <= remaining_tickets:
        remaining_tickets -= ticket_buyers
        print(f'You have purchased {ticket_buyers} tickets.')

    #else condition for no exceeded amount of tickets
    else:
        print('No tickets available or limit of 4 tickets. ')

    return remaining_tickets

#creating second function
def ticket_counter():
    #intializing variables for total tickets available, total people
    #buying the tickets, and connecting remaining tickets to total tickets
    total_tickets = 20
    remaining_tickets = total_tickets
    total_people = 0

    #while loop until tickets are sold out
    while remaining_tickets > 0:
        remaining_tickets = main(remaining_tickets)
        #purchase count accumulated
        total_people += 1
        print(f'Tickets remainng: {remaining_tickets} \n')

    #Displaying total buyers
    print(f'Sold out! Total buyers : {total_people}')

#displaying function
ticket_counter()



