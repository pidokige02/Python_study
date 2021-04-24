
-- 문제 3
create table ClubMember(
    id int unsigned not null auto_increment primary key, 
    student int unsigned, 
    club smallint unsigned not null,
    level tinyint(1) unsigned not null default 0,
    constraint foreign key fk_stu(student) references Student(id) on delete cascade,
    constraint foreign key fk_club(club) references Club(id) on delete cascade
);

-- 같은학생이 같은 동아리에 중복되지 않도록!!
alter table ClubMember add unique index uk_club_student (student, club);

-- 먼저 리더 처리
insert into ClubMember(club, student, level) select id, leader, 2 from Club where leader is not null;

-- 랜덤하게 학생 약 50명 (세개 클럽이니 150개) 등록
insert ignore into ClubMember(club, student, level)
 select c.id, s.id, 0 from Student s, Club c order by rand() limit 150;

-- 클럽별 몇명의 학생을 간부로 등록
select * from ClubMember where student < 100;   -- 적절하게 id로 끊어서 처리
update ClubMember set level = 1
 where student in (select id from Student where id < 100);
 
-- 클럽짱이 비어있는 4번 클럽에 회원 한명을 클럽짱으로!!
update ClubMember set level=2 where club=4 order by rand() limit 1;

-- 검증
select * from ClubMember;
select club, count(*) from ClubMember group by club;
select club, level, count(*) from ClubMember group by club, level;

drop table ClubMember;

show variables like '%commit%';

START transaction;
commit;


-- 문제 4
create table Dept(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    prof smallint unsigned,
    student int unsigned,
    constraint foreign key fk_prof(prof) references Prof(id) on delete set null,
    constraint foreign key fk_student(student) references Student(id) on delete set null
);

alter table Student add column dept smallint unsigned;
alter table Student add constraint foreign key fk_dept(dept) references Dept(id);

select * from Dept;
select * from Student;
select * from Subject;

-- dept 생성
insert into Dept(name, prof)
 select '국문학과', id from Prof order by rand() limit 10;
 
-- 과이름 정리
select substring('국문학과,통계학과,역사학과,영문학과,물리학과,생물학과,화공학과,수리학과,윤리학과,사회학과', (id - 1) * 5 + 1 , 4) from Dept order by id;
update Dept set name = substring('국문학과,통계학과,역사학과,영문학과,물리학과,생물학과,화공학과,수리학과,윤리학과,사회학과', (id - 1) * 5 + 1 , 4) order by id;

-- 학생테이블 과배정
update Student set dept=(select id from Dept order by rand() limit 1);

-- 과 배정 검증
select dept, count(*) from Student group by dept;

-- Dept 테이블에 학생대표 저장
update Dept d set student = (select id from Student where dept = d.id order by rand() limit 1);

-- 학생대표 검증(해당 과대표가 해당 과 소속인지만 체크)
select d.name, d.student, d.id, (select dept from Student where id = d.student) from Dept d;


show create table Student;
show index from Student;

-- 정리 --------------------------------------------------------
alter table Student drop foreign key Student_ibfk_1;
alter table Student drop index fk_dept;
alter table Student drop column dept;
drop table Dept;
-- ------------------------------------------------------------


-- 문제 5. 강의실 문제
create table Classroom(
    id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null
);

alter table Subject add column classroom smallint unsigned;
alter table Subject add constraint foreign key fk_classroom(classroom) references Classroom(id);

insert into Classroom(name)
select concat('10', id, '호') from Subject;

update Subject set classroom = (11 - id); 

-- 강의실 중복방지
alter table Subject add unique index uk_classroom(classroom);



-- if: rand를 이용한 중복방지
select ceil(rand(id) * 10) from Student;
select distinct(ceil(rand(id) * 10)) rr from Student;

update Subject s, (select distinct(ceil(rand(id) * 10)) rr from Student) x set classroom=x.rr;


select * from Subject;
select * from Classroom;

show create table Subject;
-- 정리 --------------------------------------------------------
alter table Subject drop foreign key Subject_ibfk_2;
alter table Subject drop index fk_classroom;
alter table Subject drop index uk_classroom;
alter table Subject drop column classroom;
drop table Classroom;
-- ------------------------------------------------------------


desc Prof;

desc Club;
select * from Club;

select concat(ceil(rand() * 1000), '호') from Student order by id desc limit 10;

select * from jj;


select id from Subject order by rand();

update jj j inner join Subject s on j.stu <> s.id set j.stu = s.id;
 
 
update jj set stu = (select id from Subject order by rand() limit 1);

create table Pp As select * from jj;

desc Student;
desc Dept;

