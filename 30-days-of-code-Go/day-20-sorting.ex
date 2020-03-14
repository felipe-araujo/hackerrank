defmodule Solution do

  def sort(array) do
    List.foldl(
      Enum.to_list(0..length(array)-1),
      {[], array, 0}, fn _,
      {sorted, list, counter} ->
        outer_step({sorted, list, counter})
      end
    )
  end

  def outer_step({sorted, [], counter}) do
    step({[], sorted, counter})
  end

  def outer_step({[], list, counter}) do
    step({[], list, counter})
  end

  def step({sorted, [h | []], counter}) do
    {sorted ++ [h], [],counter}
  end

  def step({sorted, [h | t], counter}) do

    if h > hd(t) do
      step({sorted ++ [hd(t)],  [h] ++ tl(t), counter+1})
    else
      step({sorted ++ [h], t, counter})
    end
  end

end

_size = IO.read(:stdio, :line)

array = IO.read(:stdio, :line)
array = array
  |> String.trim
  |> String.split(" ")
  |> Enum.map(fn n -> String.to_integer(n) end)

{ sorted, _, swaps } = Solution.sort(array)
first = hd(sorted)
last = List.last(sorted)
IO.puts("Array is sorted in #{swaps} swaps.")
IO.puts("First Element: #{first}")
IO.puts("Last Element: #{last}")


