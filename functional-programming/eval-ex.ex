defmodule Solution do
  def exp(x) do
    case x do
      0 -> 1
      _ -> 1 + exp(x, 1, 1, x)
    end
  end

  def exp(num, den, count, x) do
    cond do
      count >= 9 -> num/den
      true -> num/den + exp(num*x, den*(count+1), count+1, x)
    end
  end
end

size = IO.read(:stdio, :line)
  |> String.trim
  |> String.to_integer

Enum.to_list(1..size)
  |> Enum.map(fn _ -> IO.read(:stdio, :line) end)
  |> Enum.map(&String.trim/1)
  |> Enum.map(&String.to_float/1)
  |> Enum.map(&Solution.exp/1)
  |> Enum.each(&IO.puts/1)

