SELECT H.FLAVOR
FROM FIRST_HALF AS H JOIN ICECREAM_INFO AS I
ON H.FLAVOR = I.FLAVOR
WHERE H.TOTAL_ORDER > 3000 AND I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY H.TOTAL_ORDER DESC;