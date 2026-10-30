def matrix_dot_vector(
    a: list[list[int | float]], b: list[int | float]
) -> list[int | float] | int:
  # Base dimension check: empty matrix or column count != vector length
  if not a or len(a[0]) != len(b):
    return -1

  # Compute dot product using list comprehension and zip
  return [sum(r * v for r, v in zip(row, b)) for row in a]