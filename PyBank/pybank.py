import csv
import os

budget_data_raw = os.path.join("Resources", "budget_data.csv")

with open(budget_data_raw) as budget_data:
	reader = csv.reader(budget_data)

	header = next(reader)

	first_row = next(reader)
	print(first_row)

	total_months = 1
	total_amount = float(first_row[1])
	max_profit = float(first_row[1])
	max_month = first_row[0]
	min_profit = float(first_row[1])
	min_month = first_row[0]
	for row in reader:
		total_months += 1
		total_amount += float(row[1])
		if float(row[1]) > max_profit:
			max_profit = float(row[1])
			max_month = row[0]
		if float(row[1]) < min_profit:
			min_profit = float(row[1])
			min_month = row[0]

	average_change = total_amount / total_months

summary = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${int(total_amount)}
Average Change: ${round(average_change, 2)}
Greatest Increase in Profits: {max_month} (${int(max_profit)})
Greatest Decrease in Profits: {min_month} (${int(min_profit)})
----------------------------
"""

print(summary)


output_file = os.path.join("Resources", "budget_summary.txt")
with open(output_file, "w") as txt_file:
    txt_file.write(summary)