#Function representing exponentiation approximation formula
def exponentiation(num_people, num_days=365):
    #Probability of no match for each pair
    probability_of_no_match = (num_days - 1) / num_days
    #Calculate number of pairs
    num_pairs = num_people * (num_people - 1) / 2
    #Determine overall probability of no match occurring by raising probability of no match to the number of pairs
    overall_probability_of_no_match = probability_of_no_match**num_pairs
    #Subtract probability from 1 to find probability of match occurring
    probability_of_match = 1 - overall_probability_of_no_match
    #Return result when functino is called
    return probability_of_match

#Calls function with 23 random people
print(exponentiation(23))

#Print output: 0.5004771540365807

#Importing the math module for factorial function
import math

#Create function to calculate using factorial equation
def factorial_equation(num_people, num_days = 365):
    #Compute nummerator
    numerator = math.factorial(num_days)
    #Compute denominator
    denominator = math.factorial(num_days - num_people) * num_days**num_people
    #Calculate probability of no match
    probability_no_match = numerator / denominator
    #Calculate probability of match occurring
    probability_match = 1 - probability_no_match
    #Return probability of match whenever function is called
    return probability_match

#Calls and prints result when function is given 23 as the number of people
print(factorial_equation(23))

#Print output: 0.5072972343239854

#Import necessary functions
from random import seed
from random import randint

#Since computers only work in pseudo-random numbers, we can set a seed to have replicable results
#42 is my preferred number (see The Hitchhiker's Guide to the Galaxy for context)
seed(42)

#Function to build 10,000 random sets and calculate percentage that have a duplicated birthday
def perc_matches(num_people, num_days = 365, num_iterations = 10000):
    #This creates a list of lists that is num_iterations long
    #Each list contains num_people number of randomm numbers with num_days as the amount of integers to chose from
    random_selections = [[randint(0,num_days) for i in range(0,num_people)] for x in range(0,num_iterations)]
    #Initiates count of matches
    matches = 0
    #For each list in the list of lists
    for i in random_selections:
        #If the lenght of the list is different than the length of the set of items in the list
        #the list must have duplicated items.
        if len(i) != len(set(i)):
            #When duplicated items appear in the list, the number of matches increases by 1
            matches += 1
    #Number of lists with duplicated items is divided by number of lists to give percentage of list with duplicated birthdays
    perc = matches / num_iterations
    #Returns computed percentage
    return perc

#Prints result of function call when 23 people are given to the function.
print(perc_matches(23))

#Print output: 0.5131

#Import Pandas to work with dataframes
import pandas as pd

#Initiate dataframe with column names
df = pd.DataFrame(columns = ["Number of People", "Exponentiation Approximation", "Factorial Equation", "Coded Output"])

#Loop to feed teh functions every number from 1-70
#70 is where the probability hits 99.9%, and computing much higher makes this code run very slowly
for i in range(1,71):
    #Calls the functions for each number and adds the results to the dataframe
    df.loc[i] = [i, exponentiation(i), factorial_equation(i), perc_matches(i)]

#Exports the dataframe as a CSV for use in other code and visualizations in future posts. :)
df.to_csv("birthday_problem.csv", index=False)