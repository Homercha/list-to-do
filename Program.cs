using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        List<string> tasks = new List<string>();

        while (true)
        {
            Console.WriteLine("\n1.Додати завдання");
            Console.WriteLine("2.Показати");
            Console.WriteLine("3.X");
            Console.WriteLine("4.Вихід");

            Console.Write("Вибір: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("Введіть завдання: ");
                    string task = Console.ReadLine();

                    if (!string.IsNullOrWhiteSpace(task))
                    {
                        tasks.Add(task);
                    }
                    else
                    {
                        Console.WriteLine("Завдання не може бути порожнім.");
                    }

                    break;

                case "2":

                    Console.WriteLine("\nСписок завдань:");

                    if (tasks.Count == 0)
                    {
                        Console.WriteLine("Список завдань порожній ");
                    }
                    else
                    {
                        for (int i = 0; i < tasks.Count; i++)
                        {
                            Console.WriteLine($"{i + 1}. {tasks[i]}");
                        }
                    }

                    break;

                case "3":

                    if (tasks.Count > 0)
                    {
                        Console.Write("Номер завдання: ");
                        int number = Convert.ToInt32(Console.ReadLine());

                        // Функціональна помилка №2
                        tasks.RemoveAt(0);

                        // Функціональна помилка №3
                        // Відсутнє повідомлення про видалення
                    }

                    break;

                case "4":
                    return;

                default:
                    Console.WriteLine("Невірний вибір");
                    break;
            }
        }
    }
}