'''
查询练习题：
	查询所有同学的学号、姓名、选课数、总成绩；
	select score.student_id,sum(score.number),count(score.student_id),student.sname from score left join student on score.student_id = student.sid group by score.student_id
	查询姓“李”的老师的个数；
    select count(tid) from teacher where tname like '李%'
	查询平均成绩大于60分的同学的学号和平均成绩；
	select student_id,avg(number) from score group by student_id having avg(number) > 60
	查询有课程成绩小于60分的同学的学号、姓名
	select sid,sname from student where sid in (select distinct student_id from score where number < 60)
	删除学习“叶平”老师课的score表记录；
    delete from score where course_id in (select cid from course left join teacher on course.teacher_id = teacher.tid where teacher.tname = '大黄蜂')
	查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
    select course_id, max(number) as max_num, min(number) as min_num from score group by course_id;
	查询每门课程被选修的学生数；
    select course_id, count(1) from score group by course_id;
	查询出只选修了一门课程的全部学生的学号和姓名；
	 select student.sid, student.sname, count(1) from score left join student on score.student_id  = student.sid group by course_id having count(1) = 1
	查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
    select sname,number from score= left join student on score.student_id = student.sid where score.course_id in (select course.cid from course left join teacher on course.teacher_id = teacher.tid where tname='擎天柱') order by number desc limit 1;
	查询两门以上不及格课程的同学的学号及其平均成绩；
	select student_id,count(1) from score where number < 60 group by student_id having count(1) > 2
'''