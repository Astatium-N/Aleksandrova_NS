salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_cap = 0
spend_plus = spend
for month in range(1, months + 1):
    if spend_plus > salary:
        money_cap += spend_plus - salary
    if month < months:
        spend_plus *= (1 + increase)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_cap = round(money_cap, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_cap)
