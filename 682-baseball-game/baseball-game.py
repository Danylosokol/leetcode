class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for record in operations:
            if record.isdigit() or len(record) > 1:
                records.append(int(record))
            elif record == "+":
                if len(records) > 1:
                    records.append(records[-1] + records[-2])
            elif record == "D":
                records.append(records[-1]*2)
            elif record == "C":
                if len(records) >= 1:
                    records.pop()
            print(records)
            print("-----------")
        print(records)
        sum = 0
        for item in records:
            print("item:")
            print(item)
            sum += item
            print(sum)
        return sum