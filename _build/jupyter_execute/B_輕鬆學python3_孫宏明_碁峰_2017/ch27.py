# ch27 類別的私有、保護、公開和靜態成員

## 27-2 類別的私有、保護和公開成員

# %load "27-2/School/main.py
import student as stu

s = stu.Student('李大中', 200, -5, 90)   # 故意傳入錯誤的成績
print(s)   # 測試類別中的__str__()方法
print('學生成績：' + str(s.get_data()))   # 顯示成績：0, 0, 90

s.set_data('李大中', 70, 80, 90)
print('學生成績：' + str(s.get_data()))   # 顯示成績：70, 80, 90

print('學生人數：' + str(stu.Student.get_count()))  # 顯示人數1

# %load "27-2/School/student.py"
class Student:
  _count = 0   # 用來累計物件的個數

  def __init__(self, name, ch_score, en_score, math_score):
    Student._count += 1

    # 呼叫set_data()方法儲存資料
    self.set_data(name, ch_score, en_score, math_score)

  # 取得物件個數。因為不需要用到self參數，所以設定為靜態方法
  @staticmethod
  def get_count():
    return Student._count

  # 儲存學生資料
  def set_data(self, name, ch_score, en_score, math_score):
    self._name = name
    self._ch_score = Student._check_score(ch_score)
    self._en_score = Student._check_score(en_score)
    self._math_score = Student._check_score(math_score)

  # 取得學生資料
  def get_data(self):
    return self._name, self._ch_score, \
      self._en_score, self._math_score

  # 這是私有方法，用來檢查成績是否合法
  # 因為不需要用到self參數，所以設定為靜態方法
  @staticmethod
  def _check_score(score):
    if 0 <= score <= 100:
      return score
    else:
      return 0

  # 這個方法會在執行print()的時候呼叫，取得要顯示字串
  def __str__(self):
    return self._name

## 27-3 模擬教室和學生的物件導向程式專案

# %load "27-3/School/main.py"
import campus as ca

# 這個函式用來顯示教室中的學生


def show_students(classroom1, classroom2):
  print('第一個教室：')
  for s in classroom1.get_all_students():
    print(s.get_data())

  print('第二個教室：')
  for s in classroom2.get_all_students():
    print(s.get_data())


# 建立學生物件
student1 = ca.Student('學生1', 100, 100, 100)
student2 = ca.Student('學生2', 90, 90, 90)
student3 = ca.Student('學生3', 80, 80, 80)
student4 = ca.Student('學生4', 70, 70, 70)
student5 = ca.Student('學生5', 60, 60, 60)

# 建立教室物件
classroom1 = ca.Classroom()
classroom2 = ca.Classroom()

# 把學生加入教室
print('----- 學生進入教室 -----')
classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)

classroom2.add_student(student4)
classroom2.add_student(student5)

# 顯示每一個教室的學生
show_students(classroom1, classroom2)

# 把學生從教室刪除
print('----- 學生離開教室 -----')
classroom1.delete_student(student1)
classroom2.delete_student(student4)

# 顯示每一個教室的學生
show_students(classroom1, classroom2)

# 清空教室
print('----- 放學後 -----')
classroom1.clear()
classroom2.clear()

# 顯示每一個教室的學生
show_students(classroom1, classroom2)

# %load "27-3/School/campus/student.py
class Student:
  _count = 0   # 用來累計物件的個數

  def __init__(self, name, ch_score, en_score, math_score):
    Student._count += 1

    # 呼叫set_data()方法儲存資料
    self.set_data(name, ch_score, en_score, math_score)

  # 取得物件個數。因為不需要用到self參數，所以設定為靜態方法
  @staticmethod
  def get_count():
    return Student._count

  # 儲存學生資料
  def set_data(self, name, ch_score, en_score, math_score):
    self._name = name
    self._ch_score = Student._check_score(ch_score)
    self._en_score = Student._check_score(en_score)
    self._math_score = Student._check_score(math_score)

  # 取得學生資料
  def get_data(self):
    return self._name, self._ch_score, \
      self._en_score, self._math_score

  # 這是私有方法，用來檢查成績是否合法
  # 因為不需要用到self參數，所以設定為靜態方法
  @staticmethod
  def _check_score(score):
    if 0 <= score <= 100:
      return score
    else:
      return 0

  # 這個方法會在執行print()的時候呼叫，取得要顯示字串
  def __str__(self):
    return self._name

# %load "27-3/School/campus/classroom.py
class Classroom:
  def __init__(self):
    self._students = []   # 用來儲存學生的list資料組

  # 這個方法用來加入學生
  def add_student(self, student):
    self._students += [student]

  # 這個方法用來刪除學生
  def delete_student(self, student):
    self._students.remove(student)

  # 這個方法用來取得全部學生
  def get_all_students(self):
    return self._students

  # 這個方法用來清空教室
  def clear(self):
    self._students.clear()

  # 這個方法會傳回教室中的學生人數
  def get_student_number(self):
    return len(self._students)

