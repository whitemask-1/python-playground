from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for num in nums:
            new_nums_list = nums.copy()
            new_nums_list.remove(num)
            product = 1
            for n in new_nums_list:
                product *= n
            products.append(product)
        return products

# First instict was the for each number in the array we would need to multiply all remaining nums after removing the num from the list
# The way to do this was to create a products list for the final list to return at the end so that we can append it throughout the for loop
# Then for each number in the list create a new list as a copy of the input number list and then remove the number value
# Initialize a product variable to append as we multiply through the new list
# Then for each number in the new list multiply by the product, afterwards append said product to the final product list
# Then return products at the end when all numbers have been cycled through the first for loop
