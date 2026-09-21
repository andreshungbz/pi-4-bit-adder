from time import sleep

from gpiozero import LED, Button  # type: ignore

# Define GPIO Inputs (LSB to MSB)
A = [Button(2), Button(3), Button(4), Button(17)]  # [A0 (LSB), A1, A2, A3 (MSB)]
B = [Button(27), Button(22), Button(10), Button(9)]  # [B0 (LSB), B1, B2, B3 (MSB)]

# Define GPIO Outputs
Sum_LEDs = [LED(11), LED(5), LED(6), LED(13)]  # [S0 (LSB), S1, S2, S3 (MSB)]
Carry_LED = LED(19)  # [C4]


def full_adder(a: int, b: int, cin: int) -> tuple[int, int]:
    """full_adder implements a 1-bit full adder logic."""
    sum_bit = a ^ b ^ cin
    cout = (a & b) | (cin & (a ^ b))
    return sum_bit, cout


def main() -> None:
    """Start the 4-bit binary adder program."""
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
