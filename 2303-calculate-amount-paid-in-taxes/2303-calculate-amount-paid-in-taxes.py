class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        if income == 0:
            return 0.0
        
        total_tax = 0.0
        prev_upper = 0.0

        for upper, percent in brackets:
            tax_amount = min(upper, income) - prev_upper
    
            if tax_amount > 0:
                total_tax += tax_amount * percent / 100
            else:
                break
        
            prev_upper = upper

        return total_tax

        


            