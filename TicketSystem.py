from ticket import Ticket
Tickets =[]
ticketnumber = 2000

def Submit_tickets(Tickets,ticketnumber):
    ticket1=Ticket(20245, "David1", "DavidN@hotmail.com", "change password")
    Tickets.append(ticket1)
    ticketnumber +=1
    ticket1.Submit_ticket(ticketnumber)
    ticket2=Ticket(20436, "Grace1", "Grace.d@gmail.com", "Monitor stopped working")
    Tickets.append(ticket2)
    ticketnumber +=1
    ticket2.Submit_ticket(ticketnumber)
    ticket3=Ticket(20879, "Kristine1", "Kristine.l@gmail.com", "Computer is running very slow ")
    Tickets.append(ticket3)
    ticketnumber +=1
    ticket3.Submit_ticket(ticketnumber)

def Prints_Ticket(Tickets):
    for x in Tickets:
        x.DisplaytTicket()

def statics(Tickets):
    
    counterOpen = 0 
    counterClosed = 0
    counterReopen= 0
    i=0
    n= len(Tickets)

    while i <n:
        T=str(Tickets[i].Status)
        if T == "Open":
           counterOpen+=1 

        elif T == "Closed":
            counterClosed+=1   

        else:
          counterReopen+=1  
            
        i+=1
    print("the number of opened ",counterOpen)
    print("the number of Closed ",counterClosed)
    print("the number of Reopened ",counterReopen)

Submit_tickets(Tickets,ticketnumber)
Prints_Ticket(Tickets)
for x in Tickets:
    NewPass = x.Resolve()
    print(NewPass)
Prints_Ticket(Tickets)
statics(Tickets)