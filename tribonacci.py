def tribonacci(signature, n):
    #your code here
    if n < 0:
        return
    elif n == 0:
        return []
    elif n == 1:
        return [signature[0]] #[1]
    elif n == 2:
        return [signature[0], signature[1]] #signature[2]
    else:
        a = signature[0]
        b = signature[1]
        c = signature[2]
        nl = [signature[0], signature[1], signature[2]]
        m = 3
        while m < n:
            s = a + b + c
            nl.append(s)
            a = b
            b = c
            c = s
            m += 1
            
        return nl
            
