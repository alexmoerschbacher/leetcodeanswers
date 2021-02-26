select class 
from courses
Group by class having count(distinct student)>4