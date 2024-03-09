class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        history = []
        for item in s:
            if item in valid_pairs:
               history.append(item)
            elif len(history):
                last_in_history = history.pop()
                if item != valid_pairs[last_in_history]:
                    return False
            else:
                return False
        return not history
        