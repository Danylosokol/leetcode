class Solution:

    def sortByBits(self, arr: List[int]) -> List[int]:
        print(arr)
        n = len(arr)
    
        for i in range(n - 1):
            for j in range(n - i - 1):
                curr_item = arr[j]
                next_item = arr[j + 1]
                curr_item_count = curr_item.bit_count()
                next_item_count = next_item.bit_count()
                if curr_item_count > next_item_count:
                    print("swaping...")
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                elif curr_item_count == next_item_count and curr_item > next_item:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

