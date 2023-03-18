SELECT COUNT(USER_ID)
FROM USER_INFO
WHERE DATE_FORMAT(JOINED, '%Y') = '2021'
-- WHERE YEAR(JOINED) = 2021
AND AGE BETWEEN 20 AND 29;

'''
<BETWEEN>

날짜 혹은 범위의 데이터를 조회할 때 범위를 설정하고 싶을 때 사용

컬럼명 BETWEEN 시작범위 AND 종료범위

<날짜 데이터에서 일부만 추출하기>

YEAR: 연도 추출
MONTH: 월 추출
DAY: 일 추출
HOUR: 시 추출
MINUTE: 분 추출
SECOND: 초 추출

ex)
YEAR(기준 날짜)
'''