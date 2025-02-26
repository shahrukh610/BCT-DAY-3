sumofnaturalnumber = lambda n: 1 if(n==1) else(n+sumofnaturalnumber(n-1))
print(sumofnaturalnumber(6))