import math

def main():
    G = 6.6743e-11
    M = input("Do you want to use the default mass of the Earth (597.2e24 kg)? (y/n): ")
    if M == "y":
        M = 5.972e+24
    else:
        M = int(input("Enter custom mass in kilograms: ").strip('kg').strip('kilograms'))
    R = int(input("What is the distance from the center of mass in meters?: ").strip('m').strip('meters'))
    escape_velocity = int(((2*G*M)/R)**0.5)
    print(escape_velocity)

main()
