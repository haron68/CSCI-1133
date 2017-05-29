with open('xcolors.txt', 'r') as file_colors:
    file_data_colors   = file_colors.read()

file_colorsCSV = open('xcolorsCSV.txt', 'w+')

file_data_colors = file_data_colors.replace(' \t', ' ').replace(' \t\t', '\n').replace('\t\t', '\n').replace(' \t', '\n').replace('\t', '').replace('     ', ' ').replace('   ', ' ').replace('  ', ' ')
file_colors = file_data_colors.split('\n')

xcolor_list      = []
xcolor_rgb_list  = []
xcolor_name_list = []

xcolor_r_list = []
xcolor_g_list = []
xcolor_b_list = []

for line in file_colors:
    xcolor_list.append(line)

for i in range(0, len(xcolor_list) - 1, 2):
    xcolor_rgb_list.append(xcolor_list[i])

for i in range(1, len(xcolor_list), 2):
    xcolor_name_list.append(xcolor_list[i])

for i in range(0, len(xcolor_rgb_list)):
    r = xcolor_rgb_list[i].split(' ')
    xcolor_r_list.append(r)

    if xcolor_r_list[i][0] == '':
        del xcolor_r_list[i][0]

    xcolor_r_list[i] = xcolor_r_list[i][0]

for i in range(0, len(xcolor_rgb_list)):
    g = xcolor_rgb_list[i].split(' ')
    xcolor_g_list.append(g)

    if xcolor_g_list[i][1] == '':
        del xcolor_g_list[i][1]

    xcolor_g_list[i] = xcolor_g_list[i][1]

for i in range(0, len(xcolor_rgb_list)):
    b = xcolor_rgb_list[i].split(' ')
    xcolor_b_list.append(b)

    if xcolor_b_list[i][2] == '':
        del xcolor_b_list[i][2]

    xcolor_b_list[i] = xcolor_b_list[i][2]

for i in range(0, len(xcolor_name_list)):
    r     = xcolor_r_list[i]
    g     = xcolor_g_list[i]
    b     = xcolor_b_list[i]
    names = xcolor_name_list[i]

    s = '{},{},{},{}{}'.format(r, g, b, names, '\n')
    file_colorsCSV.write(s)