SELECT ANIMAL_TYPE, IFNULL(NAME, "No name") AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID ASC;

'''
<IFNULL>
해당 column의 값이 null을 반환할 때, 다른 값으로 출력할 수 있도록 하는 함수

SELECT IFNULL(column명, "null일 경우 대체 값") FROM 테이블명;

<CASE>
해당 column 값을 조건식으로 통해 True, False를 판단하여 조건에 맞게 column 값을 변환할 때
사용하는 함수

CASE
    WHEN 조건식1 THEN 식1
    WHEN 조건식2 THEN 식2
    ...
    ELSE 조건에 맞는 경우가 없을 경우 실행할 식
END

ex)
# NAME Column의 IS NULL 조건이 True인 경우 "No name" 출력
# WHEN 조건들에 True인 조건이 없을 경우 ELSE 문을 통해 NAME Column의 값 출력
#END 이후 그 Column의 별칭을 NAME으로 지정

SELECT
    CASE
        WHEN NAME IS NULL THEN "No name"
        ELSE NAME
    END AS NAME
FROM ANIMAL_INS

'''