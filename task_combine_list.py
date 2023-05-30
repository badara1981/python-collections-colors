
#Task 1
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))




# Task 2
dic_1_color_names = {'red', 'green', 'blue'}

dic_2_color_hex = {'#FF0000','#00FF00', '#0000FF'}

def Merge(dict_1_color_names, dict_2_color_hex):
	result = dict_1_color_names | dict_2_color_hex
	return result
	
# Driver code
dict_1_color_names = {'red', 'green', 'blue' }
dict_2_color_hex = {'#FF0000' , '#00FF00' , '#0000FF'}
dict_3 = Merge(dict_1_color_names, dict_2_color_hex)
print(dict_3)

### Task - Combine lists into a dict


color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000','#00FF00', '#0000FF']
color_names_and_color_hex = dict(zip(color_names,color_hex))
#
names = ['Badara', 'Victor', 'Nadie', 'Felipe', 'Michel']
countries = ['Gambia', 'Sweden', 'Iran', 'columbia', 'Germany']

names_and_countries = dict(zip(names, countries))
print(names_and_countries)
