SELECT BOOK_ID, PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021 AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE ASC;