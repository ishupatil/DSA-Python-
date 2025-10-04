SELECT 
    A_start.machine_id,
    ROUND(
        AVG(A_end.timestamp-A_start.timestamp),3)as processing_time
FROM Activity as A_start JOIN Activity as A_end
on
     A_start.machine_id=A_end.machine_id 
    and
     A_start.process_id=A_end.process_id
WHERE A_start.activity_type='start'
      AND A_end.activity_type='end'

GROUP by A_start.machine_id;


    
   