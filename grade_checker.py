def get_score():
    score = int(input("Enter your score: "))
    return score


def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def display_result(score, grade):
    print(f"Score: {score}")
    print(f"Grade: {grade}")


def main():
    score = get_score()
    grade = calculate_grade(score)
    display_result(score, grade)


if __name__ == "__main__":
    main()
