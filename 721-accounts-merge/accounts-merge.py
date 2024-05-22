class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, n):
        p = self.par[n]

        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        
        return p
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)

        if px == py:
            return

        if self.rank[px] > self.rank[py]:
            self.par[py] = px
            self.rank[px] += self.rank[py]
        else:
            self.par[px] = py
            self.rank[py] += self.rank[px]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind(len(accounts))
        emails = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emails:
                    union.union(i, emails[email])
                else:
                    emails[email] = i

        merged_emails = defaultdict(list)
        for email, i in emails.items():
            leader = union.find(i)
            merged_emails[leader].append(email)

        result = []
        for i, emails in merged_emails.items():
            name = accounts[i][0]
            result.append([name] + sorted(emails))
        
        return result