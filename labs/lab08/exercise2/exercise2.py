employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

overtime_pay = (35/ overtime_hours)
gross_salary = (overtime_pay + base_salary)

if (tax_status == single and gross_salary >= 5000):
    tax_rate = 0.22
elif:
    tax_rate = 0.18
 (tax_status = married) and (gross_salary >= 6000):
    tax_rate = 0.20
else:
    tax_rate = 0.15
if (tax_status = head) and (gross_salary >= 5500):
    tax_rate = 0.25
else:
    tax_rate = 0.19

gross_salary 


print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")
