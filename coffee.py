amount_due = 50  # Необходимая сумма для покупки кофе

coins_inserted = 0  # Количество вставленных монет

print("Нужная сумма: 50")

while coins_inserted < amount_due:
    coin = int(input("Вставьте монету: "))
    coins_inserted += coin

change_owed = coins_inserted - amount_due

if change_owed >= 0:
    print(f"Ваша сдача: {change_owed}")
