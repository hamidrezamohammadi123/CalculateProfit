import os


WHITE   = '\033[97m'
BLUE    = '\033[94m'
RED     = '\033[31m'
YELLOW  = '\033[33m'
GREEN   = '\033[32m'
RESET   = '\033[0m'


MAH=12
# We define a function that calculates the daily profit
def daily_profit(capital, interest):
    return capital * interest / 100

## We define a function that calculates the monthly profit
def monthly_profit(capital, interest, days):
    profit = 0
    for day in range(days):
        profit += daily_profit(capital, interest)
        capital += daily_profit(capital, interest)
    return profit

def format_comma (number):
    return "{:,}".format (number)



os.system('cls')
# We ask the user to enter the initial capital and the daily profit percentage
#capital = float(input("Initial Investment     :"))
#interest = float(input("Daily profit percentage:"))
capital = 20000000
c=capital
interest = 2
print("-----------------------------------------------------------------------")
print("This program  calculates the final capital in  different time intervals ")
print("based on the initial capital and the expected profit percentage per day")
print("              and the number of tradable days")
print("           ------------------------------------")
print(f"Initial Investment      : {format_comma(capital)}  ")
print(f"Daily profit percentage : {interest} ")
print(f"Number of trading days per month : {MAH}")
print("-----------------------------------------------------------------------")
print(f"{RED}                              profit      Profit from    Profit percentage ")
print(f" Month  Day    Capital        state      the beginning       so far {WHITE}")


# یک متغیر برای شمارش ماه‌ها تعریف می‌کنیم
month = 1

# یک حلقه تا زمانی که کاربر می‌خواهد ادامه می‌دهیم
while True:
    # اگر ماه اول است، سود روزانه را چاپ می‌کنیم
    if month <= 1:
        for day in range(MAH):
            fp=daily_profit(capital, interest)
            temp=int(capital)
            p=int(fp+capital)
            dp=format_comma(p)
            if day==MAH-1:
                print(f"  {month}      {(day + 1):<2}   {dp}     {GREEN}{format_comma(p-temp)} {WHITE}     {format_comma(p-c)}          {GREEN}% {round((capital-c)/c*100,2)}{WHITE} ")
                print("-----------------------------------------------------------------------")
                print(f"{RED}                         profit      Profit from    Profit percentage ")
                print(f" Month   Capital      state   the beginning       so far{WHITE}")

            else:
                print(f"  {month}      {(day + 1):<2}   {dp}     {GREEN}{format_comma(p-temp)} {WHITE}     {format_comma(p-c)}          {GREEN}% {round((capital-c)/c*100,2)}{WHITE} ")
            capital += fp
    # در غیر این صورت، سود ماهیانه را چاپ می‌کنیم
    else:
        fp=monthly_profit(capital, interest, MAH)
        p=int(fp+capital)
        temp=int(capital)
        mp=format_comma(p)
        print(f"  {month:<2}    {mp}     {GREEN}{format_comma(p-temp)} {WHITE}     {format_comma(p-c)}      {GREEN}% {round((capital-c)/c*100,2)}{WHITE}")
        capital += fp
    # از کاربر می‌پرسیم که آیا می‌خواهد ادامه دهد یا خیر
    #answer = input("continiue ?")
    # اگر کاربر خیر گفت، حلقه را متوقف می‌کنیم
    if month == 12:
        break
    # در غیر این صورت، شمارنده ماه‌ها را یکی افزایش می‌دهیم
    else:
        month += 1