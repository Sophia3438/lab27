def record(total):
    with open("text.txt", "w") as txt:
        txt.write(str(total))
        print("Баланс оновлено: ", total)


def read_balance():
    try:
        with open("text.txt", "r") as txt:
            balance = float(txt.read())
    except FileNotFoundError:
        balance = 0.0  # якщо файл не знайдений, встановлюємо початковий баланс
        record(balance)
    return balance


def readd(operation):
    balance = read_balance()  # зчитуємо баланс
    if operation == "д":
        try:
            howMany = float(input("Скільки: "))
            record(balance + howMany)
        except ValueError:
            print("Помилка вводу! Введіть число.")
    elif operation == "в":
        try:
            howMany = float(input("Скільки: "))
            record(balance - howMany)
        except ValueError:
            print("Помилка вводу! Введіть число.")
    elif operation == 1:
        print("На балансі " + str(balance) + " грн \n")


while True:
    readd(1)
    readd(input("Додати/Відняти\n Д/В: ").lower())
