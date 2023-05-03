create or replace function get_users_by_namepart7(name_part varchar(256))
    returns table(
        name_ varchar,
        surname varchar,
        phone integer
    )
as 
$$

declare pattern varchar = name_part;

begin
  return query
    select * from phonebook where first_name like concat(pattern, '%');
end;
$$ language plpgsql;
 