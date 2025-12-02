tasks = []        # list of tasks
habits = {}       # habit : streak
day = 1           # simple day counter

while True:
    print(f"\n--- Day {day} ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Done")
    print("4. Add Habit")
    print("5. View Habits")
    print("6. Check Habit Today")
    print("7. Wellness Insight")
    print("8. End Day")
    print("0. Exit")

    choice = input("Choose: ")

    # Add task
    if choice == "1":
        t = input("Task name: ")
        tasks.append([t, False])     # [task name, done?]
        print("Task added.")

    # View tasks
    elif choice == "2":
        if not tasks:
            print("No tasks.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "✓" if t[1] else "✗"
                print(f"{i}. {t[0]} [{status}]")

    # Mark task done
    elif choice == "3":
        num = int(input("Task number: "))
        if 1 <= num <= len(tasks):
            tasks[num-1][1] = True
            print("Task marked done.")
        else:
            print("Invalid number.")

    # Add habit
    elif choice == "4":
        h = input("Habit name: ")
        habits[h] = 0
        print("Habit added.")

    # View habits
    elif choice == "5":
        if not habits:
            print("No habits.")
        else:
            for h, s in habits.items():
                print(f"{h} — streak: {s}")

    # Check habit today
    elif choice == "6":
        h = input("Habit to check: ")
        if h in habits:
            habits[h] += 1
            print("Habit checked. Streak:", habits[h])
        else:
            print("Habit not found.")

    # Wellness insight
    elif choice == "7":
        # task score
        if tasks:
            done = sum(1 for t in tasks if t[1])
            task_score = done / len(tasks)
        else:
            task_score = 0

        # habit score (average streak)
        if habits:
            habit_score = sum(habits.values()) / len(habits)
        else:
            habit_score = 0

        print("\n--- Wellness Insight ---")
        print("Task score:", round(task_score, 2))
        print("Habit score:", round(habit_score, 2))

        if task_score > 0.5 and habit_score > 1:
            print("Great job today! 🌟")
        else:
            print("Keep going! You can improve tomorrow.")

    # End day
    elif choice == "8":
        day += 1
        print("Day ended. New day:", day)

    # Exit
    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")