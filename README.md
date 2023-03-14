# pgwrapper

*A simple, fast way to access postgresql in python.*


### Description

* It is a postgresql python connection pool at lower layer.

* It is a mongo-like query formula system upper layer.

* It is a new version to access postgresql in python3.


### Install
pip install pgwrapper


### Usage

```
>>> import pgwrapper
>>> pg = pgwrapper.PGWrapper(
        dbname='postgres',
        user='postgres',
        password='',
        host='127.0.0.1',
        port=5432)
>>> r = pg.select('company', 'id, name', 'address is not null', 'limit 2')
>>> print(r)

[(12, 'sun'), (34, 'moon')]
```

###### select
```
    >>> select('hospital', 'id, city', control='limit 1')
    select id, city from hospital limit 1;


    >>> select('hospital', 'id', 'address is null')
    select id from hospital where address is null;
```

###### update
```
    >>> update('dept', {'name': 'design', 'quantity': 3}, {'id': 'we4d'})
    update dept set name='design', quantity=3 where id='we4d';

    >>> update('dept', {'name': 'design', 'quantity': 3}, 'introduction is null')
    update dept set name='design', quantity=3 where introduction is null;

    >>> update('physician', {'$inc': {'status': -10}, 'present': 0}, {'id': 'someid'})
    update physician set status=status+-10, present=0 where id='someid';
```

###### insert
```
    >>> insert('hospital', {'id': '12de3wrv', 'province': 'shanghai'})
    insert into hospital (id, province) values ('12de3wrv', 'shanghai');

```

insert use list way:
```
    >>> insert_list('hospital', ['id', 'province'], ['12de3wrv', 'shanghai'])
    insert into hospital (id, province) values ('12de3wrv', 'shanghai');
```

insert if the record not in the table:
```
    >>> insert_inexistence('hospital', {'id': '12de3wrv', 'province': 'shanghai'}, {'id': '12de3wrv'})
    insert into hospital (id, province) select '12de3wrv', 'shanghai' where not exists (select 1 from hospital where id='12de3wrv' limit 1);
```


###### delete
```
    >>> delete('hospital', {'id': '12de3wrv'})
    delete from hospital where id='12de3wrv';

```

###### join
comman join
```
    >>> joint('user', 'name, id_number', 'medical_card', 'number', 'id', 'user_id', 'inner_join')
    select u.name, u.id_number, v.number from user as u inner join medical_card as v on u.id=v.user_id;

```

left join
```
    >>> select_join('hospital', 'id', 'department', 'hospid')
    select hospital.id from hospital left join department on hospital.id=department.hospid where department.hospid is null;
```



### Issue

```Error: pg_config executable not found.```
If you meet this following error when installing psycopg2, you may need to install extra library.

In Ubuntu:
```sudo apt install libpq-dev```

In macOs:
```brew install postgresql```
