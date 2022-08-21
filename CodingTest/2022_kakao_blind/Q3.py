def cal_time(in_time, out_time):
    return (int(out_time[:2]) - int(in_time[:2])) * 60 + int(out_time[3:]) - int(in_time[3:])


def solution(fees, records):
    answer = []
    car_info = []

    for rec in records:
        time = rec[:5]
        car_num = int(rec[6:10])
        state = rec[11:]

        if state == "IN":  # 입차
            isin = False
            for i in range(len(car_info)):
                if car_num == car_info[i][0]:
                    isin = True
                    car_info[i][1] = time
                    car_info[i][2] = False
                    break
            if not isin:
                car_info.append([car_num, time, False, 0])

        else:  # 출차
            for i in range(len(car_info)):
                if car_num == car_info[i][0]:
                    car_info[i][3] += cal_time(car_info[i][1], time)
                    car_info[i][1] = time
                    car_info[i][2] = True
                    break

    car_info.sort()

    for car in car_info:
        if not car[2]:
            car[3] += cal_time(car[1], "23:59")

        if car[3] <= fees[0]:
            answer.append(fees[1])
        else:
            additional = (car[3] - fees[0]) / fees[2]
            if additional == int(additional):
                additional = int(additional)
            else:
                additional = int(additional) + 1
            answer.append(fees[1] + additional * fees[3])

    return answer