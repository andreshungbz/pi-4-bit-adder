from time import sleep

from gpiozero import LED, Button  # type: ignore

# Define GPIO Inputs (LSB to MSB)
A = [Button(2), Button(3), Button(4), Button(17)]
B = [Button(27), Button(22), Button(10), Button(9)]

# Define GPIO Outputs
Sum_LEDs = [LED(11), LED(5), LED(6), LED(13)]
Carry_LED = LED(19)


def full_adder(a: int, b: int, cin: int) -> tuple[int, int]:
    sum_bit = a ^ b ^ cin
    cout = (a & b) | (cin & (a ^ b))
    return sum_bit, cout


def main() -> None:
    print("4-Bit Binary Adder Ready. Press switches to perform addition...")

    try:
        while True:
            cin = 0
            for i in range(4):
                a_val = int(A[i].value)
                b_val = int(B[i].value)

                s_out, cin = full_adder(a_val, b_val, cin)

                if s_out:
                    Sum_LEDs[i].on()
                else:
                    Sum_LEDs[i].off()

            if cin:
                Carry_LED.on()
            else:
                Carry_LED.off()

            sleep(0.05)
    except KeyboardInterrupt:
        print("\nProgram terminated.")


if __name__ == "__main__":
    main()
