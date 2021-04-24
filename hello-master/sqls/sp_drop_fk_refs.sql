DROP procedure IF EXISTS `sp_drop_fk_refs`;

DELIMITER $$
CREATE DEFINER=`dooo`@`172.17.0.1` PROCEDURE `sp_drop_fk_refs`(_table varchar(64))
BEGIN
    declare _table_name varchar(64);
    declare _constraint_name varchar(64);
    Declare _done boolean default False;
    
    Declare _cur CURSOR FOR
        select table_name, constraint_name
          from INFORMATION_SCHEMA.KEY_COLUMN_USAGE
         where constraint_schema = database()
           and referenced_table_name = _table;
       
    Declare Continue Handler
        For Not Found SET _done := True;
        
    drop table if exists t_ret;
    create temporary table t_ret(sqlstr varchar(1024));
          
    OPEN _cur;
        cur_loop: LOOP
            Fetch _cur into _table_name, _constraint_name;
            
            IF _done THEN
                LEAVE cur_loop;
            END IF;
            
            select _table_name, _constraint_name from dual;
            
            set @sql = concat('alter table ', _table_name, ' drop foreign key ', _constraint_name);
            
            insert into t_ret values(@sql);
            
            PREPARE myQuery from @sql;
            EXECUTE myQuery;
            DEALLOCATE PREPARE myQuery;
            
        END LOOP cur_loop;
    CLOSE _cur;
    
    select * from t_ret;

END$$

DELIMITER ;

