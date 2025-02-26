from ex import Expense

import calendar

import datetime

 

def main():

    Budget = 600000
    
    expense_file_path = "expense.csv"

    expense_chk = check_Expense()
    save_file(expense_chk,expense_file_path)
    summerize_Expense(expense_file_path,Budget)


def check_Expense():
    print('Ky khracha kela ahe ')

    Expense_name = input('kuta khracha kela ahe :- ')
    Expense_amount = eval(input('Kiti kharcha kela ahe  :- '))
    Expense_category = ['Food','Travel','Shopping','Work','Misc','Fun']

    while True:
        print('Kutyla Category madi khrach karat hote')
        for i,category_name in enumerate(Expense_category):
            print(f'{i+1}.{category_name}')

        value_range = f'[1-{len(Expense_category)}]'
        select_index = int(input(f'Category sanga :- {value_range} :- '))-1

        if select_index in range(len(Expense_category)):
            selected_category = Expense_category[select_index]
            print(selected_category)

            new_expense = Expense(name = Expense_name,amt = Expense_amount,cat = selected_category)
            return new_expense



        else:
            print('Invalid category !!!')


    
        break

def save_file(expense_chk:Expense,expense_file_path):
   print(f'kharcha file madhe save kara : {expense_chk} to {expense_file_path}')

   # it will create the csv File automatically 

   with open(expense_file_path,'a',encoding='UTF-8') as f:
       f.write(f'{expense_chk.name},{expense_chk.amount},{expense_chk.category}\n')
   
def summerize_Expense(expense_file_path,Budget):
    print('Summary banvat ahe')

    expenses:list[Expense] = []

    with open(expense_file_path,'r',encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
           #print(line)
           expense_name,expense_amount,expense_category = line.strip().split(',')
           print(f'{expense_name} {expense_amount} {expense_category}')

           line_expense = Expense(
               name = expense_name,
               amt = float(expense_amount),
               cat = expense_category)
           
           expenses.append(line_expense)
        #print(expenses)
    amount_by_category = {}
    for e in expenses:
        key = e.category
        if key in amount_by_category:
            amount_by_category[key] += e.amount
        else:
            amount_by_category[key] = e.amount
        
    print('Category wise khracha ahe !!')
    for key,amount in amount_by_category.items():
        print(f"{key} : Rs.{amount:.2f}")

    Total_kharcha = sum([x.amount for x in expenses])
    print(f'Total karcha kela ahe : Rs.{Total_kharcha}/-')

    Remaining_Budget = Budget - Total_kharcha
    print(f'{Remaining_Budget}Rs Yevda paise urle ahe')

    now = datetime.datetime.now()

    days_in_month = calendar.monthrange(now.year,now.month)[1]

    Remaining_days = days_in_month - now.day

    per_day_budget = Remaining_Budget / Remaining_days

    print(f'Per day Kiti kharcha karu shakto : Rs.{per_day_budget:.2f}/-')




if __name__ == "__main__":
    main()



