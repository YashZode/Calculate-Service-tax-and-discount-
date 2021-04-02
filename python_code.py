

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    adult = 3 * 37550
    only_child = (37550/3)
    child = no_of_children * only_child
    total = adult + child
    service_tax = total * (7/100)
    overall_total = service_tax + total
    discount = overall_total * (10/100)
    total_ticket_cost = overall_total - discount
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)
