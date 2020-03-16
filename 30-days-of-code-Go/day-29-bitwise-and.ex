use Bitwise
defmodule Solution do
  def solve(args) do
    [array, k] = args
    Enum.map(pairs(array), fn [a, b] -> band(a,b) end)
      |> Enum.filter(fn t -> t<k end)
      |> Enum.max
  end
  def pairs(list) do
    perms(list)
  end

  def perms([head | tail]) do
    case tail do
      [] -> []
      _ -> Enum.map(tail, fn t -> [head, t] end)
            ++ perms(tail)
    end
  end

end

size = IO.read(:stdio, :line)
  |> String.trim
  |> String.to_integer

Enum.to_list(1..size)
  |> Enum.map(fn _ -> IO.read(:stdio, :line) end)
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.split/1)
  |> Enum.map(fn [a, b] -> [String.to_integer(a), String.to_integer(b)] end)
  |> Enum.map(fn [a, b] -> [Enum.to_list(1..a), b] end)
  |> Enum.map(&Solution.solve/1)
  |> Enum.each(&IO.puts/1)
