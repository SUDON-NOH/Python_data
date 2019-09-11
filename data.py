# Credit 사용에 주의해야 한다.

import pandas as pd
import googlemaps

df = pd.DataFrame()

x = pd.read_csv("daegeon_20190401_20190415.csv")
print("read csv")

x = x.drop(columns = ['timezn_cd','etl_ymd'])
x = x.groupby(['id','x', 'y'], as_index = False).sum()

print("x_groupby")

gmaps_key = ""
gmaps = googlemaps.Client(key = gmaps_key)

x["address"] = ""

print("start for sentence")

for i in range(len(x)):
    a = str(x['x'][i])
    b = str(x['y'][i])
    x1 = float('36.' + a)
    y1 = float('127.' + b)
    sample = gmaps.reverse_geocode((x1, y1), language = "ko")
    result = sample[0].get("formatted_address")
    x.loc[i, 'address'] = result
    if i % 1000 == 0:
        print('Step : ', i , '\naddress : ', x['address'][i])

print("End")

x.to_csv("Daejeon_address.csv", as_index = False)



# print(len(x))
#
# df4 = pd.DataFrame(columns=("lib", "qt1", "qt2"))
# print(df4)
#
#
# df4.loc[1, 5] = 1
# print(df4)
#
# df4.loc[2, 5] = 3
# print(df4)
# for i in range(5):
#     df4.loc[i] = [(i + 1) * (n + 1) for n in range(3)]
# print(df4)
