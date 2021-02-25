def get_avr(arr, start_index, end_index):
  _sum = 0
  _len = end_index - start_index + 1
  for i in range(start_index, end_index + 1):
    _sum = _sum + arr[i]
  return _sum / _len

def do_thanos(m_arr, s_arr, start_index, end_index):
  print(main_arr)
  if start_index == end_index:
    return
  average = get_avr(m_arr, start_index, end_index)
  left_counter = start_index
  right_counter = end_index
  
  for i in range(start_index, end_index + 1):
    if m_arr[i] <= average:
      s_arr[left_counter] = m_arr[i]
      left_counter = left_counter + 1
    else:
      s_arr[right_counter] = m_arr[i]
      right_counter = right_counter - 1
  
  # переносим в основной массив
  for j in range(start_index, end_index + 1):
    m_arr[j] = s_arr[j]  
  do_thanos(m_arr, s_arr, start_index, right_counter)
  do_thanos(m_arr, s_arr, right_counter + 1, end_index)

main_arr = [97, 25, 42, 90, 71, 16, 82, 39, 36, 74]
length = len(main_arr)
sec_arr = [0 for x in range(length)]
do_thanos(main_arr, sec_arr, 0, length - 1)
