def get_average(Subject1 ,Subject2 , Subject3):
    return (Subject1 + Subject2 + Subject3) / 3


def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def main():
    name = str(input("Enter a Name of the Students: "))
    print(name)
    s1 = float(input("Enter the marks of Subject 1: "))
    s2 = float(input("Enter the marks of Subject 2: "))
    s3 = float(input("Enter the marks of Subject 3: "))

    avg = get_average(s1, s2, s3)
    grade = get_letter_grade(avg)

    print(f"Average: {avg:.2f}")
    print(f"Letter Grade: {grade}")


main()

