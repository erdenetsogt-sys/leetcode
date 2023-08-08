# Write your MySQL query statement below
Update Salary
set
    sex = case sex
        when 'm' then 'f'
        when 'f' then 'm'
    end