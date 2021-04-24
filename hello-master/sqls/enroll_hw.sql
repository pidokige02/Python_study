-- plan 1 : 과목별로 랜덤 학생들 배정 -> 문제점: 랜덤으로 추출된 학생이 고정 됨! (이미 추출한 학생들을 대상으로 과목이 선정되므로)
select sbj.id, sbj.name, s.id
  from Subject sbj, (select id from Student order by rand() limit 3) s order by sbj.id;
  
-- plan 1' : plan1을 과목별로 한과목씩 실행시킴! (배정받은 과목은 제외)
insert into Enroll(subject, student)
select sbj.id, s.id
  from (select id from Subject where id not in (select distinct subject from Enroll) order by id limit 1) sbj, 
       (select id from Student order by rand() limit 100) s;
       

-- ----------------------------------------------------------------------------------------

-- plan 2: 모든학생이 적어도 한과목은 수강하며, 한 학생은 최대 3과목까지 수강한다면!!
insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by id;

insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;
 
insert into Enroll(student, subject)
 select id, (select id from Subject order by rand() limit 1) sid from Student order by rand() limit 500
 on duplicate key update student = student;



