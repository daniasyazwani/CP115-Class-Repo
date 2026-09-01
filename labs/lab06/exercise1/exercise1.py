# Escape Characters Exercise
# Print the receipt shown in the lab, using \n for new lines and \t for columns.
# Calculate every total, subtotal, and tax in your code. Do not type the money
# amounts in directly. Show every amount with exactly two decimal places.
Coffee_Total = 3.50 * 2
Muffin_Total = 2.10 * 3
Water_Total = 1.05 * 4
Sub_Total = Coffee_Total + Muffin_Total + Water_Total
Tax = Sub_Total * 0.06
Total = Tax + Sub_Total
print(
    f"========= RECEIPT ==========\n",
    f"Item\tPrice\tQty\tTotal\n",
    f"Coffee\t$3.50\t2\t${Coffee_Total}\n",
    f"Muffin\t$2.10\t3\t${Muffin_Total}\n",
    f"Water\t$1.05\t4\t${Water_Total}\n",
    f"------------------------------\n",
    f"Subtotal\t\t{Sub_Total}\n",
    f"Tax(6%)\t\t{Tax}\n",
    f"Total\t\t{Total}",
)