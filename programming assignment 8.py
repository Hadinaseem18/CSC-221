#programming assignment 8
#Muhammad Hadi Naseem
#11/2/2024


def main():
    amount=float(input("The amount invested:"))
    annual_interest_rate=float(input("Annual interest rate(e.g 0.09 means 9%:"))
    monthly_interest_rate= annual_interest_rate/12
    years=1
    print("Years\tFuture Value")
    while years<31:
        future_value=futureInvestmentValue( amount,monthly_interest_rate , years)
        print(f"{years}\t{future_value:.2f}")
        years=years+1
        
        
        

def futureInvestmentValue( amount,monthly_interest_rate , years):
    return amount * (1 + monthly_interest_rate) ** (years * 12)


main()
    
    
    
    
                               
