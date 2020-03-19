use Bitwise
defmodule Solution do

  def solve([a, k]) when a <= 10 do
    pairs(Enum.to_list(1..a))
      |> Enum.map(fn [x, y] -> band(x, y) end)
      |> Enum.filter(fn t -> t < k end)
      |> (fn data -> Enum.max([0|data]) end).()
      #|> Enum.max(&1, &>=/2, fn -> 0 end)
  end

  def solve([a, k]) when 2*k >= a do
    pairs(Enum.to_list(closest_power(k)-2..a))
      |> Enum.map(fn [x, y] -> band(x, y) end)
      |> Enum.filter(fn t -> t < k end)
      |> (fn data -> Enum.max([0|data]) end).()
      #|> Enum.max(&1, &>=/2, fn -> 0 end)
  end

  def solve([a, k]) when 2*k < a do
    k-1
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

  def closest_power(x) do
    case x do
      2 -> 1
      _ -> closest_power(x, 1, 2)
    end
  end

  def closest_power(x, n, acc) do
    cond do
      2 * acc >= x -> acc
      true -> closest_power(x, n+1, 2*acc)
    end
  end

end

size = IO.read(:stdio, :line)
  |> String.trim
  |> String.to_integer

#IO.puts('size is #{size}')
Enum.to_list(1..size)
  |> Enum.map(fn _ -> IO.read(:stdio, :line) end)
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.split/1)
  |> Enum.map(fn [a, b] -> [String.to_integer(a), String.to_integer(b)] end)
  #|> Enum.map(fn [a, b] -> Solution.closest_power(b) end)
  #|> Enum.each(&IO.inspect/1)
  |> Enum.map(&Solution.solve/1)
  |> Enum.each(&IO.puts/1)