create table Dept(id int unsigned not null auto_increment primary key, student int unsigned, foreign key fk_aa(student) references Student(id));

alter table Student add column dept int unsigned;

alter table Student add constraint foreign key fk_sss(dept) references Dept(id);

drop table Dept;

SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(A.TEXT, ';', 3), ';', -1) SPILT_TEXT
  FROM (SELECT 'A;B;C;D;E;F;G' TEXT) A;
  
  
select substring_index('a,b,c', ',', -1);

select substring_index(substring_index('a,b,c', ',', 3), ',', -1);


-- -------------------------------------------------------------------

select * from v_grade_enroll where subject = 1 order by avr; 

select group_concat(avr) from v_grade_enroll where subject = 1 order by avr;

select floor(avr / 10), count(*), group_concat( mod(avr, 10) SEPARATOR '' ), group_concat(avr)
  from v_grade_enroll
 where subject = 1
 group by floor(avr / 10)
;

select * from v_grade_enroll;

select subject, max(avr)
  from v_grade_enroll
 group by subject;
 
  
select * from Subject;


-- ------------------------------------------------------------------- sp_grade_stem_leaf
drop procedure if exists sp_grade_stem_leaf;

delimiter $$
create procedure sp_grade_stem_leaf(_subject_name varchar(31))
begin
    declare _stem tinyint;
    declare _avr tinyint;
    declare _done boolean default false;
    
    declare cur_avrs cursor for
        select avr from v_grade_enroll where subject = (select id from Subject where name = _subject_name) order by avr;
        
    declare continue handler for not found 
        set _done := true;
        
    drop table if exists tt;
    
    create temporary table tt(stem tinyint not null primary key, leaf varchar(1024), cnt smallint);
        
    open cur_avrs;
    
        loop1: LOOP
            
            fetch cur_avrs into _avr;
            set _stem = floor(_avr / 10);
            
            IF exists(select * from tt where stem = _stem) THEN
                update tt set leaf = concat(leaf, mod(_avr, 10)), cnt = cnt + 1
                 where stem = _stem;
                 
            ELSE
                insert into tt values(_stem, mod(_avr, 10), 1);
            END IF;
            
            IF _done THEN
                LEAVE loop1;
            END IF;
        
        END LOOP loop1;
    
    close cur_avrs;
    
    select * from tt order by stem;
end $$
delimiter ;

-- ------------------------------------------------------------------- sp_grade_stem_leaf  : END

call sp_grade_stem_leaf('물리');

-- select * from v_grade_enroll where avr = 100;
-- select avr from v_grade_enroll where subject = 3 order by avr;

-- desc Subject;
-- select floor(avr / 10), max(avr) from v_grade_enroll group by floor(avr / 10);

-- select * from v_grade_enroll where avr between 50 and 5 * 10 + 9;

-- select id  from Subject where name = '역사';

-- select subject from v_grade_enroll group by subject having count(*) > 1;



-- ------------------------------------------------------------------------ 평가문제
-- 1)
drop view if exists v_students;

create view v_students AS
    select e.student, s.name, count(distinct e.subject) sbj_cnt, round(avg(g.midterm + g.finalterm) / 2) avr
      from Enroll e inner join Grade g on e.id = g.enroll
                    inner join Student s on e.student= s.id
     group by e.student;

select * from v_students;

-- 2)
drop function if exists f_student_avg;

delimiter //
create function f_student_avg(_student int)
    returns tinyint
BEGIN
    return (select round(avg(g.midterm + g.finalterm) / 2)
              from Grade g inner join Enroll e on g.enroll = e.id
             where e.student = _student);
END //
delimiter ;

select id, f_student_avg(id), name from Student limit 10;


-- 3)
drop trigger if exists tr_club_member;

delimiter //
create trigger tr_club_member
    after insert on Club For Each Row
BEGIN
    insert into ClubMember(club, student)
        select NEW.id, id from Student order by rand() limit 1;
END //
delimiter ;

insert into Club(name) values('테니스부');


-- 4)
drop procedure if exists sp_reco_sbj;

