import secp256k1 as ice
import random
from bitstring import BitArray
import time

print("Scanning Binary Sequence")

target_ori = "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16"

start= 21778071482940061661655974875633165533184 
end=   43556142965880123323311949751266331066367

file = open("data-base.bin", "rb")

dat = bytes(file.read())       
start_time = time.time()
while True:

    pk= random.randint(start, end)
    print(pk)
    
    target = ice.scalar_multiplication(pk)

    num = 24 

    sustract= 1 

    sustract_pub= ice.scalar_multiplication(sustract)

    res= ice.point_loop_subtraction(num, target, sustract_pub)
    
    binary = ''
    
    binary = ''.join('0' if int((res[t*65:t*65+65]).hex()[2:], 16) % 2 == 0 else '1' for t in range(num))
    
        
    my_str = binary

    b = bytes(BitArray(bin=my_str))
    
    
    
    if b  in dat:

        s = b
        f = dat
        inx = f.find(s)*sustract
        inx_0=inx
        Pk = (int(pk) + int(inx_0))+int(inx_0)*7
        A0 = ice.scalar_multiplication(Pk)
        A1 = A0.hex()
        if target_ori[2:] in A1:
            end_time = time.time()  
            search_time = end_time - start_time
            print("Found")
            B0 = ice.pubkey_to_address(0,1, A0)
            A2 = ice.to_cpub(A1)
            
            data = open("output.txt","a")
            data.write(f"Pk: {Pk}\n")
            data.write(f"cPub: {A2}\n")
            data.write(f"Addr: {B0}\n")
            data.write(f"Search Time: {search_time} seconds\n")
            data.close()
            file.close()
            break
        
        

   

    

    
