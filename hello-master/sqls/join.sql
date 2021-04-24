select s.*, p.name as 'prof. name'
  from Subject s inner join Prof p on s.prof = p.id;
  
select e.subject, max(s.name) as 'subject name', count(*) as '학생수'
  from Enroll e inner join Subject s on e.subject = s.id
  group by e.subject;
  
select e.subject, max(s.name) as 'subject name', count(*) as '학생수'
  from Enroll e inner join Subject s on e.subject = s.id
  group by e.subject;
  
select student_name, birth
  from v_enroll_student_subject
 where subject_name = '역사';
 
select * from v_enroll_student_subject;
 
select s.name, s.birth
  from v_enroll_student_subject
 where sbj.name = '국어' and s.addr = '서울';
 
select addr, count(*), min(student_name)
  from v_enroll_student_subject
 where subject_name = '역사' group by addr;
 
select sbj.id, max(sbj.name), s.addr, count(*)
  from Enroll e inner join Student s on e.student = s.id
                inner join Subject sbj on e.subject = sbj.id
 group by sbj.id, s.addr;
 
select substring(s.addr,1,2) as a, count(*) as student_cnt
  from Enroll e inner join Student s on e.student = s.id
                inner join Subject sbj on e.subject = sbj.id
 where sbj.name = '역사' group by a;
 
select * from Club;

select c.*, s.name from Club c left outer join Student s on c.leader = s.id;

select * from Prof;

select p.*, sbj.name from Subject sbj right outer join Prof p on sbj.prof = p.id;