SELECT B.WRITER_ID,
       U.NICKNAME,
       CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소,
       CONCAT(LEFT(TLNO, 3), '-', MID(TLNO, 4, 4), '-', RIGHT(TLNO, 4)) AS 전화번호
FROM USED_GOODS_BOARD AS B JOIN USED_GOODS_USER AS U
ON B.WRITER_ID = U.USER_ID
GROUP BY WRITER_ID
HAVING COUNT(*) >= 3
ORDER BY WRITER_ID DESC;

'''
<MySQL 여러 문자열을 하나의 문자열로 합치기>
CONCAT: 둘 이상의 문자열을 입력한 순서대로 합쳐서 반환해주는 함수

CONCAT(문자열1, 문자열2, [, 문자열3 ...])

ex)
SELECT CONCAT('안녕하세요.', '감사해요.', '잘있어요.', '다시만나요.')
-- 안녕하세요.감사해요.잘있어요.다시만나요.

띄어쓰기가 필요하다면 (' ')를 넣어줘야 한다.
ex)
SELECT CONCAT('안녕하세요.', ' ', '감사해요.', ' ', '잘있어요.', ' ', '다시만나요.')
-- 안녕하세요. 감사해요. 잘있어요. 다시만나요.
'''