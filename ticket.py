# Ticket
class Ticket:
   
    def __init__(self,staffID, Name, email, Description):
        
        self.staffID = staffID
        self.Name = Name
        self.email = email
        self.Description = Description
        self.Status = "Open"

    def Submit_ticket(self,TicketNo):
        self.ticket_ID = TicketNo
       
        
    def Resolve(self):
        newpassword= ("");
        if self.Description == ("change password"):
            Staff_Id=str(self.staffID)
            newpassword = Staff_Id[:2]+self.Name[:3]
            print("your new password is:" +newpassword)
            self.Status="Closed"
        return newpassword

    def DisplaytTicket(self):
        print("ticket_ID",self.ticket_ID)
        print("staffID",self.staffID)
        print("Name",self.Name)
        print("email",self.email)
        print("Description",self.Description)
        print("status",self.Status)

        
                 
        