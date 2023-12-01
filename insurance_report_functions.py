# One Stop Insurance needs a program to enter and calculate new insurance policy information for its customers.
# Written By:  Kelly Stoyles
 #Date Written: November 17 - 29, 2023

# Import any required libraries
import datetime
import FormatValues as FV
import datetime


# Import any required Constants
DISCOUNT_RATE = .25
BASIC_PREMIUM_RATE = 869.00
EXTRA_LIABILITY = 130.00
GLASS_COVERAGE = 86.00
LOANER_CAR = 58.00
HST_RATE = .15
PROCESSING_FEE = 39.00
POLICY_NUMBER = 1944

#get today's date
PurDate = datetime.datetime.now()
print (PurDate)


# Import any required Functions

#This function will generate the first payment due on the insurance policy
def CalcPaymentDate(PurDate):
    PurYear = PurDate.year
    PurMonth = PurDate.month
    PurDay = PurDate.day

    if PurDay >= 25:
        PurMonth += 1

    PaymentDate = datetime.datetime (PurYear, PurMonth + 1, PurDay)
    return (PaymentDate)
 

PurchaseDate = "2023-10-4"  # is string so must be formatted
PurchaseDate = datetime.datetime.strptime (PurchaseDate, "%Y-%m-%d")
PaymentDate = CalcPaymentDate(PurchaseDate)


#C#This function will calculate the future Anniversary date
def CalcAnniversaryDate (PurDate):
    PurYear = PurDate.year
    PurMonth = PurDate.month
    PurDay = PurDate.day

    NextYearDate = datetime.datetime (PurYear + 1, PurMonth, PurDay)
    return (NextYearDate)


NextYearDate = CalcAnniversaryDate(PurDate)
print(NextYearDate) 

print()
print()

# Start the Main program

# Input customer information
while True:
    custFName = input("Enter the customer's first name: ").title()
    custLName = input("Enter the customer's last name: ").title()
    stAddress = input("Enter the customer's street address: ").title()
    city = input ("Enter the customer's city: ").title()

# Validate the province
    ProvLst = ["NL", "PE", "NS", "NB", "QC","ON","MB","SK","AB","BC","NT","NU","YT"]
    while True:
        province = input("Enter the customer's province (xx): ").upper()
        if province == " ":
            print ("Error. Province cannot be empty.")
        elif len(province) != 2:
            print ("Error. Province must be 2 digits.")
        elif province not in ProvLst:
            print ("Error.  Not a valid province. ")
        else:
            break
    print ("Province has been successfully entered. ")
    postalcode = input("Enter the customer's postal code: ")
    phoneNum = int(input("Enter the customer's phone number: "))

    DiscountPremium = 0
    print()
    print()
    
# Enter automobile information for insurance policy
    numCars = int(input("Enter the number of cars you wish to insure: "))
    if numCars > 1:
        discount= float((BASIC_PREMIUM_RATE * DISCOUNT_RATE) )
        DiscountPremium = float((BASIC_PREMIUM_RATE - discount) * (numCars - 1))
        totalPremium = float(BASIC_PREMIUM_RATE + DiscountPremium)
    else:
        totalPremium = BASIC_PREMIUM_RATE
    

# this function will calculate all the extra costs associated with car insurance.
    extLiability: str = input("Does the customer want extra liability up to $1,000,000.00? Enter Y or N. ").upper()
    if extLiability == "Y":
        costLiability = (EXTRA_LIABILITY * numCars)
    else:
        costLiability = 0

    glassCoverage = input ("Does the customer want glass coverage? Enter Y or N. ").upper()
    if glassCoverage == "Y":
        glassCoverage = (GLASS_COVERAGE * numCars)
    else:
        glassCoverage = 0

        
    loaner = input("Does the customer want a loaner car? Enter Y or N. ").upper()
    if loaner == "Y":
        loanerCost = (LOANER_CAR * numCars)
    else:
        loanerCost = 0
        
# total all the extras and calculate totalCost        
    totalExtras = (costLiability + glassCoverage + loanerCost)
    HST_1 = ((totalPremium + totalExtras )* HST_RATE)
    HST_2 =((DiscountPremium + totalExtras )* HST_RATE) * (numCars - 1)
    HST = (HST_1 + HST_2)
    totalCost = totalExtras + HST  + totalPremium  +  PROCESSING_FEE
    

