git init
git remote add origin <url-вашего-репозитория>
git push -u origin main
def main():
    # Вариант 1: предустановленный массив
    input_array = ["Hello", "2", "world", ":-)"]

    # Вариант 2: ввод с клавиатуры
    # input_array = input("Введите строки через запятую: ").split(',')
    # input_array = [s.strip() for s in input_array]

    # Фильтрация
    result = []
    for item in input_array:
        if len(item) <= 3:
            result.append(item)

    # Вывод
    print("Исходный массив:", input_array)
    print("Результат:", result)


if __name__ == "__main__":
    main()