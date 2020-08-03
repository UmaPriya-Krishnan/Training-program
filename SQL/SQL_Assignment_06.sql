umapriya.krishnan
11740611

1.select e.emp_id,e.emp_name,
count(*) over(partition by d.desc_id) as emp_desc_cnt,
count(*) over(partition by pl.place_id) as emp_place_cnt,
case when desc_name is null 
then 'others'
else desc_name
end as desc_name1,
case when place_desc is null 
then 'others'
else place_desc
end as place_desc1
from employee e left join designation d
on e.desc_id=d.desc_id
left join place pl on pl.place_id=e.place_id order by e.emp_id;

2 .select e.emp_id,e.emp_name,
case when desc_name is null then 'others'
else desc_name end as desc_name,
case when place_desc is null then 'others'
else place_desc end as place_desc,
case when proj_name is null then 'others'
else proj_name end as proj_name
from employee e left join designation d
on e.desc_id=d.desc_id left join place pl 
on e.place_id=pl.place_id left join project p                 
on e.proj_id=p.proj_id
where p.proj_name like '%Data%' or p.proj_name like '%Cloud%' order by e.emp_id;   

3. select * from (
select EMP_ID,emp_name,d.desc_id,pl.PLACE_ID,p.PROJ_ID,dense_rank() over (partition by e.place_id order by e.desc_id desc,e.proj_id ) a
from employee e  join designation d on e.desc_id=d.desc_id
join place pl on e.place_id=pl.place_id
join project p on e.proj_id=p.proj_id)a where a=1;


4. select sales_manager_name,cust_name from (
select cust_name,s1.salesman_id,s1.sales_manager_id,s2.salesman_name sales_manager_name,purchased_amount,
dense_rank() over (partition by s1.sales_manager_id order by purchased_amount desc) rn from customer c
join salesman s1 on c.salesman_id=s1.salesman_id join salesman s2
on s1.sales_manager_id=s2.salesman_id)sal
where rn=1;


