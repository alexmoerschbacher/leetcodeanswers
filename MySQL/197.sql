Select w1.id From Weather w1, Weather w2
Where w1.Temperature > w2. Temperature and w2.recordDate = DATE_SUB(w1.recordDate, INTERVAL 1 Day);