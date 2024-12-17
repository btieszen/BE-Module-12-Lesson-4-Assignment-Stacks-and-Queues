#Browsing History Management

class HistoryStack:
    def __init__(self):
        self.historys = []
        
    def add_history(self,history):
        #add ticket to top of stack
        self.historys.append(history)
    
    def delete_history(self):
        if not self.is_empty():
            return self.historys.pop()
    
    def is_empty(self):
        return len(self.historys) == 0

    def size(self):
        return len(self.historys)

    def display_historys(self):
        if self.is_empty():
            print("No Browser History")
        else:
            print("Browser History: ")
            for history in self.historys:
                print (f" Browser History Date:{history["Date"]}, Number of Pages: {history["pages"]}")

            
history_stack = HistoryStack()

history_stack.add_history({"Date":"12-12-2024","pages":25})
history_stack.add_history({"Date":"12-13-2024","pages":5})
history_stack.add_history({"Date":"12-14-2024","pages":45})

history_stack.display_historys()

deleted_history=history_stack.delete_history()
print(f"Deleted History: {deleted_history["Date"]}")

history_stack.display_historys()