"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, hourlyRate, hours, monthly, commissionType, landedContracts, contractAmount=0):
        self.name = name
        self.hourlyRate = hourlyRate
        self.hours = hours
        self.monthly = monthly
        self.commissionType = commissionType
        self.landedContract = landedContracts
        self.contractAmount = contractAmount

    def get_pay(self):
        
        if self.hourlyRate:
            pay = self.hourlyRate * self.hours
            if (self.commissionType == 'bonus'):
                pay += self.contractAmount
            elif (self.commissionType == 'contract'):
                pay += (self.landedContract * self.contractAmount)
            else:
                return pay
            return pay
        
        else:
            pay = self.monthly
            if (self.commissionType == 'bonus'):
                pay += self.contractAmount
            elif (self.commissionType == 'contract'):
                pay += (self.landedContract * self.contractAmount)
            else:
                return pay
            return pay

    def __str__(self):
        output = f"{self.name} works on a "

        if self.hourlyRate:
            output += (f"contract of {self.hours} hours at {self.hourlyRate}/hour")
        else:
            output += (f"monthly salary of {self.monthly}")

        if self.commissionType == "contract":
            output += (f" and recieves a commission for {self.landedContract} contract(s) at {self.contractAmount}/contract")
        elif self.commissionType == "bonus":
            output += (f" and recieves a bonus commission of {self.contractAmount}")

        output += (f".  Their total pay is {self.get_pay()}.")
        
        return output

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 0, 0, 4000, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 0, 0, 3000, "contract", 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 0, "contract", 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 0, 0, 2000, "bonus", 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 0, "bonus", 0, 600)