# Write your MySQL query statement below
select
    reports_to as employee_id, (
        select name
        from Employees
        where
            employee_id = test.reports_to
    ) as name,
    count(reports_to) as reports_count,
    round(avg(age)) as average_age
from Employees as test
where reports_to is not null
group by reports_to
order by employee_id asc