START TRANSACTION;

create table Grade(
    id int unsigned not null auto_increment primary key,
    enroll int unsigned not null,
    midterm tinyint unsigned not null default 0,
    finalterm tinyint unsigned not null default 0,
    constraint foreign key fk_enroll (enroll) references Enroll(id) on delete cascade
);

desc Grade;
desc Enroll;
show create table Grade;

-- 샘플 입력
insert into Grade(enroll, midterm, finalterm)
 select id, mod(id, 50) + 50, ceil((0.5 + rand() / 2) * 100) from Enroll order by id;
 
 
-- 샘플 점수 검증
select min(midterm), max(midterm), min(finalterm), max(finalterm) from Grade;

select (select count(*) from Enroll) enroll, (select count(*) from Grade) grade;


-- R#1 과목별 수강생(과목/성적순)
select subject_name '과목명', student_name '학생명', midterm '중간고사', total '총점', round(average, 1) '평균',
      (case when average >= 90 then 'A'
            when average >= 80 then 'B'
            when average >= 70 then 'C'
            when average >= 60 then 'D'
            else 'F' end) as '학점'
  from (
        select sbj.name as subject_name, stu.name as student_name, g.midterm, g.finalterm, (g.midterm + g.finalterm) as total, (g.midterm + g.finalterm) / 2 as average
          from Grade g inner join Enroll e on g.enroll = e.id
                       inner join Subject sbj on e.subject = sbj.id
                       inner join Student stu on e.student = stu.id
       ) sub
 order by sub.subject_name, sub.average desc;
 
-- 검증
select e.id, g.enroll, sbj.name, stu.name, g.midterm, g.finalterm, (g.midterm + g.finalterm) as total, (g.midterm + g.finalterm) / 2 as average,
       (select (midterm + finalterm) g_total from Grade where id = g.id) as ggg
  from Grade g inner join Enroll e on g.enroll = e.id
               inner join Subject sbj on e.subject = sbj.id
               inner join Student stu on e.student = stu.id
 order by sbj.name, (g.midterm + g.finalterm) desc;
 
 
 
-- R#2 과목별 통계 리포트(과목순)
select sbj.id, max(sbj.name) '과목명', count(*) '학생수', avg(g.midterm + g.finalterm) '평균',
       (select sstu.name
         from Grade gg inner join Enroll ee on gg.enroll = ee.id
                       inner join Student sstu on ee.student = sstu.id
         where ee.subject = sbj.id order by (gg.midterm + gg.finalterm) desc limit 1) '최고득점자'
  from Grade g inner join Enroll e on g.enroll = e.id
               inner join Subject sbj on e.subject = sbj.id
 group by sbj.id order by 과목명;

-- 과목별 학생수 검증
select subject, count(*) from Enroll group by subject;

-- 첫번째 과목 평균 검증
select avg(midterm), avg(finalterm), avg(midterm + finalterm), sum(midterm + finalterm) / count(*)
  from Grade where enroll in (select id from Enroll where subject=1);
  
-- 최고득점자 검증
select (gg.midterm + gg.finalterm), ee.student, (select name from Student where id = ee.student)
  from Grade gg inner join Enroll ee on gg.enroll = ee.id
 where ee.subject = 1
 order by (gg.midterm + gg.finalterm) desc;
 
 
 
 
 
-- R#3  학생별 통계

-- 1) 학생별 sum
select @rownum := @rownum + 1, e.student, sum(g.midterm) mterm, sum(g.finalterm) fterm, sum(g.midterm), sum(g.finalterm) as 'total', count(*) sbj_cnt
  from Grade g inner join Enroll e on g.enroll = e.id, (select @rownum := 0) t
 group by e.student;
 
-- 2) 결과에 학생명, 평점 적용
select stu.name '학생명', sbj_cnt '과목수', total '총점', round(average,2) '평균', 
      (case when average >= 90 then 'A'
            when average >= 80 then 'B'
            when average >= 70 then 'C'
            when average >= 60 then 'D'
            else 'F' end) as '학점''평점'
  from (
    select e.student, sum(g.midterm) mterm, sum(g.finalterm) fterm, sum(g.midterm) + sum(g.finalterm) as 'total', avg(g.midterm + g.finalterm) / 2 average, count(*) sbj_cnt
      from Grade g inner join Enroll e on g.enroll = e.id
     group by e.student
       ) sub inner join Student stu on sub.student = stu.id
 order by sub.average desc;
 
select * from Pp;
 
 
-- 3) 석차 표현 (@rownum 사용 또는 임시테이블사용)
select (@rownum := @rownum + 1) as '석차', stu.name '학생명', sbj_cnt '과목수', total '총점', round(average,2) '평균', 
      (case when average >= 90 then 'A'
            when average >= 80 then 'B'
            when average >= 70 then 'C'
            when average >= 60 then 'D'
            else 'F' end) as '학점''평점'
  from (
    select e.student, sum(g.midterm) mterm, sum(g.finalterm) fterm, sum(g.midterm) + sum(g.finalterm) as 'total', avg(g.midterm + g.finalterm) / 2 average, count(*) sbj_cnt
      from Grade g inner join Enroll e on g.enroll = e.id
     group by e.student
       ) sub inner join Student stu on sub.student = stu.id, (select @rownum := 0) ttt
 order by sub.average desc, sbj_cnt desc;
 
 
select s.*, (@rownum := @rownum + 1) from Subject s, (select @rownum := 0) rn;



-- 임시테이블 사용
create temporary table r3 (id int auto_increment primary key, name varchar(31), sjbcnt tinyint, total smallint, average float(5,2), grade varchar(10));

insert into r3(name, sjbcnt, total, average, grade)
select stu.name '학생명', sbj_cnt '과목수', total '총점', round(average,2) '평균', 
      (case when average >= 90 then 'A'
            when average >= 80 then 'B'
            when average >= 70 then 'C'
            when average >= 60 then 'D'
            else 'F' end) as '학점''평점'
  from (
    select e.student, sum(g.midterm) mterm, sum(g.finalterm) fterm, (sum(g.midterm) + sum(g.finalterm)) as 'total', avg(g.midterm + g.finalterm) / 2 average, count(*) sbj_cnt
      from Grade g inner join Enroll e on g.enroll = e.id
     group by e.student
       ) sub inner join Student stu on sub.student = stu.id
 order by sub.average desc;

select * from r3;



COMMIt;

























