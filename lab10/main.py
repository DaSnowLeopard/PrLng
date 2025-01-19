import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x350')
window.title("Лабораторная 10, вариант 3")

q1 = tk.Label(window, text="Выберите способ ввода чисел:\n1 - с клавиатуры\n2 - из файла")
q1.pack()

text_widget = tk.Text(window, height=5, width=30)
text_widget.pack()

result_label = tk.Label(window, text="")
result_label.pack()

ask_label = tk.Label(window, text="")
ask_label.pack()

numbers = []

def process_numbers():
    global numbers

    try:
        numbers_str = text_widget.get("1.0", tk.END).strip()
        if not numbers_str:
            result_label.config(text="Пожалуйста, введите числа.")
            return

        numbers = [int(x) for x in numbers_str.splitlines()]

        if not numbers:
            result_label.config(text="Некорректный ввод. Введите целые числа, каждое на новой строке.")
            return

        if len(numbers) % 2 == 0:
            midpoint = len(numbers) // 2
            s1 = sum(x for x in numbers[:midpoint] if x > 0)
            s2 = sum(x for x in numbers[midpoint:] if x < 0)
            if len(numbers) % 2 != 0:  # если нечетное количество элементов
                if numbers[midpoint] < 0:
                    s2 += numbers[midpoint]  # Вычитаем средний элемент если он отрицательный.
                elif numbers[midpoint] > 0:
                    s1 -= numbers[midpoint]  # Вычитаем средний элемент если он положительный.
            result_label.config(text=f"S1: {s1}\nS2: {s2}")
            ask_label.config(text="нажмите на кнопку, чтобы сохранить итог в файл")

        elif len(numbers) % 2 != 0:
            midpoint = (len(numbers) // 2) + 1
            s1 = sum(x for x in numbers[:midpoint] if x > 0)
            s2 = sum(x for x in numbers[midpoint:] if x < 0)
            if len(numbers) % 2 != 0:  # если нечетное количество элементов
                if numbers[midpoint] < 0:
                    s2 += numbers[midpoint]  # Вычитаем средний элемент если он отрицательный.
                elif numbers[midpoint] > 0:
                    s1 -= numbers[midpoint]  # Вычитаем средний элемент если он положительный.
            result_label.config(text=f"S1: {s1}\nS2: {s2}")
            ask_label.config(text="нажмите на кнопку, чтобы сохранить итог в файл")

    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод. Введите целые числа, каждое на новой строке.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла неожиданная ошибка: {e}")


def input_from_file():
    global numbers

    try:
        with open("1.txt", "r") as f:
            lines = f.readlines()
            numbers = [int(line.strip()) for line in lines]
            if not numbers:
                messagebox.showerror("Ошибка", "Файл пуст или содержит некорректные данные.")
                return

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл 1.txt не найден.")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный формат данных в файле. Введите только целые числа.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка при чтении файла: {e}")

def save_to_file():
    global numbers

    s1, s2 = process_numbers_from_list(numbers)
    try:
        with open("2.txt", "w", encoding="utf-8") as f:
            f.write(f"s1: {s1}  s2: {s2}\n")
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл 2.txt не найден.")

def process_numbers_from_list(numbers):
    midpoint = len(numbers) // 2
    s1 = sum(x for x in numbers[:midpoint] if x > 0)
    s2 = sum(x for x in numbers[midpoint:] if x < 0)
    if len(numbers) % 2 != 0:  # если нечетное количество элементов
        if numbers[midpoint] < 0:
            s2 += numbers[midpoint]  # учитываем средний элемент если он отрицательный
        elif numbers[midpoint] > 0:
            s1 -= numbers[midpoint]  # учитываем средний элемент если он положительный
    return s1, s2



btn2 = tk.Button(window, text="Способ 2", command=input_from_file)
btn2.pack()
btn3 = tk.Button(window, text="Сохранить", command=save_to_file)
btn3.pack()
button = tk.Button(window, text="Обработать числа", command=process_numbers)
button.pack(pady=10)

window.mainloop()