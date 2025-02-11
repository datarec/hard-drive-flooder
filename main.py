  GNU nano 8.2                                                               test.py                                                                        import time
import math


def main():
    try:
        byte_size = int(input("enter hard drive space: "))
        exponent = math.exp2(30) * byte_size
        confirm_attack = input("press y/n to confirm: ")
        if (confirm_attack == "y"):
            print("starting attack.")
            junk_data = "a" * (exponent)
            with open("log1.bin", "w") as f:
                f.write(junk_data)
            print("operation successful!")
        elif (confirm_attack == "n"):
            print("exiting...")
            exit()
    except TypeError:
        print("ERROR: please enter size in gb for hard-drive.")

if __name__ == "__main__":
    main()
