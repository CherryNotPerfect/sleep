import secp256k1 as ice
import random

print("Making random sustract Data-Base")

target_public_key = "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e16"

target = ice.pub2upub(target_public_key)

targets_num= 1000000

start= 21778071482940061661655974875633165533184 
end=   43556142965880123323311949751266331066367

for i in range(targets_num):

    A0 = random.randint(start, end)
    A1 = ice.scalar_multiplication(A0)
    A2= ice.point_subtraction(target, A1).hex()
    A3 = ice.to_cpub(A2)
    data = open("rand.txt","a")
    data.write(str(A3)+" "+"#"+str(A0)+"\n")
    data.close()
   
