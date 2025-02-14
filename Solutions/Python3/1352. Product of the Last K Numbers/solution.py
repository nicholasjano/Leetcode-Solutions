class ProductOfNumbers:

    def __init__(self):
        self.curr_prefix_product = 1
        self.valid_prefix_products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.curr_prefix_product = 1
            self.valid_prefix_products = []
        else:
            self.curr_prefix_product *= num
            self.valid_prefix_products.append(self.curr_prefix_product)

    def getProduct(self, k: int) -> int:
        if len(self.valid_prefix_products) < k:
            return 0
        
        if len(self.valid_prefix_products) == k:
            return self.valid_prefix_products[-1]
        
        return self.valid_prefix_products[-1] // self.valid_prefix_products[-1 - k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)