create or replace function pag(limit_ integer, offset_ integer)
    returns table(
        name_ varchar,
        surname varchar,
        phone integer
    )
as 
$$

begin
  return query
    select * from phonebook limit limit_ offset offset_;
end;
$$ language plpgsql;