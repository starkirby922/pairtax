import math
import pytest
from unittest import mock
import builtins

allowance = 132000

def func():
    x, y = input("Input self and spouse income: ").split()
    income=int(x)
    income2=int(y)

    if income*0.05>18000:
        mpf=18000
    else:
        mpf=income*0.05

    netincome= income - mpf - allowance



    first = netincome*0.02
    if first >1000:
        first = 1000
    elif first <0:
        first = 0

    second = (netincome-50000)*0.06
    if second > 3000:
        second = 3000
    elif second <0:
        second = 0

    third = (netincome-100000)*0.1
    if third > 5000:
        third = 5000
    elif third<0:
        third = 0 

    fourth = (netincome - 150000)*0.14
    if fourth > 7000:
        fourth = 7000
    elif fourth <0:
        fourth = 0 

    remainder = (netincome - 200000) *0.17
    if remainder <0:
        remainder = 0


    if income < 2022000:
        tax= first + second + third + fourth + remainder
        tax=math.floor(tax)
        print ("Self Tax Payable:"+str(tax) )
    else:
        tax = (netincome+132000)*0.15
        tax=math.floor(tax)
        print ("Self Tax Payable* Standard Rate:"+str(tax) )








    if income2*0.05>18000:
        mpf2=18000
    else:
        mpf2=income2*0.05

    netincome2= income2 - mpf2 - allowance

    first2 = netincome2*0.02
    if first2 >1000:
        first2 = 1000
    elif first2 <0:
        first2 = 0

    second2 = (netincome2-50000)*0.06
    if second2 > 3000:
        second2 = 3000
    elif second2 <0:
        second2 = 0

    third2 = (netincome2-100000)*0.1
    if third2 > 5000:
        third2 = 5000
    elif third2<0:
        third2 = 0 

    fourth2 = (netincome2 - 150000)*0.14
    if fourth2 > 7000:
        fourth2 = 7000
    elif fourth2 <0:
        fourth2 = 0 

    remainder2 = (netincome2 - 200000) *0.17
    if remainder2 <0:
        remainder2 = 0



    if income2 < 2022000:
        tax2= first2 + second2 + third2 + fourth2 + remainder2
        tax2=math.floor(tax2)
        print ("Spouse tax payable is:"+str(tax2) )
    else:
        tax2 = (netincome2+132000) * 0.15
        tax2=math.floor(tax2)
        print ("Spouse tax payable is*Standard Rate:"+str(tax2) )




    netincome3 = netincome + netincome2
    first3 = netincome3*0.02
    if first3 >1000:
        first3 = 1000
    elif first3 <0:
        first3= 0

    second3 = (netincome3-50000)*0.06
    if second3 > 3000:
        second3 = 3000
    elif second3 <0:
        second3 = 0

    third3 = (netincome3-100000)*0.1
    if third3 > 5000:
        third3 = 5000
    elif third3<0:
        third3 = 0 

    fourth3 = (netincome3 - 150000)*0.14
    if fourth3 > 7000:
        fourth3 = 7000
    elif fourth3 <0:
        fourth3 = 0 

    remainder3 = (netincome3 - 200000) *0.17
    if remainder3 <0:
        remainder3 = 0

    
    tax3= first3 + second3 + third3 + fourth3 + remainder3
    tax3=math.floor(tax3)
    
    stdtax3 = (netincome3+264000)* 0.15
    stdtax3=math.floor(stdtax3)
    if stdtax3>=tax3:
        lsstax3=tax3
        print ("Joint Assestment Tax Total:"+str(lsstax3))
    elif stdtax3<=tax3:
        lsstax3=stdtax3
        print ("Joint Assestment Tax Total*Standard Rate:"+str(lsstax3))



    seperatetotal = tax +tax2
    print ("Seperate Assestment Tax Total:"+str(seperatetotal))

    if seperatetotal < lsstax3:  
        print("Seperate Assestment Recommended")
    elif seperatetotal>lsstax3:
        print("Joint Assestment Recommended")
    else:
        print("Either Assestment is Recommended")

    return [seperatetotal, lsstax3]

if __name__ == '__main__':
    func()
