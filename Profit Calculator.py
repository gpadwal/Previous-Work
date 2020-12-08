#Python Net Profit Calculator



def confirm(): #CONFIRMS A YES OR NO ANSWER
    ans = input("\nEnter Y for Yes or N for No: ")
    while ans.upper() != "Y" and ans.upper() != "N":
        print("Sorry, I didn't get that.")
        delay(0.25)
        ans =input("Please enter Y for Yes or N for No: ")
    if ans.upper()== "Y":
        delay(.25)
        return True
    elif ans.upper() == "N":
        delay(.25)
        return False

def delay(t): #TIME DELAY BETWEEN LINES (FOR AESTHETIC)
    import time
    time.sleep(t)

def intro(): #TO CONFIRM THE PROGRAM WASN'T OPENED BY ACCIDENT
    print("""Welcome to Gurjot's Net Profit Calculator for
Independent Contractors (DELIVERY). I calculate your gross
sales and deduct your expenses to calculate your net profit.
\nWould you like to continue?""")
    ans = confirm()
    if ans == True:
        delay(.75)
        print("Let's get started.")
        delay(.5)
        print("We'll calculate your gross income first.")
        delay(1.5)
    elif ans == False:
        print("Goodbye!")
        delay(1)
        exit()

def income(company): #COMPANY AND GETS TOTAL
    print("\nDid you have any income from", company, "today?")
    ans = confirm()
    delay(0.45)
    if ans == True:
        total = input('\nWhat was your income from ' + company + ' today?\nIncome: $')
        while ans == True:
            try:
                val = float(total)
                val = float("{:.2f}".format(val))
                delay(0.25)
                print("\nIs $",val, "correct?")
                totalconfirm = confirm()
                if totalconfirm == True:
                    print('')
                    delay(0.25)
                    return val
                    break
                elif totalconfirm == False:
                        total = input('What was your income from ' + company + ' today?\nIncome: $')
            except ValueError:
                print("\nInvalid amount! Please enter in $XX.XX format.")
                total = input('Income: $')
    elif ans == False:
        return 0
            



def main():
    intro()
    companies = ['CompA', 'CompB', 'CompC']
    grand_total = 0
    for company in companies: 
        total = income(company)
        grand_total += total
    print('Your Gross Income is $'+"{:.2f}".format(grand_total)+'.')
        

main()
    
