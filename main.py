from random import randint

n = 0
d = 0


while True:
    d = input("Which level do you want? Enter a number:\n1 - simple "
              "operations with numbers 2-9\n2 - integral sqares of 11-29\n")
    try:
        d = int(d)
    except:
        print("Incorrect format.")
        continue
    else:
        if d != 1 and d != 2:
            print("Incorrect format.")
            continue
        break
for _ in range(5):
    if d == 1:
        a, b, c = randint(2, 9), randint(2, 9), randint(1, 3)
        if c == 1:
            print(f"{a} * {b}")
            ans = 100
            while True:
                ans = input()
                try:
                    ans = int(ans)
                except:
                    print("Incorrect format.")
                    continue
                else:
                    if 4 < ans > 81:
                        print("Incorrect format.")
                        continue
                    print("Right!" if ans == a * b else "Wrong!")
                    if ans == a * b:
                        n += 1
                    break
        elif c == 2:
            print(f"{a} + {b}")
            ans = 100
            while True:
                ans = input()
                try:
                    ans = int(ans)
                except:
                    print("Incorrect format.")
                    continue
                else:
                    if 4 < ans > 18:
                        print("Incorrect format.")
                        continue
                    print("Right!" if ans == a + b else "Wrong!")
                    if ans == a + b:
                        n += 1
                    break
        elif c == 3:
            print(f"{a} - {b}")
            ans = 100
            while True:
                ans = input()
                try:
                    ans = int(ans)
                except:
                    print("Incorrect format.")
                    continue
                else:
                    if -7 < ans > 7:
                        print("Incorrect format.")
                        continue
                    print("Right!" if ans == a - b else "Wrong!")
                    if ans == a - b:
                        n += 1
                    break
        else:
            print("Warning: I just skipped an iteration.")
            continue
    else:
        a = randint(11, 29)
        print(f"{a}")
        ans = 0
        while True:
            ans = input()
            try:
                ans = int(ans)
            except:
                print("Incorrect format.")
                continue
            else:
                if 121 < ans > 841:
                    print("Incorrect format.")
                    continue
                print("Right!" if ans == a ** 2 else "Wrong!")
                if ans == a ** 2:
                    n += 1
                break
print(f"Your mark is {n}/5.Would you like to save the result? Enter yes or no")
if input() in ["yes", "YES", "y", "Yes"]:
    name = input("What is your name?\n")
    with open("results.txt", 'a', encoding='utf-8') as results:
        results.write(name + ": " + str(n) + "/5" + " in level " + (
            "1 - simple operations with numbers 2-9" if d == 1 else "2 - integral sqares of 11-29"))
    print("The results are saved in \"results.txt\"")
exit()
