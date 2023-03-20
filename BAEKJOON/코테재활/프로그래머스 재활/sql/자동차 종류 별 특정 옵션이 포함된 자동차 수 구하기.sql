SELECT CAR_TYPE, COUNT(CAR_ID) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS REGEXP "통풍시트|열선시트|가죽시트"
GROUP BY CAR_TYPE
ORDER BY CAR_TYPE ASC;

'''
<MySQL 정규 표현식 REGEXP>

REGEXP는 LIKE를 이용한 검색과 달리 정규 표현식을 이용해 검색한다.

|(수직선): 또는(OR)의 의미로 구분된 문자에 해당하는 문자열을 찾음
"데이터1|데이터2|데이터3"과 같이 데이터1 또는 데이터2 또는 데이터3에 해당하는 문자열을 찾음

나머지도 필요할 때 찾아보기
'''