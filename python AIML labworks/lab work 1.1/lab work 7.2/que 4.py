def sum_digits(n):
    if n<10:                     #single digit mil gya :- ruk jao
        return n
    return sum_digits(sum(int(d)for d in str(n)))
    #str(n):- number ko string banaya
    #int(d):- har digit ko num banaya
    #sum():- sab digits add
    
print(sum_digits(987))