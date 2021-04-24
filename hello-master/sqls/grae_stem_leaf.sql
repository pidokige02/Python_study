drop procedure if exists sp_grade_stem_leaf;
delimiter $$
create procedure sp_grade_stem_leaf(_subject_name varchar(31))
begin
    declare _isdone boolean default False;
    declare _avr tinyint;
    declare _stem tinyint;
    declare _leaf tinyint;
    
    declare cur_avrs cursor for
        select avr from v_grade_enroll
         where subject = (select id from Subject where name = _subject_name)
         order by avr;
         
    declare continue handler 
        for not found set _isdone = True;
        
    drop table if exists t_grade;
    
    create temporary table t_grade (
        stem tinyint default 0 primary key,
        leaf varchar(1024) default '',
        cnt smallint default 0
    );
        
    open cur_avrs;
    
    loop1: LOOP
        FETCH cur_avrs into _avr;
        
        set _stem = floor(_avr / 10);
        set _leaf = mod(_avr, 10);
        
        IF exists(select * from t_grade where stem = _stem) THEN
            update t_grade set leaf = concat(leaf, _leaf),
                               cnt = cnt + 1
             where stem = _stem;
             
        ELSE
            insert into t_grade value(_stem, _leaf, 1);
            
        END IF;
        
        IF _isdone THEN
            LEAVE loop1;
        END IF;
    
    END LOOP loop1;
    
    close cur_avrs;
    
    select * from t_grade;
    
end $$
delimiter ;

call sp_grade_stem_leaf('국어');

select * from Subject;

/*
select * from v_grade_enroll;

select floor(avr / 10), group_concat(mod(avr, 10))
  from v_grade_enroll
  where subject = 1
  group by floor(avr / 10)
  ;

*/
-- call sp_cnt('select * from Subject');


-- select * from Club;
-- select * from ClubMember;

CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `dooo`@`172.17.0.1` 
    SQL SECURITY DEFINER
VIEW `v_grade_enroll` AS
    SELECT 
        `g`.`id` AS `id`,
        `g`.`midterm` AS `midterm`,
        `g`.`finalterm` AS `finalterm`,
        (`g`.`midterm` + `g`.`finalterm`) AS `total`,
        FLOOR(((`g`.`midterm` + `g`.`finalterm`) / 2)) AS `avr`,
        `g`.`enroll` AS `enroll`,
        `e`.`subject` AS `subject`,
        `e`.`student` AS `student`
    FROM
        (`Grade` `g`
        JOIN `Enroll` `e` ON ((`g`.`enroll` = `e`.`id`)))