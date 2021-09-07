# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:50:19 2020

@author: zudd2
"""
import numpy as np
import matplotlib.pyplot as plt

# NOTE: the program will take about 10-15 seconds to load all the graphs
# all the plt.savefig() commands were commented out since the program will not run 

# opening all files needed for graphs
content = open('EnergyConsumers.txt','r')
data = content.readlines() 

content1 = open('EnergyRawDataFinal.txt','r')
energyData = content1.readlines()

content3 = open('CarbonEmissions.txt', 'r')
emissions = content3.readlines()
   

##### setting up data to load into 2D array Consumers ######
# removes the top two rows
years = data[2].split('\t')
years.pop(0)   
for i in range(0,3):

    data.pop(0)

data0 = []
# makes each element into a nested list of data0
for row in data:
    sub = row.split(',')
    data0.append(sub)

# removes "\t" for each list    
data1 = []
for sublist in data0:
    for element in sublist:
        sub = element.split('\t')
        data1.append(sub)
        
countryNames = []
# removes country names from data1 and appends to seperate list
for sublist in data1:
    sublist.reverse()
    countryNames.append(sublist[-1])
    sublist.pop()
    sublist.reverse()
    
# removes \n for each list   
for sublist in data1:
    sublist[-1] = sublist[-1].strip()
    sublist[-1] = sublist[-1].strip()
    
# converts each element in list to float   
for sublist in data1:
    for i in range(0, len(sublist)):
        x = sublist[i]
        sublist[i] = float(x)



####### Plots for EnergyConsumers file #########
# code here makes histogram of consumption for each country
# also makes histogram of consumption for each year for all countries

consumers = np.array(data1) # 2D array with data from EnergyConsumeres.txt


def countryConsumption(x):
    """finds all the data for that country and creates a new list for it
    Parameters: takes in the index of the country"""
    countryData = consumers[x]
    return countryData



countryList = []
# loops over function countryConsumers and appends each row as its own list
for i in range(len(consumers)):
    countryList.append(countryConsumption(i))

  
    
# creates a histogram plot for the data of each country (alot of histograms)
# should be 44 graphs for each country
# 27 for each year

i = 0
for x in countryList:
    new = plt.figure()
    name = 'Energy Consumption for' +' '+ countryNames[i]
    plt.title(name)
    plt.xlabel('MTOE')
    plt.hist(x)
    #new.savefig('plots for consumers/' + countryNames[i] +' '+ 'graph.png') # saves all country graphs to folder
    i += 1

yearList = []
for i in range(len(years)):
    abc = []
    for x in range(len(countryList)):
        yearList.append(data1[x][i])
    new0 = plt.figure()
    name = 'Energy Consumption for All Countries in' +' '+ years[i]
    plt.title(name)
    plt.xlabel('MTOE')
    plt.hist(yearList)
    #if years[i] == '2016\n':
        #break
   # elif years[i] != '2016\n':
        #new0.savefig('plots for consumers/' + years[i]+' '+'graph.png')

    

# remove header
energyData.pop(0)

energy0 = []
# makes each row a nested list within energy0
for row in energyData:
    splt = row.split(',')
    energy0.append(splt)

# removes '\n' character from energy0
for sublist in energy0:
    sublist[-1] = sublist[-1].strip()
    sublist[-1] = sublist[-1].strip() 


########## Plots for EnergyRawDataFinal ########
# Compares the consumption of electricity and natural gas for each country in a histogram
# Compares the consumption of electricity and natural gas for each year for all countries using historgram
            
def energyFinder(name, Etype):
    """Finds all the values for either Electricity or Natural Gas based on country or year
    Parameters: name(country or year), Etype (energy type)"""
    energyList = []        
    for sublist in energy0:
        for element in sublist:
            if element == name: # condition finds all the values for given country/year
                if energy0[energy0.index(sublist)][2] == Etype: # condition finds all values for electricity or natural gas
                    listNum = energy0.index(sublist)
                    energyList.append(float(energy0[listNum][1]))    
    return energyList
    
e0 = 'Electricity' # variable used as parameter for energyFinder function
e1 = 'Natural Gas' # variable used as parameter for energyFinder function


# loops for each country in countryNames and uses each country as parameter for energyFinder function
for country in countryNames:
   new1 = plt.figure()
   label0 = 'Consumption for' +' '+ country +' '+ 'Histogram'
   plt.xlabel('Electricity/Natural Gas')
   plt.title(label0)
   plt.hist(energyFinder(country,e0), label = "Electricity")
   plt.hist(energyFinder(country,e1), label = "Natural Gas")
   plt.legend(loc = 'upper right')
   #new1.savefig('plots for Energytype/' +country +' '+ 'graph.png')
   

# loops for each year in years and uses each year as a parameter for energyFinder function
for year in years:
      new2 = plt.figure()
      label0 = 'Consumption of all countries in' +' '+ year +' ' +'Histogram'
      plt.title(label0)
      plt.xlabel('Electricity/Natural Gas')
      plt.hist(energyFinder(year,e0), label = "Electricity")
      plt.hist(energyFinder(year,e1), label = "Natural Gas")
      plt.legend(loc = 'upper right')
      #if year == '2016\n':
          #break
      #elif year != '2016\n':
          #new2.savefig('plots for Energytype/' +year+' '+'graph.png')
      
  
####### Plots using Ind array for each country and year ##########

# Made Ind a tuple of array consumers, the first index of tuple finds all values 
# up till 2000 and the second finds all values after 2000
Ind = consumers[0:44,0:11] , consumers[0:44, 11:27] 


percent0 = 0.15
percent1 = 0.35     
     
def indCountry(x,i,percent ):
    """finds the elements before or after 2000
    Parameters: x (row index of Ind), i (column index of Ind)"""
    usage = Ind[x][i] * percent
    return usage

# same as indCountry but uses 0:44 for first index since the function is finding 
# values for each year instead of country
def indYear(x,i,percent):
    usage = Ind[x][0:44,i] * percent
    return usage

# creates the graphs for each country before and after 2000
# alot of graphs since its for each country
for i in range(len(countryNames)):
    new3 = plt.figure()
    plt.xlabel('MTOE')
    label0 = 'Industrial Usage for' +' ' + countryNames[i]
    plt.title(label0)
    plt.hist(indCountry(0,i,percent0), label = "15%")
    plt.hist(indCountry(1,i,percent1),label = "35%")
    plt.legend(loc = 'upper left')
    #new3.savefig('plots for Ind/'+countryNames[i]+' '+'graph.png' )
    
# creates the graphs for all countries for each year
# alot of graphs
for i in range(len(years)):
    plt.figure()
    label1 = 'Industrial Usage for all countries in' +' '+ years[i] 
    plt.title(label1)
    plt.xlabel('MTOE')
    if i <= 10:
        plt.hist(indYear(0,i,percent0), label = "15%")
        plt.legend(loc = 'upperleft')
    elif i > 10:
        i -= 11 # subtracts 11 from index otherwise will go out of range
        plt.hist(indYear(1,i,percent1), label = "35%")
        plt.legend(loc = 'upper left')
        

############# Histogram of China only from Consumers ##########

plt.figure()
plt.xlabel("MTOE")
plt.title("Consumption of China only from Consumers Array")
plt.hist(countryList[26])

########## Histogram of Continents for Only Residential Usage ##############
# Since Residentual usage is opposite of Industrial, we will assume that
# 35% of total energy will be counted as Residentual up to 2000 and
# 15% of total energy will be counted as Residential after 2000
# we will also assume that Mexico is apart of south america and Austrailia is apart of Africa based 
# on their indexes in the EnergyConsumers.txt file


# Continent array. Each array will be sliced from consumers. Each slice is a continent. 
Continent = np.array([[consumers[0:18,0:27]],[consumers[18:20,0:27]],[consumers[20:26,0:27]]
                      ,[consumers[26:34,0:27]],[consumers[34:40,0:27]],[consumers[40:44,0:27]]])
 
# List of continent names that will be used for the titles of the plots       
continentList = ['Europe', 'North America', 'South America', 'Asia', 
                 'Africa','Middle East']

# function finds the array within continent array that is before and after 2000
# and computates 35% and 15% depending on the last index ([0:11] or [11:27])
def resContinent(x):
    thirtyFive = Continent[x][0][0][0:11] * 0.35
    fifteen = Continent[x][0][0][11:27] * 0.15
    return thirtyFive, fifteen

# loop creates a plot for each continent. Each continent will have 2 graphs: one for 35% and
# one for 15%
for i in range(len(continentList)): 
    cVal0, cVal1 = resContinent(i)
    new4 = plt.figure()
    plt.xlabel('MTOE')
    title0 = 'Residential Usage for' +' '+ continentList[i] +' '+ '(35%)'
    plt.title(title0)
    plt.hist(cVal0, label = '35%')
    new4.savefig('plots for residential/'+continentList[i]+'(35%)'+' '+'graph.png')
    new5 = plt.figure()
    plt.xlabel('MTOE')
    title1 = 'Residential Usage for' +' '+ continentList[i] +' '+ '(15%)'
    plt.title(title1)
    plt.hist(cVal1, label = '15%')
    #new5.savefig('plots for residential/'+continentList[i]+'(15%)'+' '+'graph.png')
      


########## double bar graph of Carbon Emissions vs Consumers 2015 ###########

### setting up data in CarbonEmissions.txt to be used here
emissions.pop(0)

eData = []
for row in emissions:
    Esplt = row.split(",")
    eData.append(Esplt)


eData0 = []
for sublist in eData:
    for element in sublist:
        sub = element.split('\t')
        eData0.append(sub)


# removes the rank and country from list 
# have seperate list for country names for double bar graph
Countries = []
for sublist in eData0:
    sublist.pop(0)
    Countries.append(sublist[0])
    sublist.pop(0)

# removes last 2 characters from each element, '\n'    
for sublist in eData0:
    sublist[-1] = sublist[-1].strip()
    sublist[-1] = sublist[-1].strip() 

# converts each element into float in eData0        
for sublist in eData0:
    for i in range(0, len(sublist)):
        x = sublist[i]
        sublist[i] = float(x)

# made another list so that it's not nested for conveniance
emissionsData = []
for sublist in eData0:
    for element in eData0:
        for a in element:
            emissionsData.append(a)
    break

N = len(Countries)
fig, ax = plt.subplots()

ind = np.arange(N)
width = 0.55

# list of all consumption values for 2015 for the 20 countries in CarbonEmissions.txt
consumption2015 = [consumers[26][25], consumers[19][25], consumers[27][25],consumers[15][25],
                   consumers[29][25], consumers[3][25], consumers[31][25], consumers[40][25],
                   consumers[18][25], consumers[42][25], consumers[21][25], consumers[24][25],
                   consumers[28][25], consumers[39][25], consumers[11][25],consumers[34][25],
                   consumers[4][25], consumers[13][25], consumers[2][25], consumers[6][25]]


p1 = ax.bar(ind, emissionsData, width, label = 'Carbon Emissions (million metric tons)')
p2 = ax.bar(ind + width, consumption2015, width, label = 'Consumption (MTOE)')

plt.xlabel('Countries (abbreviated)')
ax.set_xticks(ind + width / 2)

# labels for the graph, country names abbrieviated so names will not overlap in graph
ax.set_xticklabels(('CN', 'US', 'IO','RU', 'JP', 'DE','KR', 'IR', 'CA', 'SB',
                    'BR','MX', 'ID', 'SA', 'UK', 'AU', 'DE', 'TU', 'Fr', 'PL'))
plt.title('Carbon Emissions vs Consumption (2015) Double Bar Graph')
ax.legend(loc = 'upper right')

print('')
print('')
print('China and the United States appear to be the top two countries')
print('that use the most energy. The United States is located in North America')
print('While China is located in Asia.')
print('')
print('')


# should close all the files opened
content.close()
content1.close()
content3.close()

