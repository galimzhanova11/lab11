create or replace procedure add_to_table(arr varchar[])
as
$$

begin
    insert into phonebook(first_name, last_name, phone_num) values($1, $2, $3)  ;
end;
$$ language plpgsql;

CREATE OR REPLACE PROCEDURE insert_many_users2(a varchar)

AS $$

DECLARE
    x int;

BEGIN
    FOR x in 1..5
        LOOP

        IF length(a[x][1]) = 11 THEN

            INSERT INTO phonebook(first_name, last_name, phone_num)  
	        VALUES(a[x][1], a[x][2], a[x][3]);

        ELSE
            INSERT INTO phonebook(first_name, last_name, phone_num)  
	        VALUES(a[x][1], a[x][2], 'wrong num');

                
        END IF;

        END LOOP;
    RETURN;
	
END; $$
LANGUAGE plpgsql;