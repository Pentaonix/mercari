# Mercari tra gop

value = input("Enter Figure price:\n")
date_make_decision = input("Enter the day you would buy figure (from 1 to 30):\n")
date_to_pay_each_month = input("Enter the day you make payment for each month (from 1 to 30):\n")
amount = input("Enter the amount to pay each month:\n")

fig_price = int(value)
bought_day = int(date_make_decision)
days_in_a_month = 31
commission_rate = 0.15
days_in_a_year = 365
months = 0
final_money = int(value)

# first payment
first_interest = int(fig_price * (days_in_a_month - (bought_day + 1) + 1) * commission_rate / days_in_a_year)
months = 1
fig_price = int(fig_price - (int(amount)) + first_interest)
final_money = final_money + first_interest

# from 2nd payment
while fig_price != 0:
    const_day = int(date_to_pay_each_month) - 1 + 1
    interest = int((int(value) * const_day * commission_rate / days_in_a_year) + (fig_price * (days_in_a_month - (const_day + 1)) * commission_rate / days_in_a_year))
    if int(fig_price - int(amount) + interest) >= 0:
        fig_price = int(fig_price - int(amount) + interest)
    else:
        fig_price = 0
    months += 1
    final_money += interest
    print(f"Thang thu {months}, so tien con phai tra la {fig_price}")
print(f"Tong tien phai tra la: {final_money}")