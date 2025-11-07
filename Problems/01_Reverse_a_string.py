# String reversal 

class String:
    
    def reversal(self):
        """This class reverse the string."""
        self.string = input("Enter the string you want to reverse: ")
        self.length = len(self.string)
        
        # reverse the text
        i = self.length -1
        while i >= 0:
            print(self.string[i], end="")
            i -= 1
        
s = String()
s.reversal()
