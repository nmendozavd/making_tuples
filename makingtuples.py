"""
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"}

  def making_tuples(arr):
    output = []
    for i in arr:
        output.append((i,arr[i]))
    print output

making_tuples(my_dict)
"""



my_dict = {
  "Speros": "(555) 555-5555",
  "Mike": "(999) 999-9999",
  "John": "(777) 777-7777"
}

def making_tuples(dict):
  print my_dict.items()

making_tuples(my_dict)
