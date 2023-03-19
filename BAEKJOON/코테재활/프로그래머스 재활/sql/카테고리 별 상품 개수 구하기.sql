SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY ASC;

'''
<MySQL 문자열 부분 가져오기(LEFT, MID, RIGHT 함수)>

MySQL에서 문자열의 일부분을 가져오는 함수는 대표적으로 3가지가 있다.
* LEFT: 문자의 왼쪽을 기준으로 일정 갯수를 가져오는 함수
* MID: 문자의 지정한 시작 위치를 기준으로 일정 갯수를 가져오는 함수
* RIGHT: 문자의 오른쪽을 기준으로 일정 갯수를 가져오는 함수

참고로 MID 함수는 SUBSTR과 SUBSTRING 함수의 동의어이다.

LEFT(문자, 가져올 갯수)
MID(문자, 시작 위치, 가져올 갯수)
-- 또는 SUBSTR(문자, 시작 위치, 가져올 갯수);
-- 또는 SUBSTRING(문자, 시작 위치, 가져올 갯수);
RIGHT(문자, 가져올 갯수)

ex)
SELECT LEFT('abcdefg', 3)
> abc
'''