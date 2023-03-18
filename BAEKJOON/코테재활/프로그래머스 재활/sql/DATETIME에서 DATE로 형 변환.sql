SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') AS '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

'''
<DATE_FORMAT>

DATE_FORMAT(날짜, 형식): 날짜를 지정한 형식으로 출력

%Y: 4자리 년도 %y: 2자리 년도
%M: 월(영문)  %m: 숫자 월 (2자리)
%D: 서수      %d: 숫자 일 (2자리)

'''