# Here customer's payment options 
    print ()
    print ()
   
    #initialize variable
    downPayment = 0
    MonthlyPayment = 0
    FullPayment = 0

    print ("Your payment options are:" ) 
    print ("1. Cash - pay in full. ")
    print ("2. Finance - monthly payments. ")   
    choices = int (input ("Enter the method of payment?  "))
    print()
    if choices == 1:

            FullPayment = float(totalCost)
           
    else:
            choice =(input("Would you like to make a down payment (Y/N):  ")).upper()
            
            if choice == "Y":
                 
                downPayment = float(input("Enter the amount of the down payment:  "))
                MonthlyPayment = float((totalCost - downPayment)/ 8)
            else:
                MonthlyPayment = float(totalCost/ 8)
    break
print ()
print ()
# Insurance Receipt
print ()
print ()
print (f"                                           One Stop Insurance Company")
print (f"                                           231 Topsail Rd., Suite 200")
print (f"                                             St John's, NL A1P 2H6")
print ()
print ()
print()
print (f"  Policy #: {POLICY_NUMBER}")
print ()
print ()
print (f"  Customer Name:     {custFName} {custLName}")
print (f"  Address:           {stAddress}")
print (f"  City:              {city} ") 
print (f"  Province:          {province}") 
print (f"  PostalCode:        {postalcode}")
print (f"  Phone Number:      {phoneNum}")
print ()
print (f"==============================================================================================================================")
print ()
print (f"                                                              Liability          Glass          Optional                 ")
print (f"  Make          Model          Year          Premium        $1,000,000.00       Coverage       Car Loaner      HST Rate          ")
print (f"-------------------------------------------------------------------------------------------------------------------------------")
print ()
print (f"  Ford         Mustang         2020         {FV.FDollar2(BASIC_PREMIUM_RATE):>8s}          {FV.FDollar2(EXTRA_LIABILITY):>s}          {FV.FDollar2(GLASS_COVERAGE):>8s}         {FV.FDollar2(LOANER_CAR):>s}        {FV.FDollar2(HST_1):>8s}")
print ()
print (f"  (Additional Vehicles            )         {FV.FDollar2(DiscountPremium):>8s}         {FV.FDollar2(EXTRA_LIABILITY):>8s}          {FV.FDollar2(GLASS_COVERAGE):>8s}       {FV.FDollar2(LOANER_CAR):>8s}        {FV.FDollar2(HST_2):>8s}")
print ()
print (f"==============================================================================================================================")
print ()
print (f"  Total Premiums:       {FV.FDollar2(totalPremium):<8s}")
print (f"  Total Extras:           {FV.FDollar2(totalExtras):<8s}")
print (f"  Processing Fee:          {FV.FDollar2(PROCESSING_FEE):<8s}")
print (f"  H.S.T.:                 {FV.FDollar2(HST):<8s}")
print (f"__________________________________________")
print ()
print (f"  Yearly Premium:       {FV.FDollar2(totalCost):<8s}")
print ()
print ()
print (f"==============================================================================================================================")
print ()
print (f"  Payment Options:")
print (f" -----------------------------------------")
print()
print (f"  Down Payment:         {FV.FDollar2 (downPayment):<9s}")
print (f"  Pay in Full:          {FV.FDollar2 (FullPayment):<9s}")
print (f"  Monthly Payments:     {FV.FDollar2 (MonthlyPayment):<9s}")
print ()
print (f"==============================================================================================================================")
print ()
print (f"  First Payment Due:         {PaymentDate}")
print (f"  Policy Anniversary Date:   {NextYearDate}")
print ()
print (f"  Insurance Agent:           Kelly Stoyles")
print (f"  Phone Number:              709-642-9853")
print ()
print (f"==============================================================================================================================")
print ()
print (f"  Previous Claim Information")
print (f"  ---------------------------")
print ()
print (f"  Claim #          Claim Date          Claim Amount")
print (f"-------------------------------------------------------------------------------------------------------------------------------")
print ()
print (f"  645-2B           2016-10-17           $1,200.52")
print (f"  487-9F           2014-03-24           $2,218.65")
print (f"  134-5T           2011-12-23           $  865.97")
print ()
print (f"==============================================================================================================================")
print (f"==============================================================================================================================")

        
        
        
