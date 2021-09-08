# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

conversion = {"M":1000000, "B":1000000000}

def update_damages(lst):
    new_damages = []
    for i in lst:
        if "B" in i:
           x =  conversion["B"]*float(i[:i.find("B")])
           new_damages.append(x)
        elif "M" in i:
            y = conversion["M"]*float(i[:i.find("M")])
            new_damages.append(y)
        elif i == "Damages not recorded":
            new_damages.append("Damages not recorded")
    return new_damages

new_damages = update_damages(damages)

# write your construct hurricane dictionary function here:
def construct_hurricane():
    hurricanes = {}
    for index in range(len(names)):
        empty_dic = {"Name":names[index],"Months":months[index],"Years":years[index],"max_sustained_winds":max_sustained_winds[index],"Areas Affected":areas_affected[index],"damages":new_damages[index],"Deaths":deaths[index]}
        hurricanes.update({names[index]:empty_dic})
    return hurricanes

hurricanes = construct_hurricane()
#print(hurricanes)
        
        






# write your construct hurricane by year dictionary function here:
def hurricane_by_year_dictionary(dictionary):
    years_dict = {}
    for i in dictionary.values():
        name = i.get("Name")
        month = i.get("Months")
        year = i.get("Years")
        max_sustained_wind = i.get("max_sustained_winds")
        area_affected = i.get("Areas Affected")
        damage = i.get("damages")
        death = i.get("Deaths")
        lstt = [name,month,year,max_sustained_wind,area_affected,damage,death]
        years_dict.update({year: lstt})
    return years_dict
        
       
yu2 = hurricane_by_year_dictionary(hurricanes)
#print(yu2)
# write your count affected areas function here:

def count_affected_areas(dict1):
    area_count = {}
    jay = []
    num = 0
    for i in dict1.values():
        areas = i.get("Areas Affected")
        for j in areas:
            jay.append(j)
        for c in jay:
            num = jay.count(c)
            area_count[c] = num
    return area_count   

yu3 = count_affected_areas(hurricanes)
#print(yu3)


# write your find most affected area function here:
def most_affected(dict2):
    num = []
    max_area = {}
    for i in dict2.keys():
        num.append(dict2[i])
    num1 = max(num)
    for key, value in dict2.items():
        if value == num1:
            max_area.update({key:value})
    return max_area   
        


yu4 = most_affected(yu3)
print(yu4)

# write your greatest number of deaths function here:
def greatest_death(dict3):
    new_hurricanes = {}
    greatest_deaths = {}
    num = []
    for i in dict3.values():
        names = i.get("Name")
        deaths = i.get("Deaths")
        new_hurricanes.update({names:deaths})
    for j in new_hurricanes.keys():
        num.append(new_hurricanes[j])
    new1 = max(num)
    for key, value in new_hurricanes.items():
        if value == new1:
            greatest_deaths.update({key:value})
    return greatest_deaths
        
    

yu5 = greatest_death(hurricanes)
print(yu5)






# write your catgeorize by mortality function here:
def mortality_hurricanes(dict4):
    mortality_hurricanes = {}
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    rating_hurricanes = {}
    for i in dict4.values():
        names = i.get("Name")
        deaths =  i.get("Deaths")
        mortality_hurricanes.update({names:deaths})
    for na, de in mortality_hurricanes.items():
        if de >0 and de<=100:
            one.append(na)
        elif de>100 and de <=500:
            two.append(na)
        elif de>500 and de <=1000:
            three.append(na)
        elif de>1000 and de<= 10000:
            four.append(na)
        elif de> 10000:
            five.append(na)
        else:
            zero.append(na)
    rating_hurricanes.update({0:zero,1:one,2:two,3:three,4:four,5:five})
    return rating_hurricanes
        
                
                
                
                
            

yu6 = mortality_hurricanes(hurricanes)
print(yu6)





# write your greatest damage function here:
def greatest_damage(dict5):
    biggest_damage={}
    empy_dic = {}
    num = []
    for i in dict5.values():
        names = i.get("Name")
        damages = i.get("damages")
        empy_dic.update({names:damages})
    for j in empy_dic.keys():
        if empy_dic[j] == "Damages not recorded":
            continue
        else:
            num.append(empy_dic[j])
    new1 = max(num)
    for key, value in empy_dic.items():
        if value == new1:
            biggest_damage.update({key:value})
    return biggest_damage
            
        
yu7 = greatest_damage(hurricanes)
print(yu7)




# write your catgeorize by damage function here:
def damages_hurricanes(dict6):
    do_hurricanes = {}
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    rating_hurricanes = {}
    for i in dict6.values():
        names = i.get("Name")
        damages =  i.get("damages")
        do_hurricanes.update({names:damages})
    for na, da in do_hurricanes.items():
        if da == "Damages not recorded":
            continue
        elif da >0 and da<=100000000:
            one.append(na)
        elif da>100000000 and da <=1000000000:
            two.append(na)
        elif da>1000000000 and da <=10000000000:
            three.append(na)
        elif da>10000000000 and da<= 50000000000:
            four.append(na)
        elif da> 50000000000:
            five.append(na)
        else:
            zero.append(na)
    rating_hurricanes.update({0:zero,1:one,2:two,3:three,4:four,5:five})
    return rating_hurricanes
        
                
                
                
                
            

yu8 = damages_hurricanes(hurricanes)
print(yu8)


    








