
class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure =departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(20)] 


class Phriton:
    total_bus =5
    total_bus_list = []
    
    def add_bus(self):
        bus_no = int(input("Enter Bus No: "))

        flag = 1
        for w in self.total_bus_list:
            if bus_no == w['coach']:
                print("This Bus Already Added")
                flag = 0

        if flag:
            bus_driver = input("Enter Bus Driver Name : ")
            bus_arrival = input("Enter Bus Arrival Time : ")
            bus_departure = input("Enter Bus Departure Time : ")
            bus_from = input("Enter Bus Starting From : ")
            bus_to = input("Enter Bus Destination : ")
            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_list.append(vars(self.new_bus))
            print("\nBus Added Successfully")

class Counter(Phriton):
    user_list = []
    def Booking(self):
        bus_no = int(input("Enter Bus No : "))
        for w in self.total_bus_list:
            if bus_no == w['coach']: #find bus
                passanger = input("Enter Your Name : ")
                seat_no = int(input("Enter Seat No : "))

                if seat_no > 20:
                    print("Sorry sir,This Seat is limited Out !!")

                elif w['seat'][seat_no-1] != "Empty":
                     print("Sorry sir,This Seat is Already booked !!")
                else:
                    w['seat'][seat_no-1] = passanger
                    print(f'Succesfully {bus_no} is Booked for You. Have a nice Journy sir.')
            else:
                print("No bus available now!")
                    
        # for bus in self.total_bus_list:
        #     print(bus['seat'])

    def show_ticket(self):
        bus_no= int(input("Enter Bus Number"))

        for w in self.total_bus_list:
            if bus_no== w['coach']:
                print('*' * 50)
                print()
                print(f"{' '*10}{'#'*10}BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t\t Driver :{w['driver']}")
                print(f"Arrival : {w['arrival']}\t\t\t Departure Time : {w['departure']} \n From: \t{w['from_des']} \t\t\t TO: \t{w['to']}")

                a= 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end = "\t\t")
                        a+=1
                    for j in range(2):
                        print(f"{a}. {w['seat'][a-1]}", end = "\t\t")
                        a+=1
                        
                    print()
                print('*' * 50)

    def get_users(self):
        return self.user_list
    
    def create_account(self):
        name = input("Enter Your Username : ")
        password = input("Enter a password : ")
        self.new_bus = User(name, password)

        self.user_list.append(vars(self.new_bus))

  
    def available_buses(self):
        if len(self.total_bus_list) == 0:
            print("No bus in this root")

        else:
            print('*' * 50)
            for bus in self.total_bus_list:
                print()
                print(f"{' ' * 10} {'#' *10} BUS {bus['coach']} Info. {'#' *10}")
                print(f"Bus Number : {bus['coach']} \t Driver : {bus['driver']}")
                print(f"Arrival : {bus['arrival']} \t Departure Time : {bus['departure']} \nFrom : {bus['from_des']} \t To : {bus['to']} ")
            print('*' * 50)

# Tohidul islam Rupok
# Dhaka international university

while True:
    company = Phriton()
    b = Counter()
    print("1. Create an account \n 2.Login to your account\n 3.EXIT")
    user_input = int(input("Enter Your Choice : "))

    if user_input ==3:
        break
    elif user_input ==1:
        b.create_account()

    elif user_input  == 2:
        name = input("Enter Your Username : ")
        password = input("Enter a password : ")

        flage = 0
        isAdmin = False

        if name == "admin" and password =="123":
            isAdmin = True
        #chaeck pass/id
        if isAdmin == False:                #he is not a admin
            for user in b.get_users():
                if user['username'] == name and user['password'] == password:
                    flage = 1 #find
                    break 

                
            if flage:
                while True:
                    print(f"\n {' ' * 10}Welcome to LAL_Sobug Tricket Booking System.")
                    print("1.Available buses\n2.Show Bus Info\n3.Booking\n4.Exit")
                
                    a = int(input("Enter Youe Choice : "))
                    if a ==4:
                        break
                    elif a==1:
                        b.available_buses()
                    elif a==2:
                        b.show_ticket()
                    elif a == 3:
                        b.Booking()

            else:
                print("No user found.")
                
        else:
            while True:
                print(f"\n {' ' * 10}Hello Admin sir welcome back to LAL_Sobug Tricket Booking System.")
                print("1.Add Bus\n2.Available Buses\n3.Show Bus Info\n4.EXIT")

                a = int(input("Enter Youe Choice : "))
                if a ==4:
                    break
                elif a==1:
                   b.add_bus()
                elif a==2:
                    b.available_buses()
                elif a == 3:
                    b.show_ticket()

