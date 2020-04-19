import base64
from io import BytesIO

import matplotlib.pyplot as plt



# dates=['2020-04-12', '2020-04-12', '2020-04-13', '2020-04-13', '2020-04-13',
#        '2020-04-13', '2020-04-13', '2020-04-13', '2020-04-14', '2020-04-14', '2020-04-14', '2020-04-19']
#
#
#
# def all_list(arr):
#     result = {}
#     for i in set(arr):
#         result[i] = arr.count(i)
#     return result
#
# if __name__ == '__main__':
#     x_data = []
#     y_data = []
#     all=all_list(dates)
#     print(all)
#
#     for i in sorted(all.keys()):
#         print((i,all[i]))


    # for key in all.keys():
    #     print(key)
    #     x_data.append(key)
    # for va in all.values():
    #     print(va)
    #     y_data.append(va)
    # plt.plot(x_data,y_data,color='red',linewidth=2.0,linestyle='--')
    #
    # sio=BytesIO()
    # plt.savefig(sio,format='png')
    # data=base64.encodebytes(sio.getvalue()).decode()
    # print(data)




# def get_year(arr):
#     arr="2020-04-12"
#     year=arr.split('-',3)[0]
#     return year
#
# def get_month(arr):
#     arr="2020-04-12"
#     month=arr.split('-',3)[1]
#     return month
#
# def get_day(arr):
#     arr="2020-04-12"
#     day=arr.split('-',3)[2]
#     return day
#
# if __name__ == '__main__':
#     arr='2020-04-12'
#     year=get_year(arr)
#     month=get_month(arr)
#     day=get_day(arr)
#     print(year,month,day)

a=[1,1,3,2,3]
b=0
for i in a:
    b=b+i
print(b)