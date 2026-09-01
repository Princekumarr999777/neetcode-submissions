class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.lru_dict={}
        

    def get(self, key: int) -> int:
        if key in self.lru_dict:
            value=self.lru_dict.pop(key)
            self.lru_dict[key]=value
            return value
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.lru_dict:
            self.lru_dict.pop(key)
        elif len(self.lru_dict) >= self.capacity:
            first_key=next(iter(self.lru_dict))
            self.lru_dict.pop(first_key)
        self.lru_dict[key] = value 



          
                

            
     