delimiter $$
create procedure sp_reco_sbj()
begin
    declare _tot_avr int;
    declare _tot_stu int;
    declare _tot_likecnt int;
    
    drop table if exists t_reco;
    
    create temporary table t_reco (
        sbj smallint unsigned primary key,
        stucnt smallint,
        avr decimal(5,2),
        prof smallint unsigned,
        sbjname varchar(31),
        profname varchar(31),
        likecnt smallint
    );
        
    -- 과목별
    insert into t_reco(sbj, stucnt, avr, prof, sbjname, profname, likecnt)
        select e.subject, count(*), avg(g.midterm + g.finalterm) / 2, p.id, sbj.name, p.name, p.likecnt
          from Enroll e inner join Grade g on e.id = g.enroll
                        inner join Subject sbj on e.subject = sbj.id
                        inner join Prof p on sbj.prof = p.id
         group by e.subject
      ;
      
    -- 학생은 중복 수강이 가능하므로 과목별 학생수의 총합을 구해 이것을 기준으로 비율을 정함!!
    -- 강의를 한 교수만을 대상으로 전체 likecnt를 구해야 100분율로 나옴!!
    select sum(avr), sum(stucnt), sum(likecnt)
      into _tot_avr, _tot_stu, _tot_likecnt
      from t_reco;
      
      
    select (@rownum := @rownum + 1) ranking, sbjname, profname,
        (avr / _tot_avr), (stucnt / _tot_stu), (likecnt / _tot_likecnt),
        (avr / _tot_avr) * 30 + (stucnt / _tot_stu) * 30 + (likecnt / _tot_likecnt) * 40 score
      from t_reco t, (select @rownum := 0) r
     order by score desc;
      
end $$
delimiter ;

call sp_reco_sbj();


-- 6)  ******************************************** cursor 사용
drop procedure if exists sp_stu_top3_cursor;


-- 6)  ******************************************** cursor 사용 X
drop procedure if exists sp_stu_top3;

delimiter $$
create procedure sp_stu_top3()
begin
    declare _sbj_cnt tinyint;
    declare i int default 0;
    declare _avr tinyint;
    declare _done boolean default false;
    
    declare cur_avrs cursor for
        select * from t;
        
    declare continue handler for not found 
        set _done := true;
        
        
    drop table if exists t_result;
    
    create temporary table t_result(subject smallint, idx smallint, s1 int, s1name varchar(31), s2 int, s2name varchar(31), s3 int, s3name varchar(31));
    
    insert into t_result(subject, idx)
    select v.subject, (@rownum := @rownum + 1) from (select distinct subject from v_grade_enroll) v, (select @rownum := 0) r;
    
    select * from t_result;
    
    
    drop table if exists t;
    
    create temporary table t(subject smallint not null, student int, student_name varchar(31), idx smallint);
    
    select count(*) into _sbj_cnt from t_result;
    
    while i <= _sbj_cnt do
        set i = i + 1;
        
        insert into t
         select subject, student, (select name from Student where id = v.student), (@rn := @rn + 1)
           from v_grade_enroll v, (select @rn := 0) rn
          where subject = (select subject from t_result where idx = i) order by avr limit 3;
        
    end while;
    
    select * from t;
    
    -- non - cursor
    -- update t_result ret 
      --  set ret.s1 = (select student from t where subject = ret.subject and idx = 1),
      --      ret.s2 = (select student from t where subject = ret.subject and idx = 2);
            
    update t_result ret inner join t on ret.subject = t.subject
       set ret.s1 = t.student, ret.s1name = t.student_name
     where t.idx = 1;
     
    update t_result ret inner join t on ret.subject = t.subject
       set ret.s2 = t.student, ret.s2name = t.student_name
     where t.idx = 2;
     
    update t_result ret inner join t on ret.subject = t.subject
       set ret.s3 = t.student, ret.s3name = t.student_name
     where t.idx = 3;
            
        
    select * from t_result;
    
     
end $$
delimiter ;

call sp_stu_top3();


-- ----------------------------------------------------------
CREATE DEFINER=`dooo`@`172.17.0.1` PROCEDURE `sp_drop_foreign_key`(_table varchar(64))
BEGIN
    declare _constraint varchar(64);
    declare _ref_table varchar(64);
    
    Declare _done boolean default False;
    
    Declare _cur CURSOR FOR
        select constraint_name, table_name from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
         where CONSTRAINT_SCHEMA = database() and REFERENCED_TABLE_NAME = _table;
        
    Declare Continue Handler
        For Not Found SET _done := True;
        
    drop table if exists t;
    create table t (sqlstr varchar(1024));
        
    OPEN _cur;
    
        cur_loop: LOOP
        
            Fetch _cur into _constraint, _ref_table;
            IF _done THEN
                LEAVE cur_loop;
            END IF;
            
            set @sql = concat('alter table ', _ref_table, ' drop foreign key ', _constraint);
            insert into t values(@sql);
            
            PREPARE myQuery from @sql;
            EXECUTE myQuery;
            DEALLOCATE PREPARE myQuery;
            
        END LOOP cur_loop;
        
    CLOSE _cur;
    
    select * from t;

END