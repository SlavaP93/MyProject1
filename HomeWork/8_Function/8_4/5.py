def func_open(new_list,lst=None):
  if lst is None:
    lst = []
  for i_ind, i_elem in enumerate(new_list):
      if isinstance(i_elem,list):
          func_open(new_list[i_ind],lst)
      elif isinstance(i_elem,(int,float)):
          print(i_elem)
          lst.append(i_elem)
  return lst


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(func_open(nice_list))