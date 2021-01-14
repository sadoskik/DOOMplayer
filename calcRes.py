cap = 10**(-7)
R_a = 400
print("Previous R_b")
prevR_b = float(input())
print("Target frequency")
freq = float(input())
R_b = ((1.44/(freq*cap)) - R_a)/2
print("R_b needed: ")
print(R_b)
print("Difference: ")
print(R_b - prevR_b)