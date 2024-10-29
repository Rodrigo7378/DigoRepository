import time
import sys
import os

print("AIRCRAFT RFT (REMAINING FLIGHT TIME) CALCULATOR! ATTENTION, USE THIS UTILITY ONLY TO FLIGHT SIMULATION.")

def get_fuel_flow_choice():
    while True:
        fuel_flow_choice = input("TO START, CHOOSE YOUR FUEL FLOW MEASUREMENT SYSTEM. BETWEEN KG/M, KG/H, LB/M, or LB/H: ")
        if fuel_flow_choice.upper() in ["KG/M", "KG/H", "LB/M", "LB/H", "KGM", "KGH", "LBM", "LBH"]:
            return fuel_flow_choice.upper()
        else:
            print("Invalid choice. Please choose a valid fuel flow option.")

def get_fuel_remaining(fuel_flow_choice):
    while True:
        try:
            if fuel_flow_choice in ["KG/M", "KG/H", "KGM", "KGH"]:
                fuel_remaining = float(input("PLEASE INS ACT FUEL RE (KG): "))
                if 0 <= fuel_remaining <= 111000:
                    return fuel_remaining
                else:
                    print("Invalid input. Please enter a value between 0 and 111,000.")
            elif fuel_flow_choice in ["LB/M", "LB/H", "LBM", "LBH"]:
                fuel_remaining = float(input("PLEASE INS ACT FUEL RE (LB): "))
                if 0 <= fuel_remaining <= 245000:
                    return fuel_remaining
                else:
                    print("Invalid input. Please enter a value between 0 and 245,000.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_fuel_flow(fuel_flow_choice):
    while True:
        try:
            fuel_flow = float(input("INS ACT FF or EXPECTED FF. ATTENTION: IN YOUR MEASUREMENT SYSTEM YOU CHOOSE EARLIER: "))
            if fuel_flow_choice in ["KG/M", "KGM", "LB/M", "LBM"]:
                if 5 <= fuel_flow <= 1000:
                    return fuel_flow
                else:
                    print("Invalid input. Please enter a value between 5 and 100.")
            elif fuel_flow_choice in ["KG/H", "KGH", "LB/H", "LBH"]:
                if 5 <= fuel_flow <= 100000:
                    return fuel_flow
                else:
                    print("Invalid input. Please enter a value between 5 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_rft(fuel_remaining, fuel_flow, fuel_flow_choice):
    if fuel_flow == 0:
        print("Error: Fuel flow cannot be zero.")
        return None
    if fuel_flow_choice in ["KG/M", "LB/M", "KGM", "LBM"]:
        rft = fuel_remaining / fuel_flow
    elif fuel_flow_choice in ["KG/H", "LB/H", "KGH", "LBH"]:
        rft = (fuel_remaining / fuel_flow) * 60
    return rft

def main():
    fuel_flow_choice = get_fuel_flow_choice()
    fuel_remaining = get_fuel_remaining(fuel_flow_choice)
    fuel_flow = get_fuel_flow(fuel_flow_choice)
    rft = calculate_rft(fuel_remaining, fuel_flow, fuel_flow_choice)
    if rft is not None:
        print("Calculating RFT...", end="", flush=True)
        for i in range(5):  # adjust the number of iterations as needed
            sys.stdout.write("\r" + "|/-\\"[i % 4] + " Calculating RFT...")
            sys.stdout.flush()
            time.sleep(0.5)  # adjust the timeout as needed
        print(f"\n**IS THE ACT RFT FOR THE FLIGHT: {rft:.2f} MIN**")
        time.sleep(5)  # wait for 5 seconds
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
        print("ARCFT RFT CALC")  # reprint the header
        print("Also, visit my Github! Rodrigo7378 ")
        time.sleep(2)
        main()  # restart the program
if __name__ == "__main__":
    main()