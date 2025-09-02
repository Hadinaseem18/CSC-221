#programmingassignment3
#Muhammad Hadi Naseem
#09/26/2024


#input
burst_psi = float(input("Enter the rated bursting pressure of the boiler (psi):"))
current_psi = float(input("Enter the current (psi):"))






#process
max_safe_psi = burst_psi/3






#output
print(f"The maximum safe pressure is {max_safe_psi:.1f} psi.")
if current_psi < burst_psi/3:
    print("The current pressure is safe.")
else:
    print("WARNING! The current pressure is not safe.")

