create or replace procedure delete_by_name(
    name_ varchar)
as 
$$
declare
    user record;
begin 
    delete from phonebook where first_name = name_;
end;
$$ language plpgsql;   
