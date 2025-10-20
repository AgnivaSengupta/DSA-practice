# Satisfiability of Equality Equations
# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

class  DSU:
    def __init__(self)->None:
        self.parent = [i for i in range(26)]
        self.rank = [0]*26
        
    def find(self, x: int)->int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x:int, y:int)->None:
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return
            
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
            
        return 
        
def main():
    equations = ["a==b","b==a"]
    
    # the varaible are from a to b. So for DSU, we are using ASCII vals
    def satisfy(equations: list[str])->bool:
        n = len(equations)
        dsu = DSU()
        #  LOOP 1 to build the sets
        for eq in equations:
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            
            if eq[1] == eq[2]:  #meaning equals to: ==
                dsu.union(x, y)
            
            else:
                continue
        # LOOP 2 to check for inequalities
        for eq in equations:
            x = ord(eq[0]) - ord('a')
            y = ord(eq[3]) - ord('a')
            
            if eq[1] == '!':
                if dsu.find(x) == dsu.find(y):
                   return False
        return True 

    if satisfy(equations):
        print("Equation Satisfied!!")
    else:
        print("EQ not satisfied!")
        
if __name__ == "__main__":
    main()