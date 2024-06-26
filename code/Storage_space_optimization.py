import matplotlib.pyplot as plt         ###宣告引用插件
import matplotlib.patches as pc
import random

the_last_coordinate = []                ###宣告變數
frquency = 1
base_number = 250
A_probability = 10.57
B_probability = 35.65
C_probability = 31.58
D_probability = 16.10
E_probability = 4.56
F_probability = 1.36
G_probability = 0.16
commodity_height = [2,3,4,5,6,7,8]
num_x = 11
num_y = 6 * 8
arg_ = 0


def window(the_last_coordinate_):           ###定義matplotlib視窗
    plot_x = []
    plot_y = []
    axis = plt.figure(figsize=(30, 18))
    # plt.title("aa")
    ax1 = axis.add_subplot()
    plt.title("best storage = " + str(len(the_last_coordinate_)), fontsize=50)
    for x in range(num_x):
        plot_x.append(-x - 1)
    for y in range(num_y):
        plot_y.append(-y - 1)
    plt.xticks(ticks=plot_x, fontsize=50)
    plt.yticks(ticks=plot_y, fontsize=20)
    plt.grid(axis='x', linestyle="-.", linewidth=1, color='black')
    plt.grid(axis='y', linestyle="-.", linewidth=1, color='black')
    for i in range(len(the_last_coordinate_)):
        x_axis = the_last_coordinate_[i][0][0]
        y_axis = the_last_coordinate_[i][0][1]
        color_num = the_last_coordinate_[i][1]
        color = ["red", 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        ax1.add_patch(pc.Rectangle((-x_axis - 0.1, -y_axis), -1 + 0.2, color_num - 0.2, edgecolor='black',
                                   facecolor=color[color_num - 2]))
    plt.show()
    plt.close()


for i in range(100):            ###跑100筆資料做驗證
    commodity_number = []
    reward_coordinate = []
    current_rows = 0
    space = True
    for base_number_ in range(base_number):             ###依照順序將貨物入資料庫
        commodity_number.append(random.choices(commodity_height, weights=(A_probability,B_probability,
                                                                          C_probability,D_probability,
                                                                          E_probability,F_probability,
                                                                          G_probability))[0])
    for coordinate in range(num_x):             ###將大型貨物置頂
        the_highest_commodiry = max(commodity_number)
        the_highest_commodiry_corrdinate = commodity_number.index(the_highest_commodiry)
        reward_coordinate.append([[coordinate, 0], commodity_number.pop(the_highest_commodiry_corrdinate)])
    space = True
    for current_rows in range(num_x):
        current_grid = 1
        while (current_grid < (num_y-1)):
            if ((current_grid + commodity_number[0]) <= (num_y-1)):             ###按照順序入庫
                current_grid += commodity_number[0]
                reward_coordinate.append([[current_rows, current_grid], commodity_number.pop(0)])
            else:           ###若有剩餘空間做判斷
                if (current_rows != num_x-1):
                    remaining_space = (num_y-1) - current_grid
                    match remaining_space:
                        case 1:
                            reminding_space_ = reward_coordinate.pop(-1)[1]+1
                            commodity_number = [reminding_space_ - 1] + commodity_number
                            match reminding_space_:
                                case 2|3|4|5:
                                    current_grid = num_y-1
                                    reward_coordinate.append([[current_rows, current_grid], commodity_number.pop(commodity_number.index(reminding_space_))])
                                case 6:
                                    for i in range(2):
                                        current_grid -= 3
                                        reward_coordinate.append([[current_rows, current_grid], commodity_number.pop(commodity_number.index(3))])
                                case 7:
                                    for i in range(2):
                                        current_grid -= 3 + i
                                        reward_coordinate.append([[current_rows, current_grid],commodity_number.pop(commodity_number.index(3 + i))])
                        case 2|3|4|5:
                            current_grid = num_y-1
                            reward_coordinate.append([[current_rows, current_grid], commodity_number.pop(commodity_number.index(remaining_space))])
                        case 6:
                            for i in range(2):
                                current_grid -= 3
                                reward_coordinate.append([[current_rows, current_grid], commodity_number.pop(commodity_number.index(3))])
                        case 7:
                            for i in range(2):
                                current_grid -= 3 + i
                                reward_coordinate.append([[current_rows, current_grid], commodity_number.pop(commodity_number.index(3+i))])
                else:
                    current_grid = num_y-1

    if (frquency % 10 == 0):            ###每10筆資料紀錄
        the_last_coordinate.append(reward_coordinate)
        print("N" + str(frquency) + " = " + str(len(reward_coordinate)))
    arg_ += len(reward_coordinate)
    frquency += 1

print(int(arg_/100))
for i in range(10):             ###將入庫資料顯示
    window(the_last_coordinate[i])
