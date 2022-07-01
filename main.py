import Task_1.Task1_Main
import Task_2.Task2_Main
import Task_3.Task3_Main

print("Skriv nr på task for å gå til den")
select_nr = input()

if select_nr == "1":
    Task_1.Task1_Main.multiple_of_3_and_5()
elif select_nr == "2":
    Task_2.Task2_Main.even_fibonacci_numbers()
elif select_nr == "3":
    Task_3.Task3_Main.largest_prime_factor()
