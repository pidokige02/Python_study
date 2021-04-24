-- 문제 1)
drop view if exists v_students;

create view v_students AS
    select e.student, max(s.name) name, count(*) sbj_cnt, 
        round(avg(g.midterm + g.finalterm) / 2) avr
      from Enroll e inner join Grade g on e.id = g.enroll
                    inner join Student s on e.student = s.id
     group by e.student;
     
     
select * from v_students;

-- 문제 2)
drop function if exists f_student_avg;

delimiter $$
create function f_student_avg(_stu int unsigned) returns decimal(5,2)
begin
    return (select avg(g.midterm + g.finalterm) / 2
      from Grade g inner join Enroll e on g.enroll = e.id
     where e.student = _stu);
end $$
delimiter ;

select name, id, round(f_student_avg(id)) from Student limit 10;

-- 문제 3) 
drop trigger if exists tr_club_member_rand1;
delimiter $$
create trigger tr_club_member_rand1
    after insert on Club for each row
begin
    insert into ClubMember(club, student, level)
        select NEW.id, id, 2
          from Student 
         where id not in (select student from ClubMember where level > 0)
         order by rand() limit 1;
    
end $$
delimiter ;

insert into Club(name) values('3부');

select * from Club order by id desc;

select * from ClubMember
 where club = (select max(id) from Club);


-- 문제4)
drop procedure if exists sp_recommend_top3;
delimiter $$
create procedure sp_recommend_top3()
begin
    declare _avr decimal(8,4);
    declare _stu_cnt smallint;
    declare _likecnt smallint;
    
    drop table if exists t;
    
    create temporary table t (
        subject smallint unsigned primary key,
        avr decimal(7,4),
        stu_cnt smallint,
        likecnt smallint
    );
    
    insert into t
    select v.subject, avg(v.avr) avr, count(*) stu_cnt, max(p.likecnt) likecnt
      from v_grade_enroll v inner join Subject sbj on v.subject = sbj.id
                            inner join Prof p on sbj.prof = p.id
     group by v.subject;
     
    select sum(avr), sum(stu_cnt), sum(likecnt)
      into _avr, _stu_cnt, _likecnt
      from t;
    
    select sbj.name, t.*, 
           (t.avr / _avr) * 3 + (t.stu_cnt / _stu_cnt) * 3 + (t.likecnt / _likecnt) * 5  score
      from t inner join Subject sbj on t.subject = sbj.id
     order by score desc;
end $$
delimiter ;

call sp_recommend_top3();

-- select * from v_grade_enroll;

-- 문제 6)
drop procedure if exists sp_grade_top3;
delimiter $$
create procedure sp_grade_top3()
begin
    declare i smallint default 0;
    declare _sbjcnt smallint;

    drop table if exists t_result;
    
    create temporary table t_result (
        subject smallint primary key,
        stu1 int unsigned,
        stu_name1 varchar(31),
        stu2 int unsigned,
        stu_name2 varchar(31),
        stu3 int unsigned,
        stu_name3 varchar(31),
        rn smallint
    );
    
    insert t_result(subject, rn)
     select v.subject, (@rownum := @rownum + 1) rn
       from (select distinct subject from v_grade_enroll) v, (select @rownum := 0) r;
      
    -- select * from t_result;
    
    drop table if exists t;
    
    create temporary table t(
        subject smallint, 
        student int unsigned,
        name varchar(31),
        avr tinyint,
        idx tinyint
    );
    
    select count(*) into _sbjcnt from t_result;
    
    while i < _sbjcnt do
        set i = i + 1;
        
        insert into t
        select v.subject, v.student,
               (select name from Student where id = v.student),
              v.avr, (@rn := @rn + 1) rn
          from v_grade_enroll v, (select @rn := 0) r
         where v.subject = (select subject from t_result where rn = i)
         order by avr desc limit 3;
         
    end while;
    
    set i = 0;
    while i < _sbjcnt do
        
        /*
        update t_result ret
           set stu1 = (select student from t
                        where subject = ret.subject and idx = 1),
               stu_name1 = (select name from t
                        where subject = ret.subject and idx = 1),
               stu2 = (select student from t
                        where subject = ret.subject and idx = 2),
               stu_name2 = (select name from t
                        where subject = ret.subject and idx = 2),
               stu3 = (select student from t
                        where subject = ret.subject and idx = 3),
               stu_name3 = (select name from t
                        where subject = ret.subject and idx = 3);
                        
        */
        
        update t_result ret inner join t on ret.subject = t.subject
           set stu1 = t.student, stu_name1 = t.name
         where t.idx = 1;
         
        update t_result ret inner join t on ret.subject = t.subject
           set stu2 = t.student, stu_name2 = t.name
         where t.idx = 2;
         
        update t_result ret inner join t on ret.subject = t.subject
           set stu3 = t.student, stu_name3 = t.name
         where t.idx = 3;
           
                        
        set i = i + 1;
    end while;
    
    alter table t_result drop column rn;
    
    select * from t_result;
end $$
delimiter ;

call sp_grade_top3();
