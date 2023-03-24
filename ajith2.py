print("**************** Welcome To Undatakar travel engency****************")

print("*****1.dubai*****")
print("*****2.maldives*****")
print("*****3.malesiya*****")
print("*****4.gova*****")
print("*****5.ooty*****")

def dubai(days,budjet,flight,sheet_no):
    if days>=10 and budjet>=20000 and flight>=112 and sheet_no>=23:
        print("Your Travelling Is Chennai To Dubai")
        print("passport is manitory")
        print("your budjet is 100+k")
        print("you flight name is air india,Your Sheet No Is 23c")
        print("Your Travelling Times IS 5h:35Min")
    else:
        print("Your Bedjet is below 80k")
        print("you passport is not valid")
    
def maldives(days,budjet,flight,sheet_no):
    if days>=8 and budjet>=15000 and flight>=76 and sheet_no>=67:
        print("Your Travelling is Chenni To Maldives") 
        print("Passport Is Manitory")
        print("you flight name is air asia,Sheet No is 67c")
        print("your budjet 80+k")
        print("Travelling Time Is 2h:15Min")
    else:
        print(" Your Brtjet is below 60k")

def malesiya(days,budjet,flight,sheet_no):
    if days>=7 and budjet>=13000 and flight>=334 and sheet_no>=117:
        print("Your Travelling Is Vellore To Malesiya")
        print("Passport Is Manitory")
        print("your budjet 70+k") 
        print("you flight name is indigo")
        print("Your Travelling Time Is 4h:40Min")
    else:
        print("Your Bedjet Is below 50k")
    
def goa(days,budjet,train):
    if days>=5 and budjet>=10000 and train>=666:
        print("your budjet 40k")
        print("train Name is Lalbakh Exp A/C2929 Compartment Sheet No 334")
        print("Incude Break Fast,Travelling Time is 21:23Min")
    else:
        print("below 25k,lalbakh Train is Not Avaliable")

def ooty(days,budjet,bus):
    if days>=3 and budjet>=5000 and bus>=202:
        print("your Bus Name is Krishna Travells 202")
        print("your Budjet is 20+k")
        print("travelling Time 11h:30Min,With 2 Rest Stopings")
    else:
        print("below 10K ,Krishna Travells Sheet Is Not Avaliable")
    
user=int(input("enter your number:"))

if user==1:
    days=int(input("enter your days:"))
    budjet=int(input("enter your budjet:"))
    flight=int(input("enter your flight:"))
    sheet_no=int(input("enter your sheet_no:"))
    dubai(days,budjet,flight,sheet_no)

elif user==2:
    days=int(input("enter your days:"))
    budjet=int(input("enter your budjet:"))
    flight=int(input("enter your flight:"))
    sheet_no=int(input("enter your sheet_no:"))
    maldives(days, budjet,flight,sheet_no)

elif user==3:
    days=int(input("enter your days:"))
    budjet=int(input("enter your budjet:"))
    flight=int(input("enter your flight:"))
    sheet_no=int(input("enter your sheet_no:"))
    malesiya(days,budjet,flight,sheet_no)

elif user==4:
    days=int(input("enter your days:"))
    budjet=int(input("enter your budjet:"))
    train=int(input("enter your train:"))
    goa(days,budjet,train)

elif user==5:
    days=int(input("enter your days:"))
    budjet=int(input("enter your budjet:"))
    bus=int(input("enter your bas name:"))
    ooty(days,budjet,bus)

else:
    print("first 5 numbers only threr...")
