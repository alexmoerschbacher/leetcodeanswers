select email
from Person
Group By email HAVING count(*)>1