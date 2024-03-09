class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for record in operations:
            if record == "+":
                if len(records) > 1:
                    records.append(records[-1] + records[-2])
            elif record == "D":
                records.append(records[-1]*2)
            elif record == "C":
                if len(records) >= 1:
                    records.pop()
            else:
                records.append(int(record))
        return sum(records)