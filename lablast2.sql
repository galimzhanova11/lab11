create or replace procedure insert_to_table(
    new_name varchar,
    new_surname varchar,
    new_phone numeric
)
as
$$

begin
    insert into phonebook(first_name, last_name, phone_num) values($1, $2, $3)  ;
end;
$$ language plpgsql;