import numpy
import random
#Creating a numpy array with all zeros as its elements
groupa=numpy.zeros((1000,2))
groupb=numpy.zeros((1000,2))

# Generating a 1000 random numbers in a normal distribution and storing them in groups
groupa[:,0]=numpy.random.normal(1,0.5,1000)
groupb[:,0]=numpy.random.normal(1,0.5,1000)


totalmarried=[]
#sampling the data in the group 
for i in range(0,100000):
    married=0.0
    a=0
    b=0
    #generate a sudo random number between 0 and 999 which would act as the index for groupa and groupb
    a=random.randint(0,999)
    b=random.randint(0,999)

    #Check if the flag for both indices is 0 i.e they havent been married yet
    if groupa[a][1] == 0 and groupb[b][1] ==0:

        #Check if the salary of the person in groupa is greater than that of the person in groupb
        if (groupa[a][0]>groupb[b][0]):

            #If both conditions are true increment the number of married people and flag then as 1 i.e. they cannot be paired anymore
            married=married + 1.0
            groupa[a][1]=1
            groupb[b][1]=1
    totalmarried.append(married)

#print the average number of married people over all iterations 
print numpy.sum(totalmarried)/1000*100

