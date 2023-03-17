SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE ADDRESS LIKE '강원도%'
ORDER BY FACTORY_ID ASC;

'''
# <아이스커피>로 시작하는 데이터 검색
SELECT * FROM TEST WHERE TITLE LIKE '아이스커피%';

# <아이스커피>로 끝나는 데이터 검색
SELECT * FROM TEST WHERE TITLE LIKE '%아이스커피';

# <아이스커피>가 들어가는 데이터 검색
SELECT * FROM TEST WHERE TITLE LIKE '%아이스커피%';
'''