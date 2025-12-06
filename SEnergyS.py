"""
Smart Energy Saver - Simple CLI
Save this file as: smart_energy.py
Run: python smart_energy.py
"""

import random

# --------------------------
# Configuration / Simulated data
# --------------------------
# Hours per day each appliance is used (simulated)
appliance_usage = {
    "Air Conditioner": 6,    # hours/day
    "Television": 4,
    "Fridge": 24,
    "Washing Machine": 1
}

# Typical power ratings (kW)
appliance_power_kw = {
    "Air Conditioner": 1.5,   # 1500 W
    "Television": 0.1,        # 100 W
    "Fridge": 0.2,            # 200 W
    "Washing Machine": 0.5    # 500 W
}

# Unit cost (currency per kWh) — change to your local tariff
UNIT_COST = 60.0  # LKR per kWh (example)

# Simple list of tips
tips = [
    "Switch to LED bulbs to save 20–30% energy vs incandescent.",
    "Unplug chargers and small appliances when not in use (standby losses).",
    "Batch laundry so washing machine runs less often with full loads.",
    "Raise AC thermostat by 1–2°C to reduce compressor run-time.",
    "Use natural light during daytime when possible."
]

# --------------------------
# Helper functions
# --------------------------
def show_usage():
    """Print simulated daily usage for each appliance."""
    print("\nDaily appliance usage (simulated):")
    for app, hrs in appliance_usage.items():
        print(f" - {app}: {hrs} hours/day")
    print()

def suggest():
    """Print rule-based suggestions based on usage."""
    print("\nEnergy-saving suggestions:")
    # Rule: if AC > 5 hours/day
    if appliance_usage.get("Air Conditioner", 0) > 5:
        print(" → Air Conditioner runs often. Consider reducing to 4 hours/day or increasing setpoint.")
    # Rule: if TV > 3 hours/day
    if appliance_usage.get("Television", 0) > 3:
        print(" → Television usage is high. Reduce screen time or switch off when unattended.")
    # Rule: Washing machine used daily
    if appliance_usage.get("Washing Machine", 0) >= 1:
        print(" → Try to use full loads in the washing machine to avoid frequent small loads.")
    # Fridge tips (always on)
    print(" → Fridge runs 24/7. Keep the door closed and set temperature to recommended range (2–4°C).")
    print()

def calculate_weekly_cost():
    """Estimate weekly electricity cost using simulated usage and power ratings."""
    total_kwh = 0.0
    for app, hrs_per_day in appliance_usage.items():
        power_kw = appliance_power_kw.get(app, 0)
        weekly_kwh = power_kw * hrs_per_day * 7  # hours/day * 7 days
        total_kwh += weekly_kwh
    cost = total_kwh * UNIT_COST
    return total_kwh, cost

def show_cost():
    total_kwh, cost = calculate_weekly_cost()
    print("\nEstimated weekly consumption and cost (simulated):")
    print(f" - Estimated weekly energy: {total_kwh:.2f} kWh")
    print(f" - Estimated weekly cost: {cost:.2f} LKR (using {UNIT_COST} LKR/kWh)\n")

def show_tip():
    print("\nWeekly tip:")
    print(" →", random.choice(tips), "\n")

def apply_example_saving():
    """
    Show example of potential saving:
    For demonstration, assume applying suggestions reduces flexible loads by 10%.
    """
    total_kwh, cost = calculate_weekly_cost()
    after_kwh = total_kwh * 0.9
    after_cost = after_kwh * UNIT_COST
    saved = cost - after_cost
    print("\nIf you apply suggestions (example reduction = 10% of flexible loads):")
    print(f" - New weekly energy (example): {after_kwh:.2f} kWh")
    print(f" - New weekly cost (example): {after_cost:.2f} LKR")
    print(f" - Example weekly saving: {saved:.2f} LKR\n")

# --------------------------
# CLI Loop
# --------------------------
def main():
    print("Smart Energy Saver - CLI Demo")
    print("Type 'help' for commands.\n")

    while True:
        try:
            cmd = input("command> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Goodbye!")
            break

        if cmd in ("help", "?"):
            print("Commands:")
            print("  usage         - show simulated daily appliance usage")
            print("  suggest       - get rule-based energy saving suggestions")
            print("  cost          - show estimated weekly energy consumption & cost")
            print("  example_save  - show an example of potential savings after actions")
            print("  tip           - show one weekly tip")
            print("  set <app> <hours> - change simulated hours for an appliance (e.g. set \"TV 2\")")
            print("  apps          - list known appliances")
            print("  exit | quit   - quit the program\n")
        elif cmd == "usage":
            show_usage()
        elif cmd == "suggest":
            suggest()
        elif cmd == "cost":
            show_cost()
        elif cmd == "example_save":
            apply_example_saving()
        elif cmd == "tip":
            show_tip()
        elif cmd.startswith("set "):
            parts = cmd.split()
            if len(parts) >= 3:
                app_name = " ".join(parts[1:-1]).title()
                try:
                    hours = float(parts[-1])
                    if app_name in appliance_usage:
                        appliance_usage[app_name] = hours
                        print(f"Updated {app_name} to {hours} hours/day.\n")
                    else:
                        print(f"Unknown appliance: {app_name}. Use 'apps' to list.\n")
                except ValueError:
                    print("Invalid number of hours. Example: set \"TV 2\"\n")
            else:
                print("Usage: set <appliance name> <hours>\n")
        elif cmd == "apps":
            print("\nKnown appliances:")
            for a in appliance_usage:
                print(" -", a)
            print()
        elif cmd in ("exit", "quit"):
            print("Thank you for using Smart Energy Saver. Goodbye!")
            break
        elif cmd == "":
            continue
        else:
            print("Unknown command. Type 'help' for a list of commands.\n")

if __name__ == "__main__":
    main()

