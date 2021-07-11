import csv
import math
import matplotlib.pylab as plt

def retrieve_iris_file(irisfile):

    # put user input in a loop with a try/ except statement to catch input errors and allow user to try again
    while True:

        try:
            input_stream = open(irisfile, "r")       # creates a stream for the data
            break
        except FileNotFoundError:
            print("you did not enter the correct file name. Please enter an already existing .csv file(ex. epadata2003.csv)")
            print("#########################################################################################################\n")

            irisfile = input("please select the iris flower data that you would like to import:")
            print("#########################################################################################################\n")
    return input_stream
########################################################################################################################
def iris_list_creation(input_stream):

    iris_list = []           # creates a empty list to store mpg in
    line_count = 0          # counts how many lines have been read

    csv_reader = csv.reader(input_stream)       # the input stream is read by the csv library
    for line in csv_reader:
        #print(line)
        # the if statement skips the header line for the csv library
        if line_count < 1:
            line_count = line_count + 1
            continue
        else:
             iris_list.append((float(line[0]),float(line[1]),float(line[2]),float(line[3]),line[4]))  # puts the column into a tuplet, and appends to the list

        line_count = line_count + 1
    return iris_list
########################################################################################################################
def avg_values(iris_list):
    # created variables to count the ammount of times the values are added together
    avg_list_dic = {}
    count = 0
    versi_count = 0
    seto_count = 0
    virgin_count = 0

    # loop through every tuple in the list
    for tup in iris_list:
        # if count is zero, initalize a list to the different species of flower, this list can fit values needed for each attribute
        if count == 0:

            versi_list = [0.0, 0.0, 0.0, 0.0]
            seto_list = [0.0, 0.0, 0.0, 0.0]
            virgin_list = [0.0, 0.0, 0.0, 0.0]

            count += 1
        elif count > 0:
            # if the name of the iris is virginica, add the current tup values onto the previous
            if tup[4] == 'virginica':
                virgin_list[0] = virgin_list[0] + tup[0]
                virgin_list[1] = virgin_list[1] + tup[1]
                virgin_list[2] = virgin_list[2] + tup[2]
                virgin_list[3] = virgin_list[3] + tup[3]

                virgin_count += 1
            elif tup[4] == 'setosa':
                seto_list[0] = seto_list[0] + tup[0]
                seto_list[1] = seto_list[1] + tup[1]
                seto_list[2] = seto_list[2] + tup[2]
                seto_list[3] = seto_list[3] + tup[3]

                seto_count += 1
            elif tup[4] == 'versicolor':
                versi_list[0] = versi_list[0] + tup[0]
                versi_list[1] = versi_list[1] + tup[1]
                versi_list[2] = versi_list[2] + tup[2]
                versi_list[3] = versi_list[3] + tup[3]

                versi_count +=1
            count += 1


    # finds the average of the added values by dividing by the count of each added on value
    virgin_list[0] = virgin_list[0]/virgin_count
    virgin_list[1] = virgin_list[1]/virgin_count
    virgin_list[2] = virgin_list[2]/virgin_count
    virgin_list[3] = virgin_list[3]/virgin_count

    seto_list[0] = seto_list[0]/seto_count
    seto_list[1] = seto_list[1]/seto_count
    seto_list[2] = seto_list[2]/seto_count
    seto_list[3] = seto_list[3]/seto_count

    versi_list[0] = versi_list[0]/versi_count
    versi_list[1] = versi_list[1]/versi_count
    versi_list[2] = versi_list[2]/versi_count
    versi_list[3] = versi_list[3]/versi_count


    # creates a dictionary that stores the the list as a value, and the name of the iris as the key
    avg_list_dic['virginica'] = virgin_list
    avg_list_dic['setosa'] = seto_list
    avg_list_dic['versicolor'] = versi_list
    avg_list_dic['iriscount'] = {'versicolor':versi_count, 'setosa':seto_count, 'virginica':virgin_count}

    return(avg_list_dic)
