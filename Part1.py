#Restaurant Order Management
#Task 1 Restaurant order queue

class OrderQueue:
    def __init__(self):
        self.orders=[]
        
    def post_orders(self,order):
        self.orders.append(order)
        
    def delete_order(self):
        if not self.is_empty():
            return self.orders.pop(0)
        
    def is_empty(self):
        return len(self.orders)==0
    
    def number_orders(self):
        return len(self.orders)
    
    def display_orders(self):
        if self.is_empty():
            print("There are no orders")
        else:
            print("Orders in queue:")
            for order in self.orders:
                print (f" Order Number:{order["Id"]}, Table: {order["table"]}, Order: {order["customerOrder"]}")
                
order_queue = OrderQueue()

order_queue.post_orders({"Id":"1", "table":"5", "customerOrder":"Ice Tea,Chesseburger,fries"})
order_queue.post_orders({"Id":"2", "table":"4", "customerOrder":"Coke,Chicken Salad, green beans"})
order_queue.post_orders({"Id":"3", "table":"10", "customerOrder":"Diet Coke,2 Chicken Tacos,rice and beans"})

order_queue.display_orders()

deleted_order=order_queue.delete_order()
print(f"Completed Order: {deleted_order["Id"]}")

order_queue.display_orders()
