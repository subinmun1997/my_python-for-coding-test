SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
FROM ANIMAL_INS
WHERE ANIMAL_TYPE IN ('Cat', 'Dog')
GROUP BY ANIMAL_TYPE
ORDER BY FIELD(ANIMAL_TYPE, 'Cat', 'Dog');

'''
<FIELD>

어떤 특정 데이터의 값의 정렬을 우선으로 정해서 정렬하고 싶을 때 사용

ORDER BY FIELD (column, 1순위, 2순위, 3순위, n순위...)
'''