########################################################################################################################
def std_deviation(iris_list, avg_list_dic, iris_species):

    # find the standard deviation
    values_list = []
    values_list2 = []
    values_list3 = []
    values_list4 = []
    sum_of_squares = [0,0,0,0]
    variance = [0,0,0,0]
    std_devi = [0,0,0,0,'']
    temp_list = []

    # take all the values and subtract the mean from each of the numbers
    # square each value to cause them to be positive numbers
    for have in iris_list:
        if have[4] == iris_species:
            temp_list.append(have)

    for iris in temp_list:
        values_list.append((iris[0] - avg_list_dic[iris_species][0]) ** 2) # appends the value list to a list
        values_list2.append((iris[1] - avg_list_dic[iris_species][1]) ** 2)  # appends the value list to a list
        values_list3.append((iris[2] - avg_list_dic[iris_species][2]) ** 2)  # appends the value list to a list
        values_list4.append((iris[3] - avg_list_dic[iris_species][3]) ** 2)  # appends the value list to a list

    value_list_holder = []
    value_list_holder = [values_list, values_list2, values_list3, values_list4]

    #find the sum of the squares
    for square in value_list_holder[0]:
        sum_of_squares[0] += square
    for square2 in value_list_holder[1]:
        sum_of_squares[1] += square2
    for square3 in value_list_holder[2]:
        sum_of_squares[2] += square3
    for square4 in value_list_holder[3]:
        sum_of_squares[3] += square4


    # divide by the number of values to find the variance
    variance[0] = sum_of_squares[0] / avg_list_dic['iriscount'][iris_species]
    variance[1] = sum_of_squares[1] / avg_list_dic['iriscount'][iris_species]
    variance[2] = sum_of_squares[2] / avg_list_dic['iriscount'][iris_species]
    variance[3] = sum_of_squares[3] / avg_list_dic['iriscount'][iris_species]

    # find the square root of the variance because of the earlier square
    std_devi[0] = math.sqrt(variance[0])
    std_devi[1] = math.sqrt(variance[1])
    std_devi[2] = math.sqrt(variance[2])
    std_devi[3] = math.sqrt(variance[3])

    return(std_devi)
########################################################################################################################
def find_min_max(iris_list, iris_species):

    # makes a attribute list that holds the minimum values of each attribute
    attribute_list_min = [0, 0, 0, 0]
    attribute_list_max = [0, 0, 0, 0]

    # temporary dict that will hold the atributes of the min and max values
    temp_dict = {'sepallength': [], 'sepalwidth': [], 'petallength': [], 'petalwidth': []}

    # uses this to just get list of the iris species that is in formal parameter
    for have in iris_list:
        if have[4] == iris_species:
            temp_dict['sepallength'].append(have[0])
            temp_dict['sepalwidth'].append(have[1])
            temp_dict['petallength'].append(have[2])
            temp_dict['petalwidth'].append(have[3])

    # take all appeneded species attributes for sepallength and test the
    for max in temp_dict['sepallength']:
        if max > attribute_list_max[0]:
            attribute_list_max[0] = max

    for max in temp_dict['sepalwidth']:
        if max > attribute_list_max[1]:
            attribute_list_max[1] = max

    for max in temp_dict['petallength']:
        if max > attribute_list_max[2]:
            attribute_list_max[2] = max

    for max in temp_dict['petallength']:
        if max > attribute_list_max[3]:
            attribute_list_max[3] = max

    # take all appeneded species attributes for sepallength and test the
    for min in temp_dict['sepallength']:
        if (min < attribute_list_min[0]) or (attribute_list_min[0] == 0):
            attribute_list_min[0] = min

    for min in temp_dict['sepalwidth']:
        if (min < attribute_list_min[1]) or (attribute_list_min[1] == 0):
            attribute_list_min[1] = min

    for min in temp_dict['petallength']:
        if (min < attribute_list_min[2]) or (attribute_list_min[2] == 0):
            attribute_list_min[2] = min

    for min in temp_dict['petalwidth']:
        if (min < attribute_list_min[3]) or (attribute_list_min[3] == 0):
            attribute_list_min[3] = min

    attribute_return_dic = {'sepallength': [attribute_list_max[0], attribute_list_min[0]], 'sepalwidth': [attribute_list_max[1], attribute_list_min[1]], 'petallength': [ attribute_list_max[2], attribute_list_min[2]], 'petalwidth': [attribute_list_max[3], attribute_list_min[3]]}

    return attribute_return_dic
