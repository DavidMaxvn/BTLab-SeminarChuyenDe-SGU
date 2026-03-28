CONTEXT: Bạn sẽ nhận được một đoạn mã Python cho bài quiz phép nhân.

TASK: Tìm bug logic và trả về phiên bản đã sửa.

CODE: {{{
import random

def multiplication_quiz():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    answer = input(f"What is {a} x {b}? ")

    if answer == a * b:
        print("Well done!")
    else:
        print("No.")

multiplication_quiz()
}}}

NEW_CODE:
import random

def multiplication_quiz():
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    answer = input(f"What is {a} x {b}? ")

    try:
        answer = int(answer)  # input() trả về chuỗi, cần ép sang số để so sánh đúng
    except ValueError:
        print("Please enter a valid number.")
        return

    if answer == a * b:
        print("Well done!")
    else:
        print("No.")

multiplication_quiz()

