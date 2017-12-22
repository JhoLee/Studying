##p.29 순서도 실습 - 순차 3.1


sec_data=int(input("초를 입력하세요 >>  "))

hour = int(sec_data/(60*60))

sec = sec_data-hour*3600

minute = int(sec/60)

sec = sec - minute*60





print("%d초는 %d 시간 %d분 %d초" % (sec_data, hour, minute, sec))