########################################################################################################################
def print_iris_avg(avg_list_dic):

    # This just sets strings as variable to allows for formating
    species = 'species'
    setosa = 'setosa'
    versicolor = 'versicolor'
    virginica = 'virginica'

    avg_p_l = 'Average Petal Length:'
    avg_p_w = 'Average Petal Width:'
    avg_s_l = 'Average Sepal Length:'
    avg_s_w = 'Average Sepal Width:'


    # prints the avg_attributes in a 'pretty' table
    print(f"------------------------------------------------------------------------------------------------------------------------")
    print(f"{species:^30}|{setosa:^30}|{versicolor:^30}|{virginica:^30}")
    print(f"------------------------------------------------------------------------------------------------------------------------")
    print(f"{avg_p_l:^30}|{avg_list_dic[setosa][2]:^30.4f}|{avg_list_dic[versicolor][2]:^30.4f}|{avg_list_dic[virginica][2]:^30.4f}")
    print(f"{avg_p_w:^30}|{avg_list_dic[setosa][3]:^30.4f}|{avg_list_dic[versicolor][3]:^30.4f}|{avg_list_dic[virginica][3]:^30.4f}")
    print(f"{avg_s_l:^30}|{avg_list_dic[setosa][0]:^30.4f}|{avg_list_dic[versicolor][0]:^30.4f}|{avg_list_dic[virginica][0]:^30.4f}")
    print(f"{avg_s_w:^30}|{avg_list_dic[setosa][1]:^30.4f}|{avg_list_dic[versicolor][1]:^30.4f}|{avg_list_dic[virginica][1]:^30.4f}")
########################################################################################################################
def normalize_mean_data(avg_list_dic, iris_species_min_max, species):

    # sets variables to maximum values for each attribute for a ceratain species
    normalize_max_spl = iris_species_min_max['sepallength'][0]
    normalize_max_spw = iris_species_min_max['sepalwidth'][0]
    normalize_max_pl = iris_species_min_max['petallength'][0]
    normalize_max_pw = iris_species_min_max['petalwidth'][0]

    # sets variables to minimum values for each attribute for a ceratain species
    normalize_min_spl = iris_species_min_max['sepallength'][1]
    normalize_min_spw = iris_species_min_max['sepalwidth'][1]
    normalize_min_pl = iris_species_min_max['petallength'][1]
    normalize_min_pw = iris_species_min_max['petalwidth'][1]

    # sets variables to mean values for each attribute for a certain species
    normalize_avg_spl = avg_list_dic[species][0]
    normalize_avg_spw = avg_list_dic[species][1]
    normalize_avg_pl = avg_list_dic[species][2]
    normalize_avg_pw = avg_list_dic[species][3]

    # use normalization equation for each attrubute: sepal length, sepalwidth, petallength ect seperatly

    normalize_spl = {'max': [], 'mean': [], 'min': []}  # declares dict that will hold the normalized max, mean and min values

    # uses normalization equation x[normalized] = (x - x[min])/(x[max] - x[min])
    normalize_spl['max'].append((normalize_max_spl - normalize_min_spl) / (normalize_max_spl - normalize_min_spl))
    normalize_spl['mean'].append((normalize_avg_spl - normalize_min_spl) / (normalize_max_spl - normalize_min_spl))
    normalize_spl['min'].append((normalize_min_spl - normalize_min_spl) / (normalize_max_spl - normalize_min_spl))

    normalize_spw = {'max': [], 'mean': [], 'min': []}  # declares dict that will hold the normalized max, mean and min values

    normalize_spw['max'].append((normalize_max_spw - normalize_min_spw) / (normalize_max_spw - normalize_min_spw))
    normalize_spw['mean'].append((normalize_avg_spw - normalize_min_spw) / (normalize_max_spw - normalize_min_spw))
    normalize_spw['min'].append((normalize_min_spw - normalize_min_spw) / (normalize_max_spw - normalize_min_spw))

    normalize_pl = {'max': [], 'mean': [], 'min': []}   # declares dict that will hold the normalized max, mean and min values

    normalize_pl['max'].append((normalize_max_pl - normalize_min_pl) / (normalize_max_pl - normalize_min_pl))
    normalize_pl['mean'].append((normalize_avg_pl - normalize_min_pl) / (normalize_max_pl - normalize_min_pl))
    normalize_pl['min'].append((normalize_min_pl - normalize_min_pl) / (normalize_max_pl - normalize_min_pl))

    normalize_pw = {'max':[], 'mean':[], 'min':[]}  # declares dict that will hold the normalized max, mean and min values

    normalize_pw['max'].append((normalize_max_pw - normalize_min_pw) / (normalize_max_pw - normalize_min_pw))
    normalize_pw['mean'].append((normalize_avg_pw - normalize_min_pw) / (normalize_max_pw - normalize_min_pw))
    normalize_pw['min'].append((normalize_min_pw - normalize_min_pw) / (normalize_max_pw - normalize_min_pw))

    # make a dictionary to hold all values
    normalization = {'sepallength': normalize_spl, 'sepalwidth': normalize_spw, 'petallength': normalize_pl, 'petalwidth': normalize_pw, 'species':species}

    return normalization
