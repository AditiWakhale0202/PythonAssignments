# import/use all libraries here
# write all of your new functions in this file

# Do not change or modify this method prototype/signature
# Also do not modify current indentation

def findRemCust(saletime, cust, custArr):
    # Write your logic here
    timeleft = saletime
    time_passed= 0
    customer_served = 0
    for each_cust in custArr:
        if each_cust < 0:
            break
        wait_time = 0 if time_passed >=each_cust else each_cust-time_passed
        if timeleft>=wait_time+3:
            time_passed = time_passed + wait_time + 3
            timeleft = saletime - time_passed
            customer_served = customer_served + 1
        else:
            break
    customer_left = cust - customer_served
    return customer_left

print findRemCust(14,5,[0,0,3,4,2])


