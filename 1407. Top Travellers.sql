# Write your MySQL query statement below
select
    name,
    coalesce(sum(distance), 0) as travelled_distance
from Rides
    right outer join Users on Rides.user_id = Users.id
group by Users.id
order by
    sum(distance) desc,
    length(name) desc