########################################################################################################################
def print_summary_statistics(avg_list_dic, iris_norm, iris_list):

    # This just sets strings as variable to allows for formating
    species = 'species'
    setosa = 'setosa'
    versicolor = 'versicolor'
    virginica = 'virginica'
    petal_len = 'Average Petal Length:'
    petal_wid = 'Average Petal Width:'
    sepal_len = 'Average Sepal Length:'
    sepal_wid = 'Average Sepal Width:'
    std_dev = 'std:'
    mean = 'mean:'
    min = 'min:'
    max = 'max:'

    # call all functions to get needed values
    iris_list = iris_mean_data()

    # gets standard deviation values for each species
    std_seto = std_deviation(iris_list, avg_list_dic, setosa)
    std_versi = std_deviation(iris_list, avg_list_dic, versicolor)
    std_virgin = std_deviation(iris_list, avg_list_dic, virginica)

    # gets the maximum and minimum values for each attribute for each species
    seto_max_min = find_min_max(iris_list, setosa)
    versi_max_min = find_min_max(iris_list, versicolor)
    virgin_max_min = find_min_max(iris_list, virginica)

    # if iris_norm is not iris_norm then print the data table of specific values
    if iris_norm != 'iris_norm':
        # prints the avg_attributes in a 'pretty' table
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'species: Setosa':^30}||{petal_len:^30}||{petal_wid:^30}||{sepal_len:^30}||{sepal_wid:^30}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{std_dev:^30}||{std_seto[0]:^30.4f}||{std_seto[1]:^30.4f}||{std_seto[2]:^30.4f}||{std_seto[3]:^30.4f}|")
        print(f"|{mean:^30}||{avg_list_dic[setosa][0]:^30.4f}||{avg_list_dic[setosa][1]:^30.4f}||{avg_list_dic[setosa][2]:^30.4f}||{avg_list_dic[setosa][3]:^30.4f}|")
        print(f"|{min:^30}||{seto_max_min['sepallength'][1]:^30.4f}||{seto_max_min['sepalwidth'][1]:^30.4f}||{seto_max_min['petallength'][1]:^30.4f}||{seto_max_min['petalwidth'][1]:^30.4f}|")
        print(f"|{max:^30}||{seto_max_min['sepallength'][0]:^30.4f}||{seto_max_min['sepalwidth'][0]:^30.4f}||{seto_max_min['petallength'][0]:^30.4f}||{seto_max_min['petalwidth'][0]:^30.4f}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'species: Versicolor':^30}||{petal_len:^30}||{petal_wid:^30}||{sepal_len:^30}||{sepal_wid:^30}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{std_dev:^30}||{std_versi[0]:^30.4f}||{std_versi[1]:^30.4f}||{std_versi[2]:^30.4f}||{std_versi[3]:^30.4f}|")
        print(f"|{mean:^30}||{avg_list_dic[versicolor][0]:^30.4f}||{avg_list_dic[versicolor][1]:^30.4f}||{avg_list_dic[versicolor][2]:^30.4f}||{avg_list_dic[versicolor][3]:^30.4f}|")
        print(f"|{min:^30}||{versi_max_min['sepallength'][1]:^30.4f}||{versi_max_min['sepalwidth'][1]:^30.4f}||{versi_max_min['petallength'][1]:^30.4f}||{versi_max_min['petalwidth'][1]:^30.4f}|")
        print(f"|{max:^30}||{versi_max_min['sepallength'][0]:^30.4f}||{versi_max_min['sepalwidth'][0]:^30.4f}||{versi_max_min['petallength'][0]:^30.4f}||{versi_max_min['petalwidth'][0]:^30.4f}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'species: Virginica':^30}||{petal_len:^30}||{petal_wid:^30}||{sepal_len:^30}||{sepal_wid:^30}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{std_dev:^30}||{std_virgin[0]:^30.4f}||{std_virgin[1]:^30.4f}||{std_virgin[2]:^30.4f}||{std_virgin[3]:^30.4f}|")
        print(f"|{mean:^30}||{avg_list_dic[virginica][0]:^30.4f}||{avg_list_dic[virginica][1]:^30.4f}||{avg_list_dic[virginica][2]:^30.4f}||{avg_list_dic[virginica][3]:^30.4f}|")
        print(f"|{min:^30}||{virgin_max_min['sepallength'][1]:^30.4f}||{virgin_max_min['sepalwidth'][1]:^30.4f}||{virgin_max_min['petallength'][1]:^30.4f}||{virgin_max_min['petalwidth'][1]:^30.4f}|")
        print(f"|{max:^30}||{virgin_max_min['sepallength'][0]:^30.4f}||{virgin_max_min['sepalwidth'][0]:^30.4f}||{virgin_max_min['petallength'][0]:^30.4f}||{virgin_max_min['petalwidth'][0]:^30.4f}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    else:   #if iris_norm is normal
        seto_norm = normalize_mean_data(avg_list_dic, seto_max_min, setosa)
        versi_norm = normalize_mean_data(avg_list_dic, versi_max_min, versicolor)
        virgin_norm = normalize_mean_data(avg_list_dic, virgin_max_min, virginica)

        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'NORMALIZATION':^120}                                      |")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'species: Setosa':^30}||{petal_len:^30}||{petal_wid:^30}||{sepal_len:^30}||{sepal_wid:^30}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{min:^30}||{seto_norm['sepallength']['min'][0]:^30.4f}||{seto_norm['sepalwidth']['min'][0]:^30.4f}||{seto_norm['petalwidth']['min'][0]:^30.4f}||{seto_norm['petalwidth']['min'][0]:^30.4f}|")
        print(f"|{mean:^30}||{seto_norm['sepallength']['mean'][0]:^30.4f}||{seto_norm['sepalwidth']['mean'][0]:^30.4f}||{seto_norm['petalwidth']['mean'][0]:^30.4f}||{seto_norm['petalwidth']['mean'][0]:^30.4f}|")
        print(f"|{max:^30}||{seto_norm['sepallength']['max'][0]:^30.4f}||{seto_norm['sepalwidth']['max'][0]:^30.4f}||{seto_norm['petalwidth']['max'][0]:^30.4f}||{seto_norm['petalwidth']['max'][0]:^30.4f}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'species: Setosa':^30}||{petal_len:^30}||{petal_wid:^30}||{sepal_len:^30}||{sepal_wid:^30}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{min:^30}||{versi_norm['sepallength']['min'][0]:^30.4f}||{versi_norm['sepalwidth']['min'][0]:^30.4f}||{versi_norm['petalwidth']['min'][0]:^30.4f}||{versi_norm['petalwidth']['min'][0]:^30.4f}|")
        print(f"|{mean:^30}||{versi_norm['sepallength']['mean'][0]:^30.4f}||{versi_norm['sepalwidth']['mean'][0]:^30.4f}||{versi_norm['petalwidth']['mean'][0]:^30.4f}||{versi_norm['petalwidth']['mean'][0]:^30.4f}|")
        print(f"|{max:^30}||{versi_norm['sepallength']['max'][0]:^30.4f}||{versi_norm['sepalwidth']['max'][0]:^30.4f}||{versi_norm['petalwidth']['max'][0]:^30.4f}||{versi_norm['petalwidth']['max'][0]:^30.4f}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{'species: Setosa':^30}||{petal_len:^30}||{petal_wid:^30}||{sepal_len:^30}||{sepal_wid:^30}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"|{min:^30}||{virgin_norm['sepallength']['min'][0]:^30.4f}||{virgin_norm['sepalwidth']['min'][0]:^30.4f}||{virgin_norm['petalwidth']['min'][0]:^30.4f}||{versi_norm['petalwidth']['min'][0]:^30.4f}|")
        print(f"|{mean:^30}||{versi_norm['sepallength']['mean'][0]:^30.4f}||{versi_norm['sepalwidth']['mean'][0]:^30.4f}||{versi_norm['petalwidth']['mean'][0]:^30.4f}||{versi_norm['petalwidth']['mean'][0]:^30.4f}|")
        print(f"|{max:^30}||{versi_norm['sepallength']['max'][0]:^30.4f}||{versi_norm['sepalwidth']['max'][0]:^30.4f}||{versi_norm['petalwidth']['max'][0]:^30.4f}||{versi_norm['petalwidth']['max'][0]:^30.4f}|")
        print(f"----------------------------------------------------------------------------------------------------------------------------------------------------------------")
########################################################################################################################
#def iris_scatterplot(iris_list):





########################################################################################################################
def iris_mean_data():

    irisfile = input("please select the iris flower data that you would like to import:")
    iris_input_stream = retrieve_iris_file(irisfile)
    iris_list = iris_list_creation(iris_input_stream)
    avg_list_dic = avg_values(iris_list)
    print_iris_avg(avg_list_dic)

    return iris_list
def main():

    iris_list = iris_mean_data()
    avg_list_dic = avg_values(iris_list)

    print(iris_list)

    iris_norm = input("would you like to open table in data form or normalized data form?(data or normal?:")

    if iris_norm == 'normal':
        iris_norm = 'iris_norm'

    print_summary_statistics(avg_list_dic, iris_norm, iris_list)

    iris_scatterplot(iris_list)



main()