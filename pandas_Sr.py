import pandas as pd

# Q1

index_table = []
qty_table = []
while True:

    sr = pd.Series(qty_table, index = index_table)

    x = int(input("\n"
              "제품 수량 관리\n"
              "======================================================\n"
              "1. 입력   2. 출력   3. 검색   9. 종료 중에 메뉴를 선택하세요.\n"
              "======================================================\n"
              "입력 :"))
    if x == 9:
        break
    while True:
        if x == 1:
            a = input("제품명 : ")
            b = int(input("수량 : "))
            if a in index_table:
                u = qty_table[index_table.index(a)] + b
                qty_table.insert(qty_table[index_table.index(a)] + 1, u)
                del qty_table[index_table.index(a)]
                c = input("계속 입력 Y/N :")
                if c == 'N':
                    break
                else:
                    continue
            elif a not in index_table:
                index_table.append(a)
                qty_table.append(b)
                c = input("계속 입력 Y/N :")
                if c == 'N':
                    break
                else:
                    continue
            else:
                continue
        elif x == 2:
            print("\n"
                  "제품 수량 관리\n"
                  "======================================================\n"
                  "                 제품명  수량                   \n"
                  "======================================================\n"
                  "                ", sr)
            break


        elif x == 3:
            a = input("제품명: ")

            if a in sr:
                print("\n"
                      "제품 수량 관리\n"
                      "======================================================\n"
                      "                 제품명  수량                   \n"
                      "======================================================\n",
                      "                ",a ,"  ", sr[a])
                break
        else:
            break




# Series_실습문제.py


import pandas as pd

def series_lab01():
    sr = pd.Series([0], name='제품 데이터',
                   index = ['제품명'] )
    while True:
        print('제품수량관리')
        print('=' * 60)
        print('1. 입력 2. 출력 3.검색  9.종료 중에 메뉴를 선택하세요')
        print('=' * 60)

        menu = input('입력하세요  ->   ')
        menu = int(menu)

        if menu == 1:
            while True:
                name = input('제품명:')
                count = input('수량:')
                count = int(count)
                sr = sr.append(pd.Series([count], index=[name]))
                contin = input('계속 입력? Y/N')
                if contin == 'N' or contin == 'n':
                    break

        elif menu == 2:
            print('=' * 30)
            print('      제품명   수량')
            print('=' * 30)
            for idx, v in sr.items():
                print('%10s%10d' % (idx, v))

        elif menu == 3:
            name = input('제품명:')
            print('=' * 30)
            print('      제품명   수량')
            print('=' * 30)

            print('\t',sr[sr.index.str.contains(name)])

        elif menu == 9:
            print('종료합니다')
            break;

        else:
            pass


series_lab01()

# 2번
# 방법 1
def change_nan_by_mean_df():
    org_csv = 'WHO_first9cols.csv'
    new_csv = 'WHO_NoNaN.csv'
    df = pd.read_csv(org_csv)

    sr_null = pd.isnull(df).sum() # 결측치 수를 얻어서 출력
    print('[',org_csv,'결측치수]')
    print(sr_null)

    df = df.fillna(df.mean()) # 결측치를 평균값으로 변경

    df.to_csv(new_csv,index=False) # 새파일로 저장

    sr_null = pd.isnull(df).sum() # 결측치 수를 얻어서 출력
    print('[',new_csv,'결측치수]')
    print(sr_null)


change_nan_by_mean_df()

# 방법 2
def change_nan_by_mean_for_loop():
    org_csv = 'WHO_first9cols.csv'
    new_csv = 'WHO_NoNaN.csv'
    df = pd.read_csv(org_csv)
    sr = pd.isnull(df).sum()
    print('[',org_csv,'결측치수]')
    print(sr)  # 결측치 수를 출력

    for n in range(len(df.columns)) :
        if(sr[n]>0 and df[sr.index[n]].dtype != 'object' ):
            col_mean = df[sr.index[n]].mean()  # 컬럼의 평균값을 구한다
            # print(n,col_mean)
            df[sr.index[n]] = df[sr.index[n]].fillna(col_mean)

    df.to_csv(new_csv,index=False)

    df = pd.read_csv(new_csv)
    sr = pd.isnull(df).sum()
    print('[',new_csv,'결측치수]')
    print(sr)  # 결측치 수를 출력

# change_nan_by_mean_for_loop()