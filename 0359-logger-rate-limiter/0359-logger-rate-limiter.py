class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns True if the message should be printed in the given timestap
        Otherwise, returns False.
        """
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp
            return True
        
        if timestamp - self._msg_dict[message] >= 10:
            self._msg_dict[message] = timestamp
            return True
        
        else:
            return False
# T : O(1) =? lookup and update of the hashtable takes a constant time.
# S : O(M)
        
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)