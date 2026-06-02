class Solution(object):
    def generate(self, numRows):
        
        l1=[]
        for i in range(numRows):
            temp=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    temp.append(1)
                else:
                    temp.append(l1[i-1][j-1] + l1[i-1][j])
            l1.append(temp)
        return(